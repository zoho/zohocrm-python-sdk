try:
    import os
    import re
    import json
    from zcrmsdk.src.com.zoho.crm.api.util.datatype_converter import DataTypeConverter
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants

except Exception:
    import os
    import re
    import json
    from .datatype_converter import DataTypeConverter
    from ..exception import SDKException
    from .constants import Constants


class HeaderParamValidator(object):

    """
    This class validates the Header and Parameter values with the type accepted by the CRM APIs.
    """

    def validate(self, header_param, value):
        name = header_param.name
        class_name = header_param.class_name
        json_details = self.get_json_details()
        json_class_name = self.get_file_name(class_name)
        type_detail = None

        if json_class_name in json_details:
            type_detail = self.get_key_json_details(name, json_details[json_class_name])

        if type_detail is not None:
            if not self.check_data_type(type_detail, value):
                param_or_header = 'PARAMETER' if json_class_name is not None and json_class_name.endswith('Param') else 'HEADER'
                error_details = {
                    param_or_header: name,
                    Constants.CLASS: json_class_name,
                    Constants.ACCEPTED_TYPE: Constants.TYPE_VS_DATATYPE[type_detail[Constants.TYPE]].__name__ if type_detail[Constants.TYPE] in Constants.TYPE_VS_DATATYPE else type_detail[Constants.TYPE]
                }
                raise SDKException(code=Constants.TYPE_ERROR, details=error_details)
            else:
                value = DataTypeConverter.post_convert(value, type_detail[Constants.TYPE])

        return value

    def check_data_type(self, key_detail, value):
        data_type = key_detail[Constants.TYPE]

        if data_type in Constants.TYPE_VS_DATATYPE:
            if not isinstance(value, Constants.TYPE_VS_DATATYPE[data_type]):
                return False

        return True

    def get_key_json_details(self, name, json_details):
        for key_name in json_details.keys():
            detail = json_details[key_name]

            if Constants.NAME in detail:
                if detail[Constants.NAME].lower() == name.lower():
                    return detail

    def get_file_name(self, name):
        sdk_name = 'zcrmsdk.src.'
        name_split = str(name).split('.')
        class_name = name_split.pop()

        package_name = name_split.pop()
        pack_split = re.findall('[A-Z][^A-Z]*', package_name)
        sdk_package_name = pack_split[0].lower()

        if len(pack_split) > 1:
            for i in range(1, len(pack_split)):
                sdk_package_name += '_' + pack_split[i].lower()

        name_split = list(map(lambda x: x.lower(), name_split))
        sdk_name = sdk_name + '.'.join(name_split) + '.' + sdk_package_name + '.' + class_name

        return sdk_name

    def get_json_details(self):
        try:
            from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        if Initializer.json_details is None:
            dir_name = os.path.dirname(__file__)
            filename = os.path.join(dir_name, '..', '..', '..', '..', '..', Constants.JSON_DETAILS_FILE_PATH)

            with open(filename, mode='r') as JSON:
                Initializer.json_details = json.load(JSON)

        return Initializer.json_details
