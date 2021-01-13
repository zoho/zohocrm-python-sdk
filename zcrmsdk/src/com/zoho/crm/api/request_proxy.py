try:
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
except Exception:
    from .exception import SDKException
    from .util import Constants


class RequestProxy(object):
    def __init__(self, host, port, user=None, password=None):

        """
        Creates a RequestProxy class instance with the specified parameters.

        Parameters:
            host(str): A String containing the hostname or address of the proxy server
            port(int): An Integer containing The port number of the proxy server
            user(str): A String containing the user name of the proxy server
            password(str) : A String containing the password of the proxy server. Default value is an empty string

        Raises:
            SDKException
        """

        if host is None:
            raise SDKException(Constants.USER_PROXY_ERROR, Constants.HOST_ERROR_MESSAGE)

        if port is None:
            raise SDKException(Constants.USER_PROXY_ERROR, Constants.PORT_ERROR_MESSAGE)

        self.host = host
        self.port = port
        self.user = user
        self.password = "" if password is None else password
