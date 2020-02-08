from bs4 import BeautifulSoup
from unittest.mock import MagicMock
from unittest.mock import patch
import argparse
import boto3
import json
import logging
import os
import requests
import unittest

ENVIRON_DEF = "prod"

HOMEPAGE_URL = "https://ryanrigato.com"
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

def get_boto_clients(resource_name, region_name="us-east-1"):
    """Returns the boto client for various cloudformation resources
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
    """
    return(boto3.client(resource_name, region_name))

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
    def test_bucket_stack_exists(self,
        stack_name="dev-devdocs-webpage"):
        """Tests that the templates/static_website stack exists

            Parameters
            ----------
                stack_name : str
                    name of the stack we are checking
            Returns
            -------

            Raises
            ------
        """
        logging.info("Testing if the website bucket stack exists")


        webpage_stack = describe_stacks_response(
            stack_name=stack_name)

        self.assertEqual(
            webpage_stack["Outputs"][0]["OutputValue"],
            HOMEPAGE_URL
        )
        logging.info("Output url for webpage is correct")





    def test_standards_project(self, domain_url=HOMEPAGE_URL):
        """Tests that the /docs/v1/standards/standards.html is alive

            Parameters
            ----------
                domain_url : str
                    Url string to send the request to
            Returns
            -------

            Raises
            ------
        """
        logging.info("Testing if the standards webpage is alive")

        standards_test = (
            domain_url + "/docs/v1/standards/standards.html"
        )
        logging.info(standards_test)

        r = requests.get(standards_test)

        self.assertEqual(r.status_code, 200)
        logging.info("The standards page is live")


    def test_homepage_http(self):
        """Testing that webpage is live under http scheme

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        REDIRECT_DOMAINS = [
            "http://ryanrigato.com",
            "http://www.ryanrigato.com"
        ]
        logging.info("Testing if the http homepage is alive")



        '''
            Makes sure that http is redirected
            to more secure https
        '''
        for domain_name in REDIRECT_DOMAINS:
            logging.info("Domain name: ")
            logging.info(domain_name)

            homepage_request = requests.get(domain_name)
            '''
                Tests that the request was successfull
            '''
            self.assertEqual(
                homepage_request.status_code, 200
            )

            logging.info("Homepage call successful")
            '''
                Ensuring the original request got a 301
                redirect
                .history = list of request history
            '''
            self.assertEqual(
                homepage_request.history[0].status_code,
                301
            )

            '''
                Getting a BeautifulSoup object to
                test content of the html page
            '''
            bsObj = BeautifulSoup(homepage_request.text,
                "html.parser")

            logging.info("Homepage call was redirected")


            '''
                Testing the text value of an html link
            '''
            self.assertEqual(
                bsObj.find("a",
                {"href":"https://github.com/rrigato"}).text,
                "Check out my GitHub account"
            )

            '''
                Testing that we have 3 info boxes
            '''
            self.assertEqual(
                len(bsObj.findAll("div", {"id":"info"})),
                3
            )

            logging.info("Validated the content of the homepage")

            '''
                Request started as http
                This check ensures it ended up as
                https
            '''
            self.assertEqual(
                homepage_request.url[0:5],
                "https"
            )
            logging.info("The request was upgraded to https")

    def test_homepage_https(self):
        """Testing that webpage is live under https scheme

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        REDIRECT_DOMAINS = [
            "https://ryanrigato.com",
            "https://www.ryanrigato.com"
        ]
        logging.info("Testing if the https homepage is alive")



        '''
            Makes sure that https requests are routed
            correctly
        '''
        for domain_name in REDIRECT_DOMAINS:
            logging.info("Domain name: ")
            logging.info(domain_name)

            homepage_request = requests.get(domain_name)
            '''
                Tests that the request was successfull
            '''
            self.assertEqual(
                homepage_request.status_code, 200
            )

            logging.info("Homepage call successful")


            '''
                Getting a BeautifulSoup object to
                test content of the html page
            '''
            bsObj = BeautifulSoup(homepage_request.text,
                "html.parser")

            logging.info("Homepage call was redirected")


            '''
                Testing the text value of an html link
            '''
            self.assertEqual(
                bsObj.find("a",
                {"href":"https://github.com/rrigato"}).text,
                "Check out my GitHub account"
            )

            '''
                Testing that we have 3 info boxes
            '''
            self.assertEqual(
                len(bsObj.findAll("div", {"id":"info"})),
                3
            )

            logging.info("Validated the content of the homepage")

            '''
                Request started as http
                This check ensures it ended up as
                https
            '''
            self.assertEqual(
                homepage_request.url[0:5],
                "https"
            )
            logging.info("The request was upgraded to https")




if __name__ == "__main__":
    unittest.main()
