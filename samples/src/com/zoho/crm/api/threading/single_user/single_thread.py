from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.dc import INDataCenter, USDataCenter, EUDataCenter, CNDataCenter, AUDataCenter
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore, FileStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType
from zcrmsdk.src.com.zoho.crm.api.record import *


class SingleThread(object):

    @staticmethod
    def call():
        log_instance = Logger.get_instance(level=Logger.Levels.INFO, file_path="/Users/user_name/Documents/python_sdk_log.log")

        user = UserSignature(email="abc@zoho.com")

        token = OAuthToken(client_id="clientId", client_secret="clientSecret", token="REFRESH/ GRANT Token", token_type=TokenType.REFRESH / TokenType.GRANT)

        environment = USDataCenter.PRODUCTION()

        store = FileStore(file_path='/Users/username/Documents/python_sdk_tokens.txt')

        resource_path = '/Users/user_name/Documents/python-app'

        sdk_config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        Initializer.initialize(user, environment, token, store, sdk_config, resource_path, log_instance)

        module_1 = "Leads"

        module_2 = "Contacts"

        response_1 = RecordOperations().get_records(module_1)

        response_2 = RecordOperations().get_records(module_2)


SingleThread.call()
