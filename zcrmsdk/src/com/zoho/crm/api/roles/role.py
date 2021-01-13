try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Role(object):
	def __init__(self):
		"""Creates an instance of Role"""

		self.__display_label = None
		self.__forecast_manager = None
		self.__share_with_peers = None
		self.__name = None
		self.__description = None
		self.__id = None
		self.__reporting_to = None
		self.__admin_user = None
		self.__key_modified = dict()

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

	def get_forecast_manager(self):
		"""
		The method to get the forecast_manager

		Returns:
			User: An instance of User
		"""

		return self.__forecast_manager

	def set_forecast_manager(self, forecast_manager):
		"""
		The method to set the value to forecast_manager

		Parameters:
			forecast_manager (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if forecast_manager is not None and not isinstance(forecast_manager, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: forecast_manager EXPECTED TYPE: User', None, None)
		
		self.__forecast_manager = forecast_manager
		self.__key_modified['forecast_manager'] = 1

	def get_share_with_peers(self):
		"""
		The method to get the share_with_peers

		Returns:
			bool: A bool representing the share_with_peers
		"""

		return self.__share_with_peers

	def set_share_with_peers(self, share_with_peers):
		"""
		The method to set the value to share_with_peers

		Parameters:
			share_with_peers (bool) : A bool representing the share_with_peers
		"""

		if share_with_peers is not None and not isinstance(share_with_peers, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share_with_peers EXPECTED TYPE: bool', None, None)
		
		self.__share_with_peers = share_with_peers
		self.__key_modified['share_with_peers'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_reporting_to(self):
		"""
		The method to get the reporting_to

		Returns:
			User: An instance of User
		"""

		return self.__reporting_to

	def set_reporting_to(self, reporting_to):
		"""
		The method to set the value to reporting_to

		Parameters:
			reporting_to (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if reporting_to is not None and not isinstance(reporting_to, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reporting_to EXPECTED TYPE: User', None, None)
		
		self.__reporting_to = reporting_to
		self.__key_modified['reporting_to'] = 1

	def get_admin_user(self):
		"""
		The method to get the admin_user

		Returns:
			bool: A bool representing the admin_user
		"""

		return self.__admin_user

	def set_admin_user(self, admin_user):
		"""
		The method to set the value to admin_user

		Parameters:
			admin_user (bool) : A bool representing the admin_user
		"""

		if admin_user is not None and not isinstance(admin_user, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: admin_user EXPECTED TYPE: bool', None, None)
		
		self.__admin_user = admin_user
		self.__key_modified['admin_user'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
