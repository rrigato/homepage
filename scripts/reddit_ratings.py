from bs4 import BeautifulSoup
from dateutil import parser

import boto3
import json
import logging
import math
import os
import requests

'''
    Special user agent that is recommended according to the
    api docs
    <platform>:<app ID>:<version string> (by /u/<reddit username>)
'''
REDDIT_USER_AGENT = "Lambda:toonamiratings:v1.0 (by /u/toonamiratings)"


def get_logger(working_directory=os.getcwd()):
    """Sets up logger

        Parameters
        ----------
        working_directory: str
            Where to put logger, defaults to cwd

        Returns
        -------

        Raises
        ------
    """
    '''
        Adds the file name to the logs/ directory without
        the extension
    '''
    logging.basicConfig(
        filename=os.path.join(working_directory, "logs/",
        os.path.basename(__file__).split(".")[0]),
        format="%(asctime)s %(message)s",
         datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG
         )
    logging.info("\n")

def get_boto_clients(resource_name, region_name='us-east-1'):
    '''Returns the boto client for various aws resources

        Parameters
        ----------
        resource_name : str
            Name of the resource for the client

        region_name : str
                aws region you are using, defaults to
                us-east-1

        Returns
        -------


        Raises
        ------
    '''
    return(
        boto3.client(
            service_name=resource_name, 
            region_name=region_name
        )
    )



def get_client_secrets():
    """Returns reddit client key and reddit client secret 

        Parameters
        ----------

        Returns
        -------
        reddit_client_key : str
            Reddit client key

        reddit_client_secret : str
            Reddit client secret        

        Raises
        ------
    """
    secrets_manager_client = get_boto_clients(resource_name="secretsmanager")


    '''
        Passing the Name of the string to the boto client
    '''
    reddit_client_key = secrets_manager_client.get_secret_value(
        SecretId="/prod/reddit_api_key"
    )

    reddit_client_secret = secrets_manager_client.get_secret_value(
        SecretId="/prod/reddit_api_secret"
    )

    return(
        reddit_client_key["SecretString"],
        reddit_client_secret["SecretString"]
    )


def get_oauth_token(client_key, client_secret):
    """Gets an Oath token from the reddit API

        Parameters
        ----------
        client_key : str
            Key for the reddit api

        client_secret : str
            Secret for the reddit api

        Returns
        -------
        oauth_token : dict
            Dictionary with the oauth_token and expires_in
            keys. Ex:
            {
                "access_token": "<token_value>",
                "token_type": "bearer",
                "expires_in": 3600,
                "scope": "*"
            }

        Raises
        ------
    """
    '''
        user agent specification outlined here:
        https://github.com/reddit-archive/reddit/wiki/API
    '''
    reddit_headers = {
        "user-agent": REDDIT_USER_AGENT
    }
    logging.info("Custom Headers: ")
    logging.info(reddit_headers)
    '''
        grant_type=client_credentials is
        x-www-form-urlencoded which is what indicates
        this is a application only with no
        user sign in
        auth basic auth where key is reddit client key
        and password is reddit client secret
    '''
    oauth_token = requests.post(
        url="https://www.reddit.com/api/v1/access_token",
        auth=(client_key, client_secret),
        data={"grant_type":"client_credentials"},
        headers=reddit_headers
    )
    return(oauth_token.json())

def get_news_flair(access_token,
    posts_to_return, fullname_after=None):
    """Retrieves toonami subreddit posts before a given reddit post
        Post must have a flair of News
        fullname_after is a reddit unique id called a fullname,
        more info is provided in the docs here:
        https://www.reddit.com/dev/api/#fullnames

        Parameters
        ----------
        access_token : str
            access_token retrieved from get_oauth_token

        posts_to_return : int
            Number of reddit posts to return. Defaults
            to 25

        fullname_after : str
            Optional arguement to only include posts
            before a given fullname. Defautls to None


        Returns
        -------
        news_flair_posts : dict
            Dict of all posts with a news reddit flair
            after fullname_after



        Raises
        ------
    """
    '''
        API Query Parameter explanation
        q=flair:news
            Searching posts with a flair of new
        limit=10
            limit of how many posts to return
        sort=new
            sort by new posts
        restrict_sr=on
            restrict subreddit on to only search /r/toonami
        t=all
            time period, all
        raw_json=1
            Converts &lt; &gt; and &amp;
            to < > and & in response body
        after=fullname_after
            fullname is a unique identifier
            of a reddit api object
    '''
    url_param_dict = {
        "q":"flair:news",
        "limit":posts_to_return,
        "sort":"new",
        "restrict_sr":"on",
        "t":"all",
        "after":fullname_after

    }
    reddit_search_url = "https://oauth.reddit.com/r/toonami/search.json?raw_json=1"
    '''
        Iterating over the dict if the value is
        null that url parameter is not included
    '''
    for url_param in url_param_dict.keys():
        if (url_param_dict[url_param] is not None):
            reddit_search_url = (
                reddit_search_url + "&" +
                url_param + "=" +
                str(url_param_dict[url_param])
            )

    logging.info("Final search url:")
    logging.info(reddit_search_url)

    reddit_search_headers = {
        "user-agent":REDDIT_USER_AGENT,
        "Authorization":("Bearer " + access_token)
    }
    '''
        passing oauth token and user-agent as headers
    '''
    news_flair_posts = requests.get(
        reddit_search_url,
        headers=reddit_search_headers
    )
    logging.info("Successfully made search request")

    return(news_flair_posts.json())

