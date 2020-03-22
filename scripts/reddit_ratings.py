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
    pass

def get_html_table_parse(reddit_post_html):
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
    pass


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

if __name__ == "__main__":
    main()
