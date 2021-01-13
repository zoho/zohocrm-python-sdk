try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class PricingDetails(Record):
	def __init__(self):
		"""Creates an instance of PricingDetails"""
		super().__init__()


	def get_to_range(self):
		"""
		The method to get the to_range

		Returns:
			float: A float representing the to_range
		"""

		return self.get_key_value('to_range')

	def set_to_range(self, to_range):
		"""
		The method to set the value to to_range

		Parameters:
			to_range (float) : A float representing the to_range
		"""

		if to_range is not None and not isinstance(to_range, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to_range EXPECTED TYPE: float', None, None)
		
		self.add_key_value('to_range', to_range)

	def get_discount(self):
		"""
		The method to get the discount

		Returns:
			float: A float representing the discount
		"""

		return self.get_key_value('discount')

	def set_discount(self, discount):
		"""
		The method to set the value to discount

		Parameters:
			discount (float) : A float representing the discount
		"""

		if discount is not None and not isinstance(discount, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: discount EXPECTED TYPE: float', None, None)
		
		self.add_key_value('discount', discount)

	def get_from_range(self):
		"""
		The method to get the from_range

		Returns:
			float: A float representing the from_range
		"""

		return self.get_key_value('from_range')

	def set_from_range(self, from_range):
		"""
		The method to set the value to from_range

		Parameters:
			from_range (float) : A float representing the from_range
		"""

		if from_range is not None and not isinstance(from_range, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_range EXPECTED TYPE: float', None, None)
		
		self.add_key_value('from_range', from_range)
