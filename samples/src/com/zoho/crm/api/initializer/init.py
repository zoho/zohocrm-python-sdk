from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.crm.api.dc import INDataCenter, USDataCenter, EUDataCenter, CNDataCenter, AUDataCenter
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore, FileStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType


class SDKInitializer(object):

    @staticmethod
    def initialize():

        """
        Create an instance of Logger Class that takes two parameters
        1 -> Level of the log messages to be logged. Can be configured by typing Logger.Levels "." and choose any level from the list displayed.
        2 -> Absolute file path, where messages need to be logged.
        """
        logger = Logger.get_instance(level=Logger.Levels.INFO, file_path="/Users/user_name/Documents/python_sdk_log.log")

        # Create an UserSignature instance that takes user Email as parameter
        user = UserSignature(email="abc@zoho.com")

        """
        Configure the environment
        which is of the pattern Domain.Environment
        Available Domains: USDataCenter, EUDataCenter, INDataCenter, CNDataCenter, AUDataCenter
        Available Environments: PRODUCTION(), DEVELOPER(), SANDBOX()
        """
        environment = USDataCenter.PRODUCTION()

        """
        Create a Token instance that takes the following parameters
        1 -> OAuth client id.
        2 -> OAuth client secret.
        3 -> OAuth redirect URL.
        4 -> REFRESH/GRANT token.
        5 -> token type.
        """
        token = OAuthToken(client_id="clientId", client_secret="clientSecret", redirect_url="redirectURL", token="REFRESH/ GRANT Token", token_type=TokenType.REFRESH / TokenType.GRANT)

        """
        Create an instance of TokenStore
        1 -> Absolute file path of the file to persist tokens
        """
        store = FileStore(file_path='/Users/username/Documents/python_sdk_tokens.txt')

        """
        Create an instance of TokenStore
        1 -> DataBase host name. Default value "localhost"
        2 -> DataBase name. Default value "zohooauth"
        3 -> DataBase user name. Default value "root"
        4 -> DataBase password. Default value ""
        5 -> DataBase port number. Default value "3306"
        """
        store = DBStore()
        store = DBStore(host='host_name', database_name='database_name', user_name='user_name', password='password',
                        port_number='port_number')

        """
        A Boolean value for the key (auto_refresh_fields) to allow or prevent auto-refreshing of the modules' fields in the background.
        if True - all the modules' fields will be auto-refreshed in the background whenever there is any change.
        if False - the fields will not be auto-refreshed in the background. The user can manually delete the file(s) or the specific module's fields using methods from ModuleFieldsHandler
        """
        auto_refresh_fields = True

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
        5 -> Logger instance
        6 -> auto_refresh_fields
        7 -> resource_path
        """
        Initializer.initialize(user=user, environment=environment, token=token, store=store, logger=logger, auto_refresh_fields=auto_refresh_fields, resource_path=resource_path)


SDKInitializer.initialize()
