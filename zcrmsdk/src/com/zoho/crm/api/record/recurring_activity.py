try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RecurringActivity(object):
	def __init__(self):
		"""Creates an instance of RecurringActivity"""

		self.__rrule = None
		self.__key_modified = dict()

	def get_rrule(self):
		"""
		The method to get the rrule

		Returns:
			string: A string representing the rrule
		"""

		return self.__rrule

	def set_rrule(self, rrule):
		"""
		The method to set the value to rrule

		Parameters:
			rrule (string) : A string representing the rrule
		"""

		if rrule is not None and not isinstance(rrule, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rrule EXPECTED TYPE: str', None, None)
		
		self.__rrule = rrule
		self.__key_modified['RRULE'] = 1

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
