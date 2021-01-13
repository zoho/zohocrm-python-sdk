
try:
    import logging
    import os
    import json
    import threading
    from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
    from zcrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.dc.data_center import DataCenter
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.api.authenticator.token import Token
    from zcrmsdk.src.com.zoho.api.logger import Logger, SDKLogger
    from zcrmsdk.src.com.zoho.crm.api.request_proxy import RequestProxy
    from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig

except Exception:
    import logging
    import os
    import json
    import threading
    from ..api.user_signature import UserSignature
    from ...api.authenticator.store.token_store import TokenStore
    from ..api.exception import SDKException
    from ..api.dc.data_center import DataCenter
    from ..api.util.constants import Constants
    from ...api.authenticator.token import Token
    from ...api.logger import Logger, SDKLogger
    from .request_proxy import RequestProxy
    from .sdk_config import SDKConfig


class Initializer(object):

    """
    The class to initialize Zoho CRM SDK.
    """

    def __init__(self):
        self.environment = None
        self.user = None
        self.store = None
        self.token = None
        self.sdk_config = None
        self.request_proxy = None
        self.resource_path = None

    json_details = None
    initializer = None
    LOCAL = threading.local()
    LOCAL.init = None

    @staticmethod
    def initialize(user, environment, token, store, sdk_config, resource_path, logger=None, proxy=None):

        """
        The method to initialize the SDK.

        Parameters:
            user (UserSignature) : A UserSignature class instance represents the CRM user
            environment (DataCenter.Environment) : An Environment class instance containing the CRM API base URL and Accounts URL.
            token (Token) : A Token class instance containing the OAuth client application information.
            store (TokenStore) : A TokenStore class instance containing the token store information.
            sdk_config (SDKConfig) : A SDKConfig class instance containing the configuration.
            resource_path (str) : A String containing the absolute directory path to store user specific JSON files containing module fields information.
            logger (Logger): A Logger class instance containing the log file path and Logger type.
            proxy (RequestProxy) : A RequestProxy class instance containing the proxy properties of the user.
        """

        try:
            if not isinstance(user, UserSignature):
                error = {Constants.FIELD: Constants.USER, Constants.EXPECTED_TYPE: UserSignature.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.INITIALIZATION_EXCEPTION, details=error)

            if not isinstance(environment, DataCenter.Environment):
                error = {Constants.FIELD: Constants.ENVIRONMENT,
                         Constants.EXPECTED_TYPE: DataCenter.Environment.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.INITIALIZATION_EXCEPTION, details=error)

            if not isinstance(token, Token):
                error = {Constants.FIELD: Constants.TOKEN, Constants.EXPECTED_TYPE: Token.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.INITIALIZATION_EXCEPTION, details=error)

            if not isinstance(store, TokenStore):
                error = {Constants.FIELD: Constants.STORE, Constants.EXPECTED_TYPE: TokenStore.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.INITIALIZATION_EXCEPTION, details=error)

            if not isinstance(sdk_config, SDKConfig):
                error = {Constants.FIELD: Constants.SDK_CONFIG, Constants.EXPECTED_TYPE: SDKConfig.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.INITIALIZATION_EXCEPTION, details=error)

            if resource_path is None or len(resource_path) == 0:
                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.RESOURCE_PATH_ERROR_MESSAGE)

            if proxy is not None and not isinstance(proxy, RequestProxy):
                error = {Constants.FIELD: Constants.USER_PROXY, Constants.EXPECTED_TYPE: RequestProxy.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.INITIALIZATION_EXCEPTION, details=error)

            if logger is not None:
                SDKLogger.initialize(logger)
            else:
                SDKLogger.initialize(Logger(Logger.Levels.INFO, os.path.join(os.getcwd(), Constants.LOGFILE_NAME)))

            try:
                json_details_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', Constants.JSON_DETAILS_FILE_PATH)

                with open(json_details_path, mode='r') as JSON:
                    Initializer.json_details = json.load(JSON)
            except Exception as e:
                raise SDKException(code=Constants.JSON_DETAILS_ERROR, cause=e)

            initializer = Initializer()

            initializer.environment = environment
            initializer.user = user
            initializer.token = token
            initializer.store = store
            initializer.sdk_config = sdk_config
            initializer.resource_path = resource_path
            initializer.request_proxy = proxy

            Initializer.initializer = initializer

            logging.getLogger('SDKLogger').info(Constants.INITIALIZATION_SUCCESSFUL + initializer.__str__())

        except SDKException as e:
            raise e

    def __str__(self):
        return Constants.FOR_EMAIL_ID + Initializer.get_initializer().user.email + Constants.IN_ENVIRONMENT + Initializer.get_initializer().environment.url + '.'

    @staticmethod
    def get_initializer():

        """
        The method to get Initializer class instance.

        Returns:
            Initializer : An instance of Initializer
        """

        if getattr(Initializer.LOCAL, 'init', None) is not None:
            return getattr(Initializer.LOCAL, 'init')

        return Initializer.initializer

    @staticmethod
    def get_json(file_path):
        with open(file_path, mode="r") as JSON:
            file_contents = json.load(JSON)
            JSON.close()

        return file_contents

    @staticmethod
    def switch_user(user, environment, token, sdk_config, proxy=None):

        """
        The method to switch the different user in SDK environment.

        Parameters:
            user (UserSignature) : A UserSignature class instance represents the CRM user
            environment (DataCenter.Environment) : An Environment class instance containing the CRM API base URL and Accounts URL.
            token (Token) : A Token class instance containing the OAuth client application information.
            sdk_config (SDKConfig) : A SDKConfig class instance containing the configuration.
            proxy (RequestProxy) : A RequestProxy class instance containing the proxy properties of the user.
        """

        if not isinstance(user, UserSignature):
            error = {Constants.FIELD: Constants.USER, Constants.EXPECTED_TYPE: UserSignature.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.SWITCH_USER_EXCEPTION, details=error)

        if not isinstance(environment, DataCenter.Environment):
            error = {Constants.FIELD: Constants.ENVIRONMENT,
                     Constants.EXPECTED_TYPE: DataCenter.Environment.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.SWITCH_USER_EXCEPTION, details=error)

        if not isinstance(token, Token):
            error = {Constants.FIELD: Constants.TOKEN, Constants.EXPECTED_TYPE: Token.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.SWITCH_USER_EXCEPTION, details=error)

        if not isinstance(sdk_config, SDKConfig):
            error = {Constants.FIELD: Constants.SDK_CONFIG, Constants.EXPECTED_TYPE: SDKConfig.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.SWITCH_USER_EXCEPTION, details=error)

        if proxy is not None and not isinstance(proxy, RequestProxy):
            error = {Constants.FIELD: Constants.USER_PROXY, Constants.EXPECTED_TYPE: RequestProxy.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.SWITCH_USER_EXCEPTION, details=error)

        initializer = Initializer()

        initializer.user = user
        initializer.environment = environment
        initializer.token = token
        initializer.sdk_config = sdk_config
        initializer.store = Initializer.initializer.store
        initializer.resource_path = Initializer.initializer.resource_path
        initializer.request_proxy = proxy

        Initializer.LOCAL.init = initializer

        logging.getLogger('SDKLogger').info(Constants.INITIALIZATION_SWITCHED + initializer.__str__())
