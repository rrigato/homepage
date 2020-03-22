from bs4 import BeautifulSoup
from unittest.mock import MagicMock
from unittest.mock import patch
from util.test_reddit_rating_config import REDDIT_RATING_TABLE_2019
import json
import logging
import os
import requests
import unittest

'''
Where the python script was executed from
'''
WORKING_DIRECTORY = os.getcwd()


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

class WebappLive(unittest.TestCase):
    """Tests that the aws resources necessary for the webpage are running

        Note that if any of the below unit tests fail,
        The python script will have a non-zero exit code

        This will cause any CodeBuild Builds to fail out

        Preventing the Code Pipeline from continuing to delivery

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
        os.sys.path.append(WORKING_DIRECTORY)

    def setUp(self):
        """Unitest function that is run once before each function
            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        os.chdir(WORKING_DIRECTORY)


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
        header_columns = handle_table_header(mock_rating_table)
        self.assertEqual(header_columns,
            [
                "Time", "Show", "Viewers (000)",
                "18-49 Rating", "18-49 Views (000)"
            ]
        )
        logging.info("validated header columns returned from rest api")

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
