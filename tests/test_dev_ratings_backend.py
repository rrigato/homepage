from bs4 import BeautifulSoup
import argparse
import boto3
import json
import logging
import os
import requests
import unittest

ENVIRON_DEF = "dev-backend"

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


class BackendTests(unittest.TestCase):
    """Tests backend AWS resources from templates/ratings_backend.yml

        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    """
    @classmethod
    def setUpClass(self):
        '''Unitest function that is run once for the class

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        get_logger()

    def test_dynamodb(self):
        '''Tests that the dynamodb table is present

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''

        """
            Creates dynamodb resource and
            puts an item in the table
        """
        dynamo_client = get_boto_clients(resource_name='dynamodb',
        region_name='us-east-1')

        table_configuration = dynamo_client.describe_table(
            cls.DYNAMO_TABLE_NAME
        )


    @unittest.skip("Skipping for now")
    def test_dynamodb(self):
        '''Tests that we can add an item to dynamodb

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''

        """
            Dict that will be put in the dynamodb table
        """
        test_dict = {"id":{"S":"1"}, "load_id":{"N":"100000"},
        "output_class":{"N":"1"}}


        """
            Creates dynamodb resource and
            puts an item in the table
        """
        dynamo_client = get_boto_clients(resource_name='dynamodb',
        region_name='us-east-1')


        put_response = dynamo_client.put_item(TableName=DYNAMO_TABLE_NAME,
        Item=test_dict)

        """
            Removes non-primary key fields and gets the item inserted
            from the put item command

            Tests the response against the original put_item
        """
        output_class = test_dict.pop('output_class')

        dummy_item = dynamo_client.get_item(TableName=DYNAMO_TABLE_NAME,
        Key=test_dict)

        logging.info("Dummy item returned: ")

        logging.info(dummy_item)

        self.assertEqual(
            int(dummy_item['Item']['output_class']['N']),
            int(output_class['N'])
            )


        """
            deletes the dummy item and tests to make sure it
            was successfully deleted
        """
        removed_item = dynamo_client.delete_item(TableName=DYNAMO_TABLE_NAME,
        Key=test_dict)

        """
            Making another get call after the item
            was deleted
        """
        self.assertEqual(
            removed_item['ResponseMetadata']['HTTPStatusCode'], 200
            )


if __name__ == "__main__":
    unittest.main()
