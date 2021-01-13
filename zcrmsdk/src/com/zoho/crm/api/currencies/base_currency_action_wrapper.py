try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.currencies.base_currency_action_handler import BaseCurrencyActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .base_currency_action_handler import BaseCurrencyActionHandler


class BaseCurrencyActionWrapper(BaseCurrencyActionHandler):
	def __init__(self):
		"""Creates an instance of BaseCurrencyActionWrapper"""
		super().__init__()

		self.__base_currency = None
		self.__key_modified = dict()

	def get_base_currency(self):
		"""
		The method to get the base_currency

		Returns:
			ActionResponse: An instance of ActionResponse
		"""

		return self.__base_currency

	def set_base_currency(self, base_currency):
		"""
		The method to set the value to base_currency

		Parameters:
			base_currency (ActionResponse) : An instance of ActionResponse
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.currencies.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse

		if base_currency is not None and not isinstance(base_currency, ActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: base_currency EXPECTED TYPE: ActionResponse', None, None)
		
		self.__base_currency = base_currency
		self.__key_modified['base_currency'] = 1

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
