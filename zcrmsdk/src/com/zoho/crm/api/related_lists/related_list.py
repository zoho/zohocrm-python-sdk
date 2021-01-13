try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RelatedList(object):
	def __init__(self):
		"""Creates an instance of RelatedList"""

		self.__id = None
		self.__sequence_number = None
		self.__display_label = None
		self.__api_name = None
		self.__module = None
		self.__name = None
		self.__action = None
		self.__href = None
		self.__type = None
		self.__connectedmodule = None
		self.__linkingmodule = None
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

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			string: A string representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (string) : A string representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: str', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

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

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			string: A string representing the module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_action(self):
		"""
		The method to get the action

		Returns:
			string: A string representing the action
		"""

		return self.__action

	def set_action(self, action):
		"""
		The method to set the value to action

		Parameters:
			action (string) : A string representing the action
		"""

		if action is not None and not isinstance(action, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action EXPECTED TYPE: str', None, None)
		
		self.__action = action
		self.__key_modified['action'] = 1

	def get_href(self):
		"""
		The method to get the href

		Returns:
			string: A string representing the href
		"""

		return self.__href

	def set_href(self, href):
		"""
		The method to set the value to href

		Parameters:
			href (string) : A string representing the href
		"""

		if href is not None and not isinstance(href, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: href EXPECTED TYPE: str', None, None)
		
		self.__href = href
		self.__key_modified['href'] = 1

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

	def get_connectedmodule(self):
		"""
		The method to get the connectedmodule

		Returns:
			string: A string representing the connectedmodule
		"""

		return self.__connectedmodule

	def set_connectedmodule(self, connectedmodule):
		"""
		The method to set the value to connectedmodule

		Parameters:
			connectedmodule (string) : A string representing the connectedmodule
		"""

		if connectedmodule is not None and not isinstance(connectedmodule, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connectedmodule EXPECTED TYPE: str', None, None)
		
		self.__connectedmodule = connectedmodule
		self.__key_modified['connectedmodule'] = 1

	def get_linkingmodule(self):
		"""
		The method to get the linkingmodule

		Returns:
			string: A string representing the linkingmodule
		"""

		return self.__linkingmodule

	def set_linkingmodule(self, linkingmodule):
		"""
		The method to set the value to linkingmodule

		Parameters:
			linkingmodule (string) : A string representing the linkingmodule
		"""

		if linkingmodule is not None and not isinstance(linkingmodule, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linkingmodule EXPECTED TYPE: str', None, None)
		
		self.__linkingmodule = linkingmodule
		self.__key_modified['linkingmodule'] = 1

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
