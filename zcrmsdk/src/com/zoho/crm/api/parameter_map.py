try:
    from zcrmsdk.src.com.zoho.crm.api.util.header_param_validator import HeaderParamValidator
    from zcrmsdk.src.com.zoho.crm.api.param import Param
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
except Exception:
    from .util import HeaderParamValidator
    from .param import Param
    from ..api.exception import SDKException
    from ..api.util import Constants


class ParameterMap(object):

    """
    This class represents the HTTP parameter name and value.
    """

    def __init__(self):
        """Creates an instance of ParameterMap Class"""

        self.request_parameters = dict()

    def add(self, param, value):

        """
        The method to add parameter name and value.

        Parameters:
            param (Param): A Param class instance.
            value (object): An object containing the parameter value.
        """

        if param is None:
            raise SDKException(Constants.PARAMETER_NONE_ERROR, Constants.PARAM_INSTANCE_NONE_ERROR)

        param_name = param.name
        
        if param_name is None:
            raise SDKException(Constants.PARAM_NAME_NONE_ERROR, Constants.PARAM_NAME_NONE_ERROR_MESSAGE)

        if value is None:
            raise SDKException(Constants.PARAMETER_NONE_ERROR, param_name + Constants.NONE_VALUE_ERROR_MESSAGE)

        class_name = param.class_name

        if class_name is not None:
            value = HeaderParamValidator().validate(param, value)

        if param_name not in self.request_parameters:
            self.request_parameters[param_name] = str(value)

        else:
            parameter_value = self.request_parameters[param_name]
            self.request_parameters[param_name] = parameter_value + ',' + str(value)
