from bs4 import BeautifulSoup
from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

import json
import logging
import os
import requests
import unittest


'''
Where the python script was executed from
'''
WORKING_DIRECTORY = os.getcwd()
os.sys.path.append(WORKING_DIRECTORY)
from util.test_reddit_rating_config import REDDIT_RATING_TABLE_2019
from util.test_reddit_rating_config import REDDIT_RATING_TABLE_2020

def get_logger():
    """Sets up logger

        Parameters
        ----------

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
        filename=os.path.join(WORKING_DIRECTORY, "logs/",
        os.path.basename(__file__).split(".")[0]),
        format="%(asctime)s %(message)s",
         datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG
         )
    logging.info("\n")

class RedditApi(unittest.TestCase):
    """Testing the reddit api pull

        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    """
    @classmethod
    def setUpClass(self):
        """Unitest function that is run once for the class

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        get_logger()


    def test_get_oath_token(self):
        """Tests oath token returned from reddit api

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test of oath key")
        from scripts.reddit_ratings import get_oauth_token
        self.assertIsNotNone(os.environ.get(
            "REDDIT_CLIENT_KEY"
        ))
        self.assertIsNotNone(os.environ.get(
            "REDDIT_CLIENT_SECRET"
        ))
        logging.info("Validated environment variables")
        oauth_token = get_oauth_token(
            client_key=os.environ.get("REDDIT_CLIENT_KEY"),
            client_secret=os.environ.get("REDDIT_CLIENT_SECRET")
        )
        self.assertIsNotNone(oauth_token["access_token"])

        logging.info("Got an oauth token")

    def test_get_news_flair(self):
        """Tests that we are retriving posts with a news flair

            Parameters
            ----------


            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test_get_news_flair")
        from scripts.reddit_ratings import get_oauth_token
        from scripts.reddit_ratings import get_news_flair

        '''
            Getting an Oauth token and testing for
            a specific fullname which is a unique
            identifier for a given reddit api object
            which ensures the same post will be returned
            each time
        '''
        oauth_token = get_oauth_token(
            client_key=os.environ.get("REDDIT_CLIENT_KEY"),
            client_secret=os.environ.get("REDDIT_CLIENT_SECRET")
        )
        logging.info("got oauth token for /search api call")
        '''
            The fullname will anchor this search to
            ensure the api always returns the same news
            posts
        '''
        news_search = get_news_flair(
            access_token=oauth_token["access_token"],
            posts_to_return=7,
            fullname_after="t3_dm3brn"
        )

        '''
            testing last reddit post in the
            list
        '''
        self.assertEqual(
            news_search["data"]["children"][6]["data"]["created_utc"],
            1570559167.0
        )
        '''
            Testing there is 7 posts returned
        '''
        self.assertEqual(
            len(news_search["data"]["children"]),
            7
        )
        logging.info("Validated the last post returned")
        '''
            Unique id of the first post returned
        '''
        self.assertEqual(
            news_search["data"]["children"][0]["data"]["name"],
            "t3_dlyuen"
        )
        logging.info("Validated get_news_flair function")

    def test_get_ratings_post(self):
        """Tests that only reddit ratings news posts are returned

            Parameters
            ----------


            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test_get_news_flair")
        from scripts.reddit_ratings import get_ratings_post
        '''
            loading a mock reddit api response to
            test if we are returning the correct number of
            ratings related posts
        '''
        with open("util/reddit_search_response.json") as static_response:
            mock_response = json.load(static_response)
            logging.info("Loaded mock reddit api response")
            ratings_post_list = get_ratings_post(mock_response)
        '''
            Elements of the ["data"]["children"]
            list that are ratings posts
        '''
        self.assertEqual(ratings_post_list,
            [0, 4, 13, 17, 19, 20, 22, 23])
        logging.info("All ratings post in reddit search response")

    def test_handle_table_header(self,
        mock_rating_table=REDDIT_RATING_TABLE_2019):
        """Tests columns are retrieved from html table header

            Parameters
            ----------
            mock_rating_table : str
                Example of an html table returned by the
                reddit api

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test of oath key")
        from scripts.reddit_ratings import handle_table_header

        '''
            Creating BeautifulSoup object from
            a test reddit html table post
            and validating the handle_table_header
            function returns a list of column names
        '''
        bs_obj = BeautifulSoup(mock_rating_table, "html.parser")
        header_columns = handle_table_header(bs_obj)

        self.assertEqual(header_columns,
            [
                "Time", "Show", "Viewers (000)",
                "18-49 Rating", "18-49 Views (000)"
            ]
        )
        logging.info("validated header columns returned from rest api")

    def test_handle_table_body(self,
        mock_rating_table=REDDIT_RATING_TABLE_2019):
        """Tests dict from html body handler

            Parameters
            ----------
            mock_rating_table : str
                Example of an html table returned by the
                reddit api

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test of oath key")
        from scripts.reddit_ratings import handle_table_body

        '''
            Creating BeautifulSoup object from
            a test reddit html table post
            and validating the handle_table_body
            function returns a list of ratings
        '''
        bs_obj = BeautifulSoup(mock_rating_table, "html.parser")
        '''
            Stub of header columns to pass to
            handle_table_body
        '''
        header_columns = [
            "Time", "Show", "Viewers (000)",
            "18-49 Rating", "18-49 Views (000)"
        ]
        saturday_ratings = handle_table_body(
            bs_obj=bs_obj,
            header_columns=header_columns)

        self.assertEqual(
            saturday_ratings[0]["Time"],
            "11:00"
        )
        self.assertEqual(
            saturday_ratings[7]["18-49 Rating"],
            "0.12"
        )
        self.assertEqual(
            saturday_ratings[9]["Viewers (000)"],
            "282"
        )

        logging.info("validated list of table_body")


    def test_handle_table_clean(self,
        mock_rating_table=REDDIT_RATING_TABLE_2020):
        """Tests cleaning of ratings data

            Parameters
            ----------
            mock_rating_table : str
                Example of an html table returned by the
                reddit api

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test of handle_table_clean")
        from scripts.reddit_ratings import handle_table_clean
        clean_saturday_ratings = handle_table_clean(mock_rating_table,
            rating_call_counter=0,
            ratings_title="Toonami Ratings for November 2nd, 2019"
        )

        '''
            Using date format that aligns with
            historical ratings
        '''
        self.assertEqual(
            clean_saturday_ratings[0]["ratings_occurred_on"],
            "2019-11-02"

        )
        self.assertEqual(clean_saturday_ratings[2]["Viewers (000)"],
            "453"
        )
        self.assertEqual(
            len(clean_saturday_ratings), 7
        )
        '''
            Checking the value of the date parsed from the
            title for different variations

            ex: 1st, 2nd, 3rd, 5th, etc.
        '''
        clean_saturday_st = handle_table_clean(mock_rating_table,
            rating_call_counter=0,
            ratings_title="Toonami Ratings for December 21st, 2019"
        )
        '''
            Using date format that aligns with
            historical ratings
        '''
        self.assertEqual(
            clean_saturday_st[0]["ratings_occurred_on"],
            "2019-12-21"
        )

        clean_saturday_th = handle_table_clean(mock_rating_table,
            rating_call_counter=0,
            ratings_title="Toonami Ratings for January 18th, 2020"
        )
        '''
            Using date format that aligns with
            historical ratings
        '''
        self.assertEqual(
            clean_saturday_th[0]["ratings_occurred_on"],
            "2020-01-18"
        )

    @patch("scripts.reddit_ratings.get_news_flair")
    def test_ratings_iteration(self, news_flair_patch):
        """Tests that we can iterate over most recent posts

            Parameters
            ----------
            news_flair_patch : unittest.mock.MagicMock
                Mock object used to test how often
                get_news_flair is called

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test_ratings_iteration")
        from scripts.reddit_ratings import ratings_iteration
        ratings_iteration()
        '''
            Testing that the get_news_flair
            meaning we are only looking for the most recent ratings
        '''
        self.assertEqual(news_flair_patch.call_count,
            1
        )
        logging.info("get_news_flair only called for most recent ratings")

if __name__ == "__main__":
    unittest.main()
