from bs4 import BeautifulSoup
from unittest.mock import MagicMock
from unittest.mock import patch
import json
import logging
import os
import requests
import unittest

'''
    Defaults to $CODEBUILD_SRC_DIR
    which is the working directory where the
    code repository is built in codebuild
'''
WORKING_DIRECTORY = os.getcwd()

def get_logger():
    """Returns a boto cloudformation describe_stacks api call
        Parameters
        ----------
        stack_name: str
            Name of the stack

        Returns
        -------
        cf_response : dict
                Dictionary output of the describe_stacks api call

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

    @unittest.skip("Skipping for now")
    def test_get_oath_key(self):
        """Tests oath key returned from reddit api

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        logging.info("Beginning test of oath key")
        oath_key = get_oauth_key()
        self.assertEqual(len(oath_key), 128)


if __name__ == "__main__":
    unittest.main()
