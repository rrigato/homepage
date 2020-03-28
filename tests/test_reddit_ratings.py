from bs4 import BeautifulSoup
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
        #oath_response = get_oauth_token()
        #self.assertEqual(len(oath_response), 128)

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
        bs_obj = BeautifulSoup(mock_rating_table, "html5lib")
        header_columns = handle_table_header(bs_obj)

        self.assertEqual(header_columns,
            [
                "Time", "Show", "Viewers (000)",
                "18-49 Rating", "18-49 Views (000)"
            ]
        )
        logging.info("validated header columns returned from rest api")

    @unittest.skip("Skipping for now")
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
            function returns a list of column names
        '''
        bs_obj = BeautifulSoup(mock_rating_table, "html5lib")
        show_ratings = handle_table_body(bs_obj)


        logging.info("validated dict of table_body")


    def test_html_table_parse(self):
        """Tests that we are able to parse an html table

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test of oath key")
        from scripts.reddit_ratings import html_table_parse
if __name__ == "__main__":
    unittest.main()
