try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
	from zcrmsdk.src.com.zoho.crm.api.header import Header
	from zcrmsdk.src.com.zoho.crm.api.header_map import HeaderMap
except Exception:
	from ..exception import SDKException
	from ..parameter_map import ParameterMap
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants
	from ..param import Param
	from ..header import Header
	from ..header_map import HeaderMap


class RelatedRecordsOperations(object):
	def __init__(self, related_list_api_name, record_id, module_api_name):
		"""
		Creates an instance of RelatedRecordsOperations with the given parameters

		Parameters:
			related_list_api_name (string) : A string representing the related_list_api_name
			record_id (int) : An int representing the record_id
			module_api_name (string) : A string representing the module_api_name
		"""

		if not isinstance(related_list_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list_api_name EXPECTED TYPE: str', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		self.__related_list_api_name = related_list_api_name
		self.__record_id = record_id
		self.__module_api_name = module_api_name


	def get_related_records(self, param_instance=None, header_instance=None):
		"""
		The method to get related records

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_records(self, request):
		"""
		The method to update related records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delink_records(self, param_instance=None):
		"""
		The method to delink records

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_record(self, related_record_id, header_instance=None):
		"""
		The method to get related record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_record(self, related_record_id, request):
		"""
		The method to update related record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delink_record(self, related_record_id):
		"""
		The method to delink record

		Parameters:
			related_record_id (int) : An int representing the related_record_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetRelatedRecordsParam(object):
	page = Param('page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')


class GetRelatedRecordsHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsHeader')


class DelinkRecordsParam(object):
	ids = Param('ids', 'com.zoho.crm.api.RelatedRecords.DelinkRecordsParam')


class GetRelatedRecordHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordHeader')
