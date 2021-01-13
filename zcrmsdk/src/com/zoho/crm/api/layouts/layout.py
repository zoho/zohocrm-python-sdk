try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Layout(object):
	def __init__(self):
		"""Creates an instance of Layout"""

		self.__created_time = None
		self.__convert_mapping = None
		self.__modified_time = None
		self.__visible = None
		self.__created_for = None
		self.__name = None
		self.__modified_by = None
		self.__profiles = None
		self.__id = None
		self.__created_by = None
		self.__sections = None
		self.__status = None
		self.__key_modified = dict()

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_convert_mapping(self):
		"""
		The method to get the convert_mapping

		Returns:
			dict: An instance of dict
		"""

		return self.__convert_mapping

	def set_convert_mapping(self, convert_mapping):
		"""
		The method to set the value to convert_mapping

		Parameters:
			convert_mapping (dict) : An instance of dict
		"""

		if convert_mapping is not None and not isinstance(convert_mapping, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convert_mapping EXPECTED TYPE: dict', None, None)
		
		self.__convert_mapping = convert_mapping
		self.__key_modified['convert_mapping'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_visible(self):
		"""
		The method to get the visible

		Returns:
			bool: A bool representing the visible
		"""

		return self.__visible

	def set_visible(self, visible):
		"""
		The method to set the value to visible

		Parameters:
			visible (bool) : A bool representing the visible
		"""

		if visible is not None and not isinstance(visible, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: visible EXPECTED TYPE: bool', None, None)
		
		self.__visible = visible
		self.__key_modified['visible'] = 1

	def get_created_for(self):
		"""
		The method to get the created_for

		Returns:
			User: An instance of User
		"""

		return self.__created_for

	def set_created_for(self, created_for):
		"""
		The method to set the value to created_for

		Parameters:
			created_for (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if created_for is not None and not isinstance(created_for, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_for EXPECTED TYPE: User', None, None)
		
		self.__created_for = created_for
		self.__key_modified['created_for'] = 1

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

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			User: An instance of User
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_profiles(self):
		"""
		The method to get the profiles

		Returns:
			list: An instance of list
		"""

		return self.__profiles

	def set_profiles(self, profiles):
		"""
		The method to set the value to profiles

		Parameters:
			profiles (list) : An instance of list
		"""

		if profiles is not None and not isinstance(profiles, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: profiles EXPECTED TYPE: list', None, None)
		
		self.__profiles = profiles
		self.__key_modified['profiles'] = 1

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

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_sections(self):
		"""
		The method to get the sections

		Returns:
			list: An instance of list
		"""

		return self.__sections

	def set_sections(self, sections):
		"""
		The method to set the value to sections

		Parameters:
			sections (list) : An instance of list
		"""

		if sections is not None and not isinstance(sections, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sections EXPECTED TYPE: list', None, None)
		
		self.__sections = sections
		self.__key_modified['sections'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			int: An int representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (int) : An int representing the status
		"""

		if status is not None and not isinstance(status, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: int', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

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
