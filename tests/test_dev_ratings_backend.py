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
    def setUpClass(cls):
        '''Unitest function that is run once for the class

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        cls.DYNAMO_TABLE_NAME = "toonami_ratings"
        cls.LAMBDA_FUNCTION_NAME = "toonami_ratings"
        cls.S3_CODE_BUCKET = "toonami_ratings"

    def test_dynamodb_config(self):
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
            TableName=self.DYNAMO_TABLE_NAME
        )

        self.assertEqual(
            table_configuration["Table"]["TableName"],
            self.DYNAMO_TABLE_NAME
        )

        '''
            Testing primary key, on demand billing type
            and that encryption is enabled on the dynamodb
            table

        self.assertEqual(
            table_configuration["Table"]["SSEDescription"]["Status"],
            [
                {
                    "AttributeName": "RATINGS_OCCURRED_ON",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "TIME",
                    "AttributeType": "S"
                }
            ]
        )
        '''

        self.assertEqual(
            table_configuration["Table"]["BillingModeSummary"]["BillingMode"],
            "PAY_PER_REQUEST"
        )

        self.assertEqual(
            table_configuration["Table"]["SSEDescription"]["Status"],
            "ENABLED"
        )

    @unittest.skip("Skipping for now")
    def test_lambda_config(self):
        '''Tests that the lambda function configuration

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
        lambda_client = get_boto_clients(resource_name='lambda',
        region_name='us-east-1')


        lambda_function_configuration = lambda_client.describe_table(
            TableName=self.LAMBDA_FUNCTION_NAME
        )


    @unittest.skip("Skipping for now")
    def test_s3_code_bucket(self):
        '''s3 bucket configuration that stores lambda code test

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''

        """
            gets s3 bucket information
        """
        s3_client = get_boto_clients(resource_name='s3',
        region_name='us-east-1')

        s3_lambda_code_configuration = s3_client.describe_table(
            TableName=self.S3_CODE_BUCKET
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
