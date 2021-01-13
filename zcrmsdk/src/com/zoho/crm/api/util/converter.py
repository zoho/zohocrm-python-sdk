try:
    from abc import ABC, abstractmethod
    import logging
    import sys
    import zlib
    import base64
    import re
    import os
    import importlib
    from zcrmsdk.src.com.zoho.crm.api.util.choice import Choice

except Exception:
    from abc import ABC, abstractmethod
    import logging
    import sys
    import zlib
    import base64
    import re
    import os
    import importlib
    from .choice import Choice


class Converter(ABC):
    """
    This abstract class is to construct API request and response.
    """

    logger = logging.getLogger('SDKLogger')

    def __init__(self, common_api_handler):

        """
        Creates a Converter class instance with the CommonAPIHandler class instance.
        :param common_api_handler: A CommonAPIHandler class instance.
        """

        self.common_api_handler = common_api_handler

    @abstractmethod
    def get_response(self, response, pack):

        """
        This abstract method to process the API response.
        :param response: A object containing the API response contents or response.
        :param pack: A str containing the expected method return type.
        :return: A object representing the POJO class instance.
        """

        pass

    @abstractmethod
    def form_request(self, request_instance, pack, instance_number, class_member_detail):

        """
        This abstract method to construct the API request.
        :param request_instance: A Object containing the POJO class instance.
        :param pack: A str containing the expected method return type.
        :param instance_number: An int containing the POJO class instance list number.
        :param class_member_detail : A dict representing the member details
        :return: A object representing the API request body object.
        """

        pass

    @abstractmethod
    def append_to_request(self, request_base, request_object):

        """
        This abstract method to construct the API request body.
        :param request_base: A HttpEntityEnclosingRequestBase class instance.
        :param request_object: A object containing the API request body object.
        """

        pass

    @abstractmethod
    def get_wrapped_response(self, response, pack):

        """
        This abstract method to process the API response.
        :param response: A object containing the HttpResponse class instance.
        :param pack: A str containing the expected method return type.
        :return: A object representing the POJO class instance.
        """
        pass

    def value_checker(self, class_name, member_name, key_details, value, unique_values_map, instance_number):

        """
        This method is to validate if the input values satisfy the constraints for the respective fields.
        :param class_name: A str containing the class name.
        :param member_name: A str containing the member name.
        :param key_details: A JSON object containing the key JSON details.
        :param value: A object containing the key value.
        :param unique_values_map: A list containing the construct objects.
        :param instance_number: An int containing the POJO class instance list number.
        :return: A bool representing the key value is expected pattern, unique, length, and values.
        """

        try:
            from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
            from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
            from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer

        except Exception:
            from ..exception import SDKException
            from .constants import Constants
            from ..initializer import Initializer

        details_jo = {}
        name = key_details[Constants.NAME]
        data_type = key_details[Constants.TYPE]
        check = True
        given_type = None
        expected_type = None

        if data_type in Constants.TYPE_VS_DATATYPE:
            if isinstance(value, list) and Constants.STRUCTURE_NAME in key_details:
                structure_name = key_details[Constants.STRUCTURE_NAME]
                index = 0
                path_split = str(structure_name).rpartition('.')
                imported_module = importlib.import_module(path_split[0])
                class_holder = getattr(imported_module, path_split[-1])

                for each_instance in value:
                    if not isinstance(each_instance, class_holder):
                        check = False
                        instance_number = index
                        data_type = Constants.LIST_KEY + '[' + structure_name + ']'
                        given_type = each_instance.__module__
                        break

                    index = index + 1
            else:
                check = False if not isinstance(value, Constants.TYPE_VS_DATATYPE.get(data_type)) else True
                data_type = Constants.TYPE_VS_DATATYPE.get(data_type).__name__
                given_type = type(value).__name__

        elif value is not None and data_type.lower() != Constants.OBJECT_KEY:
            path_split = str(data_type).rpartition('.')
            imported_module = importlib.import_module(path_split[0])
            class_holder = getattr(imported_module, path_split[-1])

            if not isinstance(value, class_holder):
                check = False
                given_type = type(value).__name__

        if not check:
            details_jo[Constants.FIELD] = name
            details_jo[Constants.CLASS] = class_name
            details_jo[Constants.ACCEPTED_TYPE] = data_type
            details_jo[Constants.GIVEN_TYPE] = given_type
            if instance_number is not None:
                details_jo[Constants.INDEX] = instance_number

            raise SDKException(code=Constants.TYPE_ERROR, details=details_jo)

        if Constants.VALUES in key_details and (Constants.PICKLIST not in key_details or (key_details[Constants.PICKLIST] and Initializer.get_initializer().sdk_config.get_pick_list_validation())):
            values_ja = key_details[Constants.VALUES]

            if isinstance(value, Choice):
                value = value.get_value()

            if value not in values_ja:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.ACCEPTED_VALUES] = values_ja
                if instance_number is not None:
                    details_jo[Constants.INDEX] = instance_number

                raise SDKException(code=Constants.UNACCEPTED_VALUES_ERROR, details=details_jo)

        if Constants.UNIQUE in key_details:
            if name not in unique_values_map:
                unique_values_map[name] = []

            values_array = unique_values_map[name]

            if value in values_array:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.FIRST_INDEX] = values_array.index(value) + 1
                details_jo[Constants.NEXT_INDEX] = instance_number

                raise SDKException(code=Constants.UNIQUE_KEY_ERROR, details=details_jo)

            else:
                unique_values_map[name].append(value)

        if Constants.MIN_LENGTH in key_details or Constants.MAX_LENGTH in key_details:
            count = len(str(value))

            if isinstance(value, list):
                count = len(value)

            if Constants.MAX_LENGTH in key_details and count > key_details[Constants.MAX_LENGTH]:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.GIVEN_LENGTH] = count
                details_jo[Constants.MAXIMUM_LENGTH] = key_details[Constants.MAX_LENGTH]

                raise SDKException(code=Constants.MAXIMUM_LENGTH_ERROR, details=details_jo)

            if Constants.MIN_LENGTH in key_details and count < key_details[Constants.MIN_LENGTH]:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.GIVEN_LENGTH] = count
                details_jo[Constants.MINIMUM_LENGTH] = key_details[Constants.MIN_LENGTH]

                raise SDKException(code=Constants.MINIMUM_LENGTH_ERROR, details=details_jo)

        if Constants.REGEX in key_details:
            if re.search(value, key_details[Constants.REGEX]) is None:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.INSTANCE_NUMBER] = instance_number

                raise SDKException(code=Constants.REGEX_MISMATCH_ERROR, details=details_jo)

        return True

    @classmethod
    def get_encoded_file_name(cls):

        """
        The method to get the module field JSON details file name.
        :return: A str representing the module field JSON details file name.
        """

        try:
            from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        file_name = Initializer.get_initializer().user.email
        file_name = file_name.split("@", 1)[0] + Initializer.get_initializer().environment.url
        input_bytes = file_name.encode("UTF-8")
        encoded_string = base64.b64encode(input_bytes)
        encoded_string = str(encoded_string.decode("UTF-8"))
        return encoded_string + '.json'