def get_ratings_post(news_flair_posts):
    """Retrieves

        Parameters
        ----------
        news_flair_posts : dict
            Dict of all posts after fullname_after

        Returns
        -------
        ratings_post_list : list
            list providing the elements of the reddit
            search api response that are ratings posts
            Ex: [0, 3, 8]

        Raises
        ------
    """
    ratings_post_list = []
    element_counter = 0
    '''
        Iterates over every reddit post looking for
    '''
    for reddit_post in news_flair_posts["data"]["children"]:

        '''
            If the string "ratings" is in the title of the
            post after lowercasing the title string
            then we count that as a ratings related post
        '''
        if (reddit_post["data"]["title"].lower().find("ratings")
            != (-1)):
            logging.info("Rating post found")
            logging.info(reddit_post["data"]["title"])
            logging.info(reddit_post["data"]["name"])

            ratings_post_list.append(element_counter)
        element_counter += 1
    return(ratings_post_list)


def handle_table_header(bs_obj):
    """Converts table header for the html table into list

        Parameters
        ----------
        bs_obj : bs4.BeautifulSoup
            BeautifulSoup Object to parse table header

        Returns
        -------
        header_columns : list
            list of header columns parsed from html table header

        Raises
        ------
    """
    '''
        Gets all table header html tags
        And putting the contents of each of those in a
        list
    '''
    all_th_tags = bs_obj.find("thead").findAll("th")
    logging.info("Found the following table headers: ")
    logging.info(all_th_tags)

    header_columns = []

    for th_tag in all_th_tags:
        header_columns.append(th_tag.text)

    logging.info("header columns parsed: ")
    logging.info(header_columns)

    return(header_columns)

def handle_table_body(bs_obj, header_columns):
    """Converts table body for the html table into dict

        Parameters
        ----------
        bs_obj : bs4.BeautifulSoup
            BeautifulSoup Object to parse table header

        header_columns : list
            list of header columns parsed from html table header

        Returns
        -------
        saturday_ratings : list
            list of dict of one saturday nights ratings where the key
            is from the header_columns list and the value
            is from the <tr> html tag

        Raises
        ------
    """
    '''
        Gets all table header html tags
        And putting the contents of each of those in a
        list
    '''
    all_tr_tags = bs_obj.find("tbody").findAll("tr")

    logging.info("Found this many shows: ")
    logging.info(len(all_tr_tags))

    saturday_ratings = []
    '''
        First iteration is over list of <tr>
        table rows

        individual_show = list of bs4.element.Tag
    '''
    for individual_show in all_tr_tags:
        show_dict = {}
        '''
        Second iteration
        is the columns that will be used for key values
        of each dict in the list

        Iterating over the column name and
        the associated td which will be the value
        of the dict

        These two lists will always be the same length
        becuase each <td> (table data) needs a corresponding
        <tr> (table row)

        dict_key : str
        dict_value : bs4.element.Tag
        '''
        for dict_key, dict_value in zip(header_columns,
            individual_show.findAll("td")):
            '''
                will be something like
                show_dict["Time"] = "11:00"
                Taking text from td tag
            '''
            show_dict[dict_key] = dict_value.text

        ''' Append dict to list '''
        saturday_ratings.append(show_dict)

    return(saturday_ratings)


