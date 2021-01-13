try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zcrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..header import Header


class ProfilesOperations(object):
	def __init__(self, if_modified_since=None):
		"""
		Creates an instance of ProfilesOperations with the given parameters

		Parameters:
			if_modified_since (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if if_modified_since is not None and not isinstance(if_modified_since, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: if_modified_since EXPECTED TYPE: datetime', None, None)
		
		self.__if_modified_since = if_modified_since


	def get_profiles(self):
		"""
		The method to get profiles

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/settings/profiles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('If-Modified-Since', 'com.zoho.crm.api.Profiles.GetProfilesHeader'), self.__if_modified_since)
		try:
			from zcrmsdk.src.com.zoho.crm.api.profiles.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_profile(self, id):
		"""
		The method to get profile

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/settings/profiles/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('If-Modified-Since', 'com.zoho.crm.api.Profiles.GetProfileHeader'), self.__if_modified_since)
		try:
			from zcrmsdk.src.com.zoho.crm.api.profiles.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetProfilesHeader(object):
	pass


class GetProfileHeader(object):
	pass
