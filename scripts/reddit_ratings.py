from bs4 import BeautifulSoup
import logging
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
        "user-agent":REDDIT_USER_AGENT
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
        "https://www.reddit.com/api/v1/access_token",
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
            Dict of all posts after fullname_after


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


def handle_table_clean(reddit_post_html, rating_call_counter):
    """Cleans the html table reddit post returned

        Parameters
        ----------
        reddit_post_html : str
            HTML post for the table

        rating_call_counter : int
            Sequence starting at 0 that describes
            how many ratings posts have been called


        Returns
        -------


        Raises
        ------
    """
    bs_obj = BeautifulSoup(reddit_post_html, "html5lib")
    header_columns = handle_table_header(bs_obj)
    body_dict = handle_table_body(bs_obj=bs_obj,
        header_columns=header_columns)

    logging.info("Cleaned the ratings post")
    return(body_dict)

def ratings_iteration(number_posts=None):
    """Handles rating iteration

        Parameters
        ----------
        number_posts : int
            Optional arguement, if this is not None
            we only go looking for the most recent ratings,
            otherwise we iterate all posts

        Returns
        -------


        Raises
        ------

    """
    REDDIT_CLIENT_KEY = os.environ.get("REDDIT_CLIENT_KEY")
    REDDIT_CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET")

    oauth_token = get_oauth_token(
        client_key=REDDIT_CLIENT_KEY,
        client_secret=REDDIT_CLIENT_SECRET
        )

    logging.info("Oauth token for ratings_iteration")
    '''
        If number_posts is None we are only looking
        for the most recent ratings post
    '''
    if (number_posts is None):
        news_flair_posts = get_news_flair(
            access_token=oauth_token["access_token"],
            posts_to_return=15)

        ratings_post_list = get_ratings_post(news_flair_posts)

    else:
        '''
            Otherwise we need to iterate over the
            all news posts
        '''
        assert type(number_posts) is int, (
            "news_flair_posts must be passed an int for posts_to_return"
        )

        '''
            Logic for how many posts
            you can search the reddit api for historically
        '''
        for api_limit in range(round(120/posts_to_return)):
            news_flair_posts = get_news_flair(
                access_token=oauth_token["access_token"],
                posts_to_return=posts_to_return)

            '''
                No more historical posts to search over
            '''
            if news_flair_posts["data"]["dist"] ==0:
                logging.info("No more posts to iterate")
                return("Hello WOrlld")

            ratings_post_list = get_ratings_post(news_flair_posts)
            '''
                Iterating over just news flair posts
                that are ratings posts
            '''
            for ratings_post in ratings_post_list:
                clean_ratings_post = handle_table_clean(
                    reddit_post_html=["data"]["children"][ratings_post]["data"]["selftext_html"],
                     rating_call_counter=0)
                print(["data"]["children"][ratings_post]["data"]["title"])
                



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
    ratings_iteration()
    #html_table_parse("""<!-- SC_OFF --><div class=\"md\"><table><thead>\n<tr>\n<th align=\"center\">Time</th>\n<th align=\"center\">Show</th>\n<th align=\"center\">Viewers (000)</th>\n<th align=\"center\">18-49 Rating</th>\n<th align=\"center\">18-49 Views (000)</th>\n</tr>\n</thead><tbody>\n<tr>\n<td align=\"center\">11:30</td>\n<td align=\"center\">My Hero Academia</td>\n<td align=\"center\">543</td>\n<td align=\"center\">0.26</td>\n<td align=\"center\">332</td>\n</tr>\n<tr>\n<td align=\"center\">12:00a</td>\n<td align=\"center\">Sword Art Online: Alicization - War of Underworld</td>\n<td align=\"center\">385</td>\n<td align=\"center\">0.19</td>\n<td align=\"center\">245</td>\n</tr>\n<tr>\n<td align=\"center\">12:30a</td>\n<td align=\"center\">Demon Slayer</td>\n<td align=\"center\">358</td>\n<td align=\"center\">0.18</td>\n<td align=\"center\">232</td>\n</tr>\n<tr>\n<td align=\"center\">1:00a</td>\n<td align=\"center\">Food Wars!</td>\n<td align=\"center\">306</td>\n<td align=\"center\">0.16</td>\n<td align=\"center\">207</td>\n</tr>\n<tr>\n<td align=\"center\">1:30a</td>\n<td align=\"center\">Black Clover</td>\n<td align=\"center\">275</td>\n<td align=\"center\">0.15</td>\n<td align=\"center\">196</td>\n</tr>\n<tr>\n<td align=\"center\">2:00a</td>\n<td align=\"center\">Jojo’s Bizarre Adventure: Golden Wind</td>\n<td align=\"center\">235</td>\n<td align=\"center\">0.13</td>\n<td align=\"center\">170</td>\n</tr>\n<tr>\n<td align=\"center\">2:30a</td>\n<td align=\"center\">Naruto: Shippuden</td>\n<td align=\"center\">236</td>\n<td align=\"center\">0.13</td>\n<td align=\"center\">170</td>\n</tr>\n</tbody></table>\n\n<p>Source: <a href=\"https://programminginsider.com/saturday-final-ratings-hbo-premiere-of-hobbs-shaw-beats-nbc-telecast-of-its-parent-2017-film-the-fate-of-the-furious-among-adults-18-49/\">https://programminginsider.com/saturday-final-ratings-hbo-premiere-of-hobbs-shaw-beats-nbc-telecast-of-its-parent-2017-film-the-fate-of-the-furious-among-adults-18-49/</a></p>\n</div><!-- SC_ON -->""")

if __name__ == "__main__":
    main()
