from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore, FileStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType
from datetime import datetime

class SDKInitializer(object):

    @staticmethod
    def initialize_sdk():
        # Create an instance of Logger Class that takes two parameters
        # 1 -> Level of the log messages to be logged. Can be configured by typing Levels "." and choose any level from the list displayed.
        # 2 -> Absolute file path, where messages need to be logged.
        logger_instace = Logger.get_instance(level=Logger.Levels.INFO, file_path="/Users/user_name/Documents/python_sdk_log.log")

        # Create an UserSignature instance that takes user Email as parameter
        user = UserSignature(email="abc@zoho.com")

        """
        Create a Token instance that takes the following parameters
        1 -> OAuth client id.
        2 -> OAuth client secret.
        3 -> OAuth redirect URL.
        4 -> REFRESH/GRANT token.
        5 -> token type.
        """
        token = OAuthToken(client_id="clientId", client_secret="clientSecret", redirect_url="redirectURL", token="REFRESH/ GRANT Token", token_type=TokenType.REFRESH / TokenType.GRANT)

        # Configure the environment
        # which is of the pattern Domain.Environment
        # Available Domains: USDataCenter, EUDataCenter, INDataCenter, CNDataCenter, AUDataCenter
        # Available Environments: PRODUCTION(), DEVELOPER(), SANDBOX()
        environment = USDataCenter.PRODUCTION()

        # Create an instance of TokenStore
        """
        Create an instance of TokenStore
        1 -> Absolute file path of the file to persist tokens
        """
        store = FileStore(file_path='/Users/username/Documents/python_sdk_tokens.txt')

        """
        Create an instance of SDKConfig
        """
        config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        """
        The path containing the absolute directory path (in the key resource_path) to store user-specific files containing information about fields in modules. 
        """
        resource_path = '/Users/user_name/Documents/python-app'

        """
        Call the static initialize method of Initializer class that takes the following arguments
         1 -> UserSignature instance
         2 -> Environment instance
         3 -> Token instance
         4 -> TokenStore instance
         5 -> SDKConfig instance
         6 -> resource_path
         7 -> Logger instance
        """
        Initializer.initialize(user, environment, token, store, config, resource_path, logger_instace)
