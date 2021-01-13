import threading
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.request_proxy import RequestProxy
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter, EUDataCenter
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType
from zcrmsdk.src.com.zoho.crm.api.record import *
from zcrmsdk.src.com.zoho.crm.api.org import *


class MultiThread(threading.Thread):

    def __init__(self, environment, token, user, module_api_name, sdk_config, proxy=None):
        super().__init__()
        self.environment = environment
        self.token = token
        self.user = user
        self.module_api_name = module_api_name
        self.sdk_config = sdk_config
        self.proxy = proxy

    def run(self):
        try:
            Initializer.switch_user(self.user, self.environment, self.token, self.sdk_config, self.proxy)

            print('Getting records for User: ' + Initializer.get_initializer().user.email)

            response = RecordOperations().get_records(self.module_api_name)

            if response is not None:

                # Get the status code from response
                print('Status Code: ' + str(response.get_status_code()))

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                # Get object from response
                response_object = response.get_object()

                if response_object is not None:

                    # Check if expected ResponseWrapper instance is received.
                    if isinstance(response_object, ResponseWrapper):
                        # Get the list of obtained Record instances
                        record_list = response_object.get_data()

                        for record in record_list:
                            for key, value in record.get_key_values().items():
                                print(key + " : " + str(value))

                    # Check if the request returned an exception
                    elif isinstance(response_object, APIException):
                        # Get the Status
                        print("Status: " + response_object.get_status().get_value())

                        # Get the Code
                        print("Code: " + response_object.get_code().get_value())

                        print("Details")

                        # Get the details dict
                        details = response_object.get_details()

                        for key, value in details.items():
                            print(key + ' : ' + str(value))

                        # Get the Message
                        print("Message: " + response_object.get_message().get_value())

        except Exception as e:
            print(e)


    @staticmethod
    def call():
        log_instance = Logger.get_instance(level=Logger.Levels.INFO, file_path="/Users/user_name/Documents/python_sdk_log.log")

        user1 = UserSignature(email="abc@zoho.com")

        token1 = OAuthToken(client_id="clientId1", client_secret="clientSecret1", token="REFRESH/ GRANT Token", token_type=TokenType.REFRESH / TokenType.GRANT)

        environment = USDataCenter.PRODUCTION()

        sdk_config_1 = SDKConfig(auto_refresh_fields=False, pick_list_validation=True)

        store = DBStore()

        resource_path = '/Users/user_name/Documents/python-app'

        user1_module_api_name = 'Leads'

        user2_module_api_name = 'Contacts'

        user2 = UserSignature("xyz@zoho.com")

        token2 = OAuthToken(client_id="clientId2", client_secret="clientSecret2", token="REFRESH/ GRANT Token", token_type=TokenType.REFRESH / TokenType.GRANT)

        proxy_user2 = RequestProxy('host', 8080)

        sdk_config_2 = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        Initializer.initialize(user1, environment, token1, store, sdk_config_1, resource_path, log_instance)

        t1 = MultiThread(environment, token1, user1, user1_module_api_name, sdk_config_1)
        t2 = MultiThread(environment, token2, user2, user2_module_api_name, sdk_config_2, proxy_user2)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


MultiThread.call()