def handle_table_clean(reddit_post_html, rating_call_counter,
    ratings_title):
    """Cleans the html table reddit post returned

        Parameters
        ----------
        reddit_post_html : str
            HTML post for the table

        rating_call_counter : int
            Sequence starting at 0 that describes
            how many ratings posts have been called

        ratings_title : str
            The title we are attempting to parse the
            date from


        Returns
        -------
        body_dict : dict
            Dict of individual show ratings
            Ex:
            {
                "Time": "12:00a",
                "Show": "My Hero Academia (r)", 
                "Viewers (000)": "590", 
                "18-49 Rating": "0.29", 
                "18-49 Views (000)": "380", 
                "ratings_occurred_on": "2020-05-09"
            }

        Raises
        ------
    """
    bs_obj = BeautifulSoup(reddit_post_html, "html.parser")
    header_columns = handle_table_header(bs_obj)
    body_dict = handle_table_body(
        bs_obj=bs_obj,
        header_columns=header_columns
    )
    logging.info("Cleaned the ratings post")

    '''
        Parses a datetime from the title of the
        post which will originally be something like:
        "Toonami Ratings for November 2nd, 2019"

        Returns tuple where the first element is
        the datetime and the second is the leftover
        string
        (datetime.datetime(2019, 11, 2, 0, 0), ('Toonami Ratings for ', ' ', ', '))
    '''
    ratings_occurred_on = parser.parse(ratings_title,
        fuzzy_with_tokens=True)

    logging.info("Date Parse Fuzzy Logic: ")
    logging.info(ratings_title)
    logging.info(ratings_occurred_on)

    '''
        Iterating over every saturday night ratings
        which is list of dict and adding a new element
        for the datetime on which the ratings occurred
        formatting date in ISO 8601 standard
    '''
    for show_element in body_dict:
        show_element["ratings_occurred_on"] = ratings_occurred_on[0].strftime("%Y-%m-%d")
    return(body_dict)

def iterate_handle_table_clean(news_flair_posts, ratings_post_list,
    ratings_list_to_append):
    """Tests cleaning of ratings data

        Parameters
        ----------
        news_flair_posts : dict
            Dict of all posts with a news reddit flair
            after fullname_after

        ratings_post_list : list
            list providing the elements of the reddit
            search api response that are ratings posts
            Ex: [0, 3, 8]

        ratings_list_to_append : list
            Existing list of dict where each element is
            one saturday night ratings that will be appended to

        Returns
        -------
        all_ratings_list : list
            List of dict where each element is
            one saturday night ratings populated from
            news_flair_list

        Raises
        ------
    """

    '''
        Iterating over just news flair posts
        that are ratings posts
    '''
    for ratings_post in ratings_post_list:
        
        clean_ratings_post = handle_table_clean(
            reddit_post_html=news_flair_posts["data"]["children"][ratings_post]["data"]["selftext_html"],
            rating_call_counter=0,
            ratings_title=news_flair_posts["data"]["children"][ratings_post]["data"]["title"]
        )
        '''
            extend takes all dicts from
            clean_ratings_post and puts them in
            all_ratings_list
        '''
        ratings_list_to_append.extend(clean_ratings_post)


    return(ratings_list_to_append)



def ratings_iteration(number_posts=10):
    """Handles rating iteration

        Parameters
        ----------
        number_posts : int
            Defaults to 10, the number of news posts to 
            search over for ratings.

        Returns
        -------
        all_ratings_list : list
            List of dict where each element is
            one saturday night ratings


        Raises
        ------

    """
    reddit_client_key, reddit_client_secret = get_client_secrets()


    oauth_token = get_oauth_token(
        client_key=reddit_client_key,
        client_secret=reddit_client_secret
        )

    '''
        Initializing ratings post name tracker
        and list
    '''
    fullname_after = None
    all_ratings_list = []

    logging.info("Oauth token for ratings_iteration")
    '''
        If number_posts is None we are only looking
        for the most recent ratings post
    '''
    if (number_posts <= 25):
        news_flair_posts = get_news_flair(
            access_token=oauth_token["access_token"],
            posts_to_return=number_posts)

        ratings_post_list = get_ratings_post(news_flair_posts)

        all_ratings_list = iterate_handle_table_clean(
            news_flair_posts=news_flair_posts,
            ratings_post_list=ratings_post_list,
            ratings_list_to_append=all_ratings_list
        )

        return(all_ratings_list)

    else:
        '''
            Iterate in batches of 25 if we want to 
            iterate all posts
        '''
        assert type(number_posts) is int, (
            "news_flair_posts must be passed an int for posts_to_return"
        )


        '''
            Logic for breaking apart the historical api calls
        '''
        for api_call_count in range(math.ceil(number_posts/25)):
            news_flair_posts = get_news_flair(
                access_token=oauth_token["access_token"],
                posts_to_return=number_posts,
                fullname_after=fullname_after)

            '''
                No more historical posts to search over
            '''
            if news_flair_posts["data"]["dist"] == 0:
                logging.info("No more posts to iterate")
                return(all_ratings_list)

            ratings_post_list = get_ratings_post(news_flair_posts)

            '''
                Small number of news posts does not
                have any ratings posts to return
            '''
            if len(ratings_post_list) == 0:
                logging.info("No more posts to iterate")
                return(all_ratings_list)

            all_ratings_list = iterate_handle_table_clean(
                news_flair_posts=news_flair_posts,
                ratings_post_list=ratings_post_list,
                ratings_list_to_append=all_ratings_list
            )
            '''
                Gets the fullname of the last post
                in the ratings_post_list
                ratings_post_list[len(ratings_post_list) - 1] =
                last element in list
            '''
            fullname_after = news_flair_posts["data"]["children"][
                ratings_post_list[len(ratings_post_list) - 1]
                ]["data"]["name"]

