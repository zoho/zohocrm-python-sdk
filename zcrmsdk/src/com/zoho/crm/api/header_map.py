try:
    from zcrmsdk.src.com.zoho.crm.api.util.header_param_validator import HeaderParamValidator
    from zcrmsdk.src.com.zoho.crm.api.header import Header
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
except Exception:
    from .util import HeaderParamValidator
    from .header import Header
    from ..api.exception import SDKException
    from ..api.util import Constants


class HeaderMap(object):

    """
    This class represents the HTTP header name and value.
    """

    def __init__(self):
        """Creates an instance of HeaderMap Class"""

        self.request_headers = dict()

    def add(self, header, value):

        """
        The method to add the parameter name and value.

        Parameters:
            header (Header): A Header class instance.
            value (object): An object containing the header value.
        """

        if header is None:
            raise SDKException(Constants.HEADER_NONE_ERROR, Constants.HEADER_INSTANCE_NONE_ERROR)

        header_name = header.name

        if header_name is None:
            raise SDKException(Constants.HEADER_NAME_NONE_ERROR, Constants.HEADER_NAME_NULL_ERROR_MESSAGE)

        if value is None:
            raise SDKException(Constants.HEADER_NONE_ERROR, header_name + Constants.NONE_VALUE_ERROR_MESSAGE)

        class_name = header.class_name

        if class_name is not None:
            value = HeaderParamValidator().validate(header, value)

        if header_name not in self.request_headers:
            self.request_headers[header_name] = str(value)

        else:
            header_value = self.request_headers[header_name]
            self.request_headers[header_name] = header_value + ',' + str(value)
