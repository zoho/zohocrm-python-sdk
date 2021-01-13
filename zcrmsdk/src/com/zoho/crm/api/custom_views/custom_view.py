try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CustomView(object):
	def __init__(self):
		"""Creates an instance of CustomView"""

		self.__id = None
		self.__name = None
		self.__system_name = None
		self.__display_value = None
		self.__shared_type = None
		self.__category = None
		self.__sort_by = None
		self.__sort_order = None
		self.__favorite = None
		self.__offline = None
		self.__default = None
		self.__system_defined = None
		self.__criteria = None
		self.__shared_details = None
		self.__fields = None
		self.__key_modified = dict()

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

	def get_system_name(self):
		"""
		The method to get the system_name

		Returns:
			string: A string representing the system_name
		"""

		return self.__system_name

	def set_system_name(self, system_name):
		"""
		The method to set the value to system_name

		Parameters:
			system_name (string) : A string representing the system_name
		"""

		if system_name is not None and not isinstance(system_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_name EXPECTED TYPE: str', None, None)
		
		self.__system_name = system_name
		self.__key_modified['system_name'] = 1

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_shared_type(self):
		"""
		The method to get the shared_type

		Returns:
			string: A string representing the shared_type
		"""

		return self.__shared_type

	def set_shared_type(self, shared_type):
		"""
		The method to set the value to shared_type

		Parameters:
			shared_type (string) : A string representing the shared_type
		"""

		if shared_type is not None and not isinstance(shared_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_type EXPECTED TYPE: str', None, None)
		
		self.__shared_type = shared_type
		self.__key_modified['shared_type'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			string: A string representing the category
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (string) : A string representing the category
		"""

		if category is not None and not isinstance(category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: str', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

	def get_sort_by(self):
		"""
		The method to get the sort_by

		Returns:
			string: A string representing the sort_by
		"""

		return self.__sort_by

	def set_sort_by(self, sort_by):
		"""
		The method to set the value to sort_by

		Parameters:
			sort_by (string) : A string representing the sort_by
		"""

		if sort_by is not None and not isinstance(sort_by, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_by EXPECTED TYPE: str', None, None)
		
		self.__sort_by = sort_by
		self.__key_modified['sort_by'] = 1

	def get_sort_order(self):
		"""
		The method to get the sort_order

		Returns:
			string: A string representing the sort_order
		"""

		return self.__sort_order

	def set_sort_order(self, sort_order):
		"""
		The method to set the value to sort_order

		Parameters:
			sort_order (string) : A string representing the sort_order
		"""

		if sort_order is not None and not isinstance(sort_order, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_order EXPECTED TYPE: str', None, None)
		
		self.__sort_order = sort_order
		self.__key_modified['sort_order'] = 1

	def get_favorite(self):
		"""
		The method to get the favorite

		Returns:
			int: An int representing the favorite
		"""

		return self.__favorite

	def set_favorite(self, favorite):
		"""
		The method to set the value to favorite

		Parameters:
			favorite (int) : An int representing the favorite
		"""

		if favorite is not None and not isinstance(favorite, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: favorite EXPECTED TYPE: int', None, None)
		
		self.__favorite = favorite
		self.__key_modified['favorite'] = 1

	def get_offline(self):
		"""
		The method to get the offline

		Returns:
			bool: A bool representing the offline
		"""

		return self.__offline

	def set_offline(self, offline):
		"""
		The method to set the value to offline

		Parameters:
			offline (bool) : A bool representing the offline
		"""

		if offline is not None and not isinstance(offline, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: offline EXPECTED TYPE: bool', None, None)
		
		self.__offline = offline
		self.__key_modified['offline'] = 1

	def get_default(self):
		"""
		The method to get the default

		Returns:
			bool: A bool representing the default
		"""

		return self.__default

	def set_default(self, default):
		"""
		The method to set the value to default

		Parameters:
			default (bool) : A bool representing the default
		"""

		if default is not None and not isinstance(default, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default EXPECTED TYPE: bool', None, None)
		
		self.__default = default
		self.__key_modified['default'] = 1

	def get_system_defined(self):
		"""
		The method to get the system_defined

		Returns:
			bool: A bool representing the system_defined
		"""

		return self.__system_defined

	def set_system_defined(self, system_defined):
		"""
		The method to set the value to system_defined

		Parameters:
			system_defined (bool) : A bool representing the system_defined
		"""

		if system_defined is not None and not isinstance(system_defined, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_defined EXPECTED TYPE: bool', None, None)
		
		self.__system_defined = system_defined
		self.__key_modified['system_defined'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.custom_views.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_shared_details(self):
		"""
		The method to get the shared_details

		Returns:
			list: An instance of list
		"""

		return self.__shared_details

	def set_shared_details(self, shared_details):
		"""
		The method to set the value to shared_details

		Parameters:
			shared_details (list) : An instance of list
		"""

		if shared_details is not None and not isinstance(shared_details, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_details EXPECTED TYPE: list', None, None)
		
		self.__shared_details = shared_details
		self.__key_modified['shared_details'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			list: An instance of list
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (list) : An instance of list
		"""

		if fields is not None and not isinstance(fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: list', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

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
