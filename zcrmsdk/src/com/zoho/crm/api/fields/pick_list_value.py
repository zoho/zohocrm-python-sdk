try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class PickListValue(object):
	def __init__(self):
		"""Creates an instance of PickListValue"""

		self.__display_value = None
		self.__sequence_number = None
		self.__expected_data_type = None
		self.__maps = None
		self.__actual_value = None
		self.__sys_ref_name = None
		self.__type = None
		self.__key_modified = dict()

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

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			int: An int representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (int) : An int representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: int', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

	def get_expected_data_type(self):
		"""
		The method to get the expected_data_type

		Returns:
			string: A string representing the expected_data_type
		"""

		return self.__expected_data_type

	def set_expected_data_type(self, expected_data_type):
		"""
		The method to set the value to expected_data_type

		Parameters:
			expected_data_type (string) : A string representing the expected_data_type
		"""

		if expected_data_type is not None and not isinstance(expected_data_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expected_data_type EXPECTED TYPE: str', None, None)
		
		self.__expected_data_type = expected_data_type
		self.__key_modified['expected_data_type'] = 1

	def get_maps(self):
		"""
		The method to get the maps

		Returns:
			list: An instance of list
		"""

		return self.__maps

	def set_maps(self, maps):
		"""
		The method to set the value to maps

		Parameters:
			maps (list) : An instance of list
		"""

		if maps is not None and not isinstance(maps, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: maps EXPECTED TYPE: list', None, None)
		
		self.__maps = maps
		self.__key_modified['maps'] = 1

	def get_actual_value(self):
		"""
		The method to get the actual_value

		Returns:
			string: A string representing the actual_value
		"""

		return self.__actual_value

	def set_actual_value(self, actual_value):
		"""
		The method to set the value to actual_value

		Parameters:
			actual_value (string) : A string representing the actual_value
		"""

		if actual_value is not None and not isinstance(actual_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actual_value EXPECTED TYPE: str', None, None)
		
		self.__actual_value = actual_value
		self.__key_modified['actual_value'] = 1

	def get_sys_ref_name(self):
		"""
		The method to get the sys_ref_name

		Returns:
			string: A string representing the sys_ref_name
		"""

		return self.__sys_ref_name

	def set_sys_ref_name(self, sys_ref_name):
		"""
		The method to set the value to sys_ref_name

		Parameters:
			sys_ref_name (string) : A string representing the sys_ref_name
		"""

		if sys_ref_name is not None and not isinstance(sys_ref_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sys_ref_name EXPECTED TYPE: str', None, None)
		
		self.__sys_ref_name = sys_ref_name
		self.__key_modified['sys_ref_name'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

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
