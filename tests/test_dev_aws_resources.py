from bs4 import BeautifulSoup
import argparse
import boto3
import json
import logging
import os
import requests
import unittest

ENVIRON_DEF = "dev"

HOMEPAGE_URL = "http://dev-static-site-homepage.s3-website-us-east-1.amazonaws.com/"
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
    """
        Adds the file name to the logs/ directory without
        the extension
    """
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
            Gets the arguements passed from the user

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        """
        get_logger()

    def test_home_page(self):
        """Tests that the aws resources necessary for the webpage are running

            Parameters
            ----------
                request_url : str
                    Url string to send the request to
            Returns
            -------

            Raises
            ------
        """
        logging.info("Testing if the website is alive")
        r = requests.get(
            HOMEPAGE_URL + "home.html"
        )
        self.assertEqual(r.status_code, 200)
        logging.info("The website is live")


    def test_homepage_image(self):
        """Tests that the homepage image loaded

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



        """
            Makes sure that https requests are routed
            correctly
        """
        for domain_name in REDIRECT_DOMAINS:
            logging.info("Domain name: ")
            logging.info(domain_name)

            homepage_request = requests.get(domain_name)
            """
                Tests that the request was successfull
            """
            self.assertEqual(
                homepage_request.status_code, 200
            )

            logging.info("Homepage call successful")


            """
                Getting a BeautifulSoup object to
                test content of the html page
            """
            bsObj = BeautifulSoup(homepage_request.text,
                "html.parser")

            logging.info("Homepage call was redirected")


            """
                Testing the text value of an html link
            """
            self.assertEqual(
                bsObj.find("a",
                {"href":"https://github.com/rrigato"}).text,
                "Check out my GitHub account"
            )

            """
                Testing that we have 3 info boxes
            """
            self.assertEqual(
                len(bsObj.findAll("div", {"id":"info"})),
                3
            )

            logging.info("Validated the content of the homepage")

            """
                Request started as http
                This check ensures it ended up as
                https
            """
            self.assertEqual(
                homepage_request.url[0:5],
                "https"
            )
            logging.info("The request was upgraded to https")





if __name__ == "__main__":
    unittest.main()