def lambda_handler(event, context):
    """Handles lambda invocation from cloudwatch events rule

        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    """
    get_logger()
    all_ratings_list = ratings_iteration(number_posts=10)

def main():
    """Entry point into the script
        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    """
    get_logger()
    all_ratings_list = ratings_iteration(number_posts=10)

    with open("ratings_placeholder.json", "w") as output_file:
        output_file.write(json.dumps(all_ratings_list))
    #html_table_parse("""<!-- SC_OFF --><div class=\"md\"><table><thead>\n<tr>\n<th align=\"center\">Time</th>\n<th align=\"center\">Show</th>\n<th align=\"center\">Viewers (000)</th>\n<th align=\"center\">18-49 Rating</th>\n<th align=\"center\">18-49 Views (000)</th>\n</tr>\n</thead><tbody>\n<tr>\n<td align=\"center\">11:30</td>\n<td align=\"center\">My Hero Academia</td>\n<td align=\"center\">543</td>\n<td align=\"center\">0.26</td>\n<td align=\"center\">332</td>\n</tr>\n<tr>\n<td align=\"center\">12:00a</td>\n<td align=\"center\">Sword Art Online: Alicization - War of Underworld</td>\n<td align=\"center\">385</td>\n<td align=\"center\">0.19</td>\n<td align=\"center\">245</td>\n</tr>\n<tr>\n<td align=\"center\">12:30a</td>\n<td align=\"center\">Demon Slayer</td>\n<td align=\"center\">358</td>\n<td align=\"center\">0.18</td>\n<td align=\"center\">232</td>\n</tr>\n<tr>\n<td align=\"center\">1:00a</td>\n<td align=\"center\">Food Wars!</td>\n<td align=\"center\">306</td>\n<td align=\"center\">0.16</td>\n<td align=\"center\">207</td>\n</tr>\n<tr>\n<td align=\"center\">1:30a</td>\n<td align=\"center\">Black Clover</td>\n<td align=\"center\">275</td>\n<td align=\"center\">0.15</td>\n<td align=\"center\">196</td>\n</tr>\n<tr>\n<td align=\"center\">2:00a</td>\n<td align=\"center\">Jojo’s Bizarre Adventure: Golden Wind</td>\n<td align=\"center\">235</td>\n<td align=\"center\">0.13</td>\n<td align=\"center\">170</td>\n</tr>\n<tr>\n<td align=\"center\">2:30a</td>\n<td align=\"center\">Naruto: Shippuden</td>\n<td align=\"center\">236</td>\n<td align=\"center\">0.13</td>\n<td align=\"center\">170</td>\n</tr>\n</tbody></table>\n\n<p>Source: <a href=\"https://programminginsider.com/saturday-final-ratings-hbo-premiere-of-hobbs-shaw-beats-nbc-telecast-of-its-parent-2017-film-the-fate-of-the-furious-among-adults-18-49/\">https://programminginsider.com/saturday-final-ratings-hbo-premiere-of-hobbs-shaw-beats-nbc-telecast-of-its-parent-2017-film-the-fate-of-the-furious-among-adults-18-49/</a></p>\n</div><!-- SC_ON -->""")

if __name__ == "__main__":
    main()
