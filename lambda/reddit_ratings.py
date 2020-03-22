import logging
import os
import requests

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

def get_oauth_token():
    """Gets an Oath token from the reddit API

        Parameters
        ----------

        Returns
        -------
        oauth_response : dict
            Dictionary with the oauth_token and expires_in
            keys. Ex:
            {
                "access_token": "-CL6wD3y7Y3ea9se9d84oXeom5ak",
                "expires_in": 3600
            }

        Raises
        ------
    """

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


if __name__ == "__main__":
    main()
