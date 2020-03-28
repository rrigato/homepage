from bs4 import BeautifulSoup
import logging
import os
import requests

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
    reddit_headers = {"user-agent":
        "Lambda:toonamiratings:v1.0 (by /u/toonamiratings)"
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

def get_news_flair(access_token, fullname_after):
    """Retrieves toonami subreddit posts after a given reddit post
        Post must have a flair of News

        Parameters
        ----------
        access_token : str
            access_token retrieved from get_oauth_token

        client_secret : str
            Secret for the reddit api

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
    '''    
    url_param_dict = {

    }

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
        show_ratings : list
            dict of one saturday nights ratings where the key
            is from the header_columns list and the value
            is from the <tb> html tag

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





def html_table_parse(reddit_post_html):
    """Parses reddit html post to get data from table

        Parameters
        ----------
        reddit_post_html : str
            HTML post for the table


        Returns
        -------


        Raises
        ------
    """
    bs_obj = BeautifulSoup(reddit_post_html, "html5lib")
    header_columns = handle_table_header(bs_obj)
    body_dict = handle_table_body(bs_obj)
    import pdb; pdb.set_trace()


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
    REDDIT_CLIENT_KEY = os.environ.get("REDDIT_CLIENT_KEY")
    REDDIT_CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET")
    #html_table_parse("""<!-- SC_OFF --><div class=\"md\"><table><thead>\n<tr>\n<th align=\"center\">Time</th>\n<th align=\"center\">Show</th>\n<th align=\"center\">Viewers (000)</th>\n<th align=\"center\">18-49 Rating</th>\n<th align=\"center\">18-49 Views (000)</th>\n</tr>\n</thead><tbody>\n<tr>\n<td align=\"center\">11:30</td>\n<td align=\"center\">My Hero Academia</td>\n<td align=\"center\">543</td>\n<td align=\"center\">0.26</td>\n<td align=\"center\">332</td>\n</tr>\n<tr>\n<td align=\"center\">12:00a</td>\n<td align=\"center\">Sword Art Online: Alicization - War of Underworld</td>\n<td align=\"center\">385</td>\n<td align=\"center\">0.19</td>\n<td align=\"center\">245</td>\n</tr>\n<tr>\n<td align=\"center\">12:30a</td>\n<td align=\"center\">Demon Slayer</td>\n<td align=\"center\">358</td>\n<td align=\"center\">0.18</td>\n<td align=\"center\">232</td>\n</tr>\n<tr>\n<td align=\"center\">1:00a</td>\n<td align=\"center\">Food Wars!</td>\n<td align=\"center\">306</td>\n<td align=\"center\">0.16</td>\n<td align=\"center\">207</td>\n</tr>\n<tr>\n<td align=\"center\">1:30a</td>\n<td align=\"center\">Black Clover</td>\n<td align=\"center\">275</td>\n<td align=\"center\">0.15</td>\n<td align=\"center\">196</td>\n</tr>\n<tr>\n<td align=\"center\">2:00a</td>\n<td align=\"center\">Jojo’s Bizarre Adventure: Golden Wind</td>\n<td align=\"center\">235</td>\n<td align=\"center\">0.13</td>\n<td align=\"center\">170</td>\n</tr>\n<tr>\n<td align=\"center\">2:30a</td>\n<td align=\"center\">Naruto: Shippuden</td>\n<td align=\"center\">236</td>\n<td align=\"center\">0.13</td>\n<td align=\"center\">170</td>\n</tr>\n</tbody></table>\n\n<p>Source: <a href=\"https://programminginsider.com/saturday-final-ratings-hbo-premiere-of-hobbs-shaw-beats-nbc-telecast-of-its-parent-2017-film-the-fate-of-the-furious-among-adults-18-49/\">https://programminginsider.com/saturday-final-ratings-hbo-premiere-of-hobbs-shaw-beats-nbc-telecast-of-its-parent-2017-film-the-fate-of-the-furious-among-adults-18-49/</a></p>\n</div><!-- SC_ON -->""")

if __name__ == "__main__":
    main()
