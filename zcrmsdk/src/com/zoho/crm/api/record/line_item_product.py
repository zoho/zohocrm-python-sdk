try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class LineItemProduct(Record):
	def __init__(self):
		"""Creates an instance of LineItemProduct"""
		super().__init__()


	def get_product_code(self):
		"""
		The method to get the product_code

		Returns:
			string: A string representing the product_code
		"""

		return self.get_key_value('Product_Code')

	def set_product_code(self, product_code):
		"""
		The method to set the value to product_code

		Parameters:
			product_code (string) : A string representing the product_code
		"""

		if product_code is not None and not isinstance(product_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: product_code EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Product_Code', product_code)

	def get_currency(self):
		"""
		The method to get the currency

		Returns:
			string: A string representing the currency
		"""

		return self.get_key_value('Currency')

	def set_currency(self, currency):
		"""
		The method to set the value to currency

		Parameters:
			currency (string) : A string representing the currency
		"""

		if currency is not None and not isinstance(currency, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Currency', currency)

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.get_key_value('name')

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('name', name)
