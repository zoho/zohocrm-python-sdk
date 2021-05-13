import datetime


class Constants(object):

    """
    This class uses the SDK constants name reference.
    """

    DATA_TYPE_ERROR = "DATA TYPE ERROR"

    ERROR = "error"

    REQUEST_METHOD_GET = "GET"

    REQUEST_METHOD_POST = "POST"

    REQUEST_METHOD_PUT = "PUT"

    REQUEST_METHOD_DELETE = "DELETE"

    REQUEST_METHOD_PATCH = 'PATCH'

    OAUTH_HEADER_PREFIX = "Zoho-oauthtoken "

    AUTHORIZATION = "Authorization"

    API_NAME = "api_name"

    INVALID_ID_MSG = "The given id seems to be invalid."

    API_MAX_RECORDS_MSG = "Cannot process more than 100 records at a time."

    INVALID_DATA = "INVALID_DATA"

    CODE_SUCCESS = "SUCCESS"

    STATUS_SUCCESS = "success"

    STATUS_ERROR = "error"

    GRANT_TYPE = "grant_type"

    GRANT_TYPE_AUTH_CODE = "authorization_code"

    ACCESS_TOKEN = "access_token"

    EXPIRES_IN = "expires_in"

    EXPIRES_IN_SEC = "expires_in_sec"

    REFRESH_TOKEN = "refresh_token"

    CLIENT_ID = "client_id"

    CLIENT_SECRET = "client_secret"

    REDIRECT_URL = "redirect_uri"

    TYPE_VS_DATATYPE = {
        "String": str,
        "List": list,
        "Integer": int,
        "HashMap": dict,
        "Map": dict,
        "Long": int,
        "Double": float,
        "Float": float,
        "DateTime": datetime.datetime,
        "Date": datetime.date,
        "Boolean": bool
    }

    OBJECT_KEY = "object"

    GIVEN_LENGTH = "given-length"

    ZOHO_SDK = "X-ZOHO-SDK"

    SDK_VERSION = "3.1.0"

    CONTENT_DISPOSITION = "Content-Disposition"

    TOKEN_ERROR = "TOKEN ERROR"

    SAVE_TOKEN_ERROR = "Exception in saving tokens"

    INVALID_CLIENT_ERROR = "INVALID CLIENT ERROR"

    ERROR_KEY = 'error'

    GET_TOKEN_ERROR = "Exception in getting access token"

    MYSQL_HOST = "localhost"

    MYSQL_DATABASE_NAME = "zohooauth"

    MYSQL_USER_NAME = "root"

    MYSQL_PORT_NUMBER = "3306"

    GET_TOKEN_DB_ERROR = "Exception in getToken - DBStore"

    TOKEN_STORE = "TOKEN_STORE"

    DELETE_TOKEN_DB_ERROR = "Exception in delete_token - DBStore"

    SAVE_TOKEN_DB_ERROR = "Exception in save_token - DBStore"

    USER_MAIL = "user_mail"

    GRANT_TOKEN = "grant_token"

    EXPIRY_TIME = "expiry_time"

    GET_TOKEN_FILE_ERROR = "Exception in get_token - FileStore"

    SAVE_TOKEN_FILE_ERROR = "Exception in save_token - FileStore"

    DELETE_TOKEN_FILE_ERROR = "Exception in delete_token - FileStore"

    TYPE = "type"

    STREAM_WRAPPER_CLASS_PATH = 'zcrmsdk.src.com.zoho.crm.api.util.StreamWrapper'

    FIELD = "field"

    NAME = "name"

    INDEX = "index"

    CLASS = "class"

    ACCEPTED_TYPE = "accepted_type"

    GIVEN_TYPE = "given_type"

    TYPE_ERROR = "TYPE ERROR"

    VALUES = "values"

    ACCEPTED_VALUES = "accepted_values"

    UNACCEPTED_VALUES_ERROR = "UNACCEPTED VALUES ERROR"

    MIN_LENGTH = "min-length"

    MINIMUM_LENGTH = "minimum-length"

    MINIMUM_LENGTH_ERROR = "MINIMUM LENGTH ERROR"

    UNIQUE = "unique"

    FIRST_INDEX = "first-index"

    NEXT_INDEX = "next-index"

    UNIQUE_KEY_ERROR = "UNIQUE KEY ERROR"

    MAX_LENGTH = "max-length"

    MAXIMUM_LENGTH = "maximum-length"

    MAXIMUM_LENGTH_ERROR = "MAXIMUM LENGTH ERROR"

    REGEX = "regex"

    INSTANCE_NUMBER = "instance-number"

    REGEX_MISMATCH_ERROR = "REGEX MISMATCH ERROR"

    READ_ONLY = "read-only"

    IS_KEY_MODIFIED = 'is_key_modified'

    REQUIRED = "required"

    REQUIRED_IN_UPDATE = "required_in_update"

    PRIMARY = "primary"

    MANDATORY_VALUE_ERROR = "MANDATORY VALUE ERROR"

    MANDATORY_VALUE_NULL_ERROR = "MANDATORY VALUE NULL ERROR"

    MANDATORY_KEY_ERROR = "Value missing or None for mandatory key(s): "

    MANDATORY_KEY_NULL_ERROR = "Null Value for mandatory key : "

    SET_KEY_MODIFIED = "set_key_modified"

    LIST_NAMESPACE = "List"

    MAP_NAMESPACE = "Map"

    HASH_MAP = "HashMap"

    STRUCTURE_NAME = "structure_name"

    KEYS = "keys"

    INTERFACE = "interface"

    RECORD_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.Record"

    RECORD_TYPE = "zcrmsdk.src.com.zoho.crm.api.record.record.Record"

    INVENTORY_LINE_ITEMS = "zcrmsdk.src.com.zoho.crm.api.record.InventoryLineItems"

    PRICINGDETAILS = "zcrmsdk.src.com.zoho.crm.api.record.PricingDetails"

    COMMENT_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.Comment"

    FIELD_FILE_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.FileDetails"

    REMINDAT_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.RemindAt"

    CONSENT_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.Consent"

    LINE_TAX_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.LineTax"

    REMINDER_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.Reminder"

    ATTACHMENTS_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.attachments.Attachment"

    RECURRING_ACTIVITY_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.record.RecurringActivity"

    PARTICIPANTS = "zcrmsdk.src.com.zoho.crm.api.record.Participants"

    PACKAGE_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api."

    USER_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.users.User"

    MODULE_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.modules.Module"

    LAYOUT_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.layouts.Layout"

    CHOICE_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.util.Choice"

    KEY_VALUES = "key_values"

    RECORD_CLASS_NAME = "Record"

    KEY_MODIFIED = "key_modified"

    COMMENTS = "Comments"

    CLASSES = "classes"

    LOGFILE_NAME = "sdk_logs.log"

    USER = "user"

    EXPECTED_TYPE = "expected-type"

    INITIALIZATION_ERROR = "INITIALIZATION ERROR"

    ENVIRONMENT = "environment"

    STORE = "store"

    TOKEN = "token"

    SDK_CONFIG = "sdk_config"

    USER_PROXY = "proxy"

    JSON_DETAILS_FILE_PATH = 'json_details.json'

    EMAIL = "email"

    USER_SIGNATURE_ERROR = "USERSIGNATURE ERROR";

    USER_INITIALIZATION_ERROR = "Error during User Initialization"

    EMAIL_REGEX = '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$'

    STRING = "String"

    TOKEN_TYPE = "token_type"

    GRANT = "GRANT"

    REFRESH = "REFRESH"

    CONTENT_TYPE = 'Content-Type'

    STRING_NAMESPACE = 'String'

    BOOLEAN_NAMESPACE = 'Boolean'

    INTEGER_NAMESPACE = 'Integer'

    LONG_NAMESPACE = 'String'

    DOUBLE_NAMESPACE = 'Float'

    DATE_NAMESPACE = 'Date'

    DATETIME_NAMESPACE = 'DateTime'

    FILE_NAMESPACE = "zcrmsdk.src.com.zoho.crm.api.util.StreamWrapper"

    KEYS_TO_SKIP = ['Created_Time', 'Modified_Time', 'Created_By', 'Modified_By', 'Tag']

    PRODUCT_DETAILS = "Product_Details"

    PRICING_DETAILS = "Pricing_Details"

    PARTICIPANT_API_NAME = "Participants"

    INVENTORY_MODULES = ['invoices', 'sales_orders', 'purchase_orders', 'quotes']

    PRICE_BOOKS = "price_books"

    EVENTS = "events"

    CALLS = "calls"

    CALL_DURATION = "call_duration"

    SOLUTIONS = "solutions"

    CASES = "cases"

    ACTIVITIES = "activities"

    LAYOUT = "Layout"

    SUBFORM = "subform"

    LOOKUP = "lookup"

    SE_MODULE = "se_module"

    MODULEDETAILS = 'moduleDetails'

    MODULEPACKAGENAME = "modulePackageName"

    UNDERSCORE = "_"

    RELATED_LISTS = "Related_Lists"

    FIELD_DETAILS_DIRECTORY = "resources"

    NO_CONTENT_STATUS_CODE = 204

    NOT_MODIFIED_STATUS_CODE = 304

    HREF = "href"

    API_EXCEPTION = "API_EXCEPTION"

    FIELDS_LAST_MODIFIED_TIME = "FIELDS-LAST-MODIFIED-TIME"

    LINE_TAX = "$line_tax"

    CANT_DISCLOSE = " ## can't disclose ## "

    URL = "URL"

    HEADERS = "HEADERS"

    PARAMS = "PARAMS"

    INITIALIZATION_SUCCESSFUL = "Initialization successful "

    INITIALIZATION_SWITCHED = "Initialization switched "

    IN_ENVIRONMENT = " in Environment : "

    FOR_EMAIL_ID = "for Email Id : "

    REFRESH_TOKEN_MESSAGE = "Access Token has expired. Hence refreshing."

    RESOURCE_PATH_ERROR = "EMPTY_RESOURCE_PATH"

    RESOURCE_PATH_ERROR_MESSAGE = "Resource Path MUST NOT be None/empty."

    SET_TO_CONTENT_TYPE = ["/crm/bulk/v2/read", "/crm/bulk/v2/write"]

    CONTENT_TYPE_HEADER = "Content-Type"

    LIST_KEY = "List"

    ATTACHMENT_ID = "attachment_id"

    FILE_ID = "file_id"

    DELETE_FIELD_FILE_ERROR = "Exception in deleting Current User Fields file : "

    DELETE_FIELD_FILES_ERROR = "Exception in deleting all Fields files : "

    DELETE_MODULE_FROM_FIELDFILE_ERROR = "Exception in deleting module from Fields file : "

    FILE_BODY_WRAPPER = 'FileBodyWrapper'

    EXCEPTION_IS_KEY_MODIFIED = "Exception in calling is_key_modified : "

    EXCEPTION_SET_KEY_MODIFIED = "Exception in calling set_key_modified : "

    SET_API_URL_EXCEPTION = "Exception in setting API URL : "

    AUTHENTICATION_EXCEPTION = "Exception in authenticating current request : "

    FORM_REQUEST_EXCEPTION = "Exception in forming request body : "

    API_CALL_EXCEPTION = "Exception in current API call execution : "

    HTTP = "http"

    HTTPS = "https"

    CONTENT_API_URL = "content.zohoapis.com"

    EXCEPTION = "Exception"

    MODULE = "module"

    REQUEST_CATEGORY_READ = "READ"

    REQUEST_CATEGORY_CREATE = "CREATE"

    REQUEST_CATEGORY_UPDATE = "UPDATE"

    ID = "id"

    CODE = "code"

    STATUS = "status"

    MESSAGE = "message"

    INVALID_URL_ERROR = "Invalid URL Error"

    REQUEST_CATEGORY_ACTION = "ACTION"

    SKIP_MANDATORY = "skip_mandatory"

    FORMULA = "formula"

    PICKLIST = "picklist"

    ACCOUNTS = "accounts"

    PRIMARY_KEY_ERROR = "Value missing or None for required key(s) : "

    REFRESH_SINGLE_MODULE_FIELDS_ERROR = "Exception in refreshing fields of module : "

    REFRESH_ALL_MODULE_FIELDS_ERROR = "Exception in refreshing fields of all modules : "

    GET_TOKENS_DB_ERROR = "Exception in get_tokens - DBStore"

    DELETE_TOKENS_DB_ERROR = "Exception in delete_tokens - DBStore"

    GET_TOKENS_FILE_ERROR = "Exception in get_tokens - FileStore"

    DELETE_TOKENS_FILE_ERROR = "Exception in delete_tokens - FileStore"

    SDK_UNINITIALIZATION_ERROR = "SDK UNINITIALIZED ERROR"

    SDK_UNINITIALIZATION_MESSAGE = "SDK is UnInitialized"

    INITIALIZATION_EXCEPTION = "Exception in initialization"

    SWITCH_USER_EXCEPTION = "Exception in switching user"

    AUTO_REFRESH_FIELDS_ERROR_MESSAGE = "auto_refresh_fields MUST NOT be None."

    HEADER_NONE_ERROR = "NONE HEADER ERROR"

    HEADER_INSTANCE_NONE_ERROR = "Header Instance MUST NOT be None"

    PARAM_INSTANCE_NONE_ERROR = "Param Instance MUST NOT be None"

    HEADER_NAME_NONE_ERROR = "NONE HEADER NAME ERROR"

    HEADER_NAME_NULL_ERROR_MESSAGE = "Header Name MUST NOT be null"

    NONE_VALUE_ERROR_MESSAGE = " MUST NOT be None"

    PARAMETER_NONE_ERROR = "NONE PARAMETER ERROR"

    PARAM_NAME_NONE_ERROR = "NONE PARAM NAME ERROR"

    PARAM_NAME_NONE_ERROR_MESSAGE = "Param Name MUST NOT be None"

    SWITCH_USER_ERROR = "SWITCH USER ERROR"

    USER_PROXY_ERROR = "USERPROXY ERROR"

    HOST_ERROR_MESSAGE = "Host MUST NOT be None"

    PORT_ERROR_MESSAGE = "Port MUST NOT be None"

    USER_ERROR_MESSAGE = "User MUST NOT be None/empty"

    UNSUPPORTED_IN_API = "API UNSUPPORTED OPERATION"

    UNSUPPORTED_IN_API_MESSAGE = " Operation is not supported by API"

    NULL_VALUE = "null"

    NOTES = "notes"

    ATTACHMENTS = "$attachments"

    PROXY_SETTINGS = "Proxy settings - "

    PROXY_HOST = "Host: "

    PROXY_PORT = "Port: "

    PROXY_USER = "User: "

    JSON_FILE_EXTENSION = ".json"

    FILE_ERROR = "file_error"

    FILE_DOES_NOT_EXISTS = "file does not exists"

    CONSENT_LOOKUP = "consent_lookup"

    USER_MAIL_NULL_ERROR = "USER MAIL NONE ERROR"

    USER_MAIL_NULL_ERROR_MESSAGE = "User Mail MUST NOT be None. Set value to user_mail."

    JSON_DETAILS_ERROR = "ERROR IN READING JSONDETAILS FILE"
