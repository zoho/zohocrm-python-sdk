try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class Consent(Record):
	def __init__(self):
		"""Creates an instance of Consent"""
		super().__init__()


	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			User: An instance of User
		"""

		return self.get_key_value('Owner')

	def set_owner(self, owner):
		"""
		The method to set the value to owner

		Parameters:
			owner (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if owner is not None and not isinstance(owner, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: owner EXPECTED TYPE: User', None, None)
		
		self.add_key_value('Owner', owner)

	def get_contact_through_email(self):
		"""
		The method to get the contact_through_email

		Returns:
			bool: A bool representing the contact_through_email
		"""

		return self.get_key_value('Contact_Through_Email')

	def set_contact_through_email(self, contact_through_email):
		"""
		The method to set the value to contact_through_email

		Parameters:
			contact_through_email (bool) : A bool representing the contact_through_email
		"""

		if contact_through_email is not None and not isinstance(contact_through_email, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_email EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Email', contact_through_email)

	def get_contact_through_social(self):
		"""
		The method to get the contact_through_social

		Returns:
			bool: A bool representing the contact_through_social
		"""

		return self.get_key_value('Contact_Through_Social')

	def set_contact_through_social(self, contact_through_social):
		"""
		The method to set the value to contact_through_social

		Parameters:
			contact_through_social (bool) : A bool representing the contact_through_social
		"""

		if contact_through_social is not None and not isinstance(contact_through_social, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_social EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Social', contact_through_social)

	def get_contact_through_survey(self):
		"""
		The method to get the contact_through_survey

		Returns:
			bool: A bool representing the contact_through_survey
		"""

		return self.get_key_value('Contact_Through_Survey')

	def set_contact_through_survey(self, contact_through_survey):
		"""
		The method to set the value to contact_through_survey

		Parameters:
			contact_through_survey (bool) : A bool representing the contact_through_survey
		"""

		if contact_through_survey is not None and not isinstance(contact_through_survey, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_survey EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Survey', contact_through_survey)

	def get_contact_through_phone(self):
		"""
		The method to get the contact_through_phone

		Returns:
			bool: A bool representing the contact_through_phone
		"""

		return self.get_key_value('Contact_Through_Phone')

	def set_contact_through_phone(self, contact_through_phone):
		"""
		The method to set the value to contact_through_phone

		Parameters:
			contact_through_phone (bool) : A bool representing the contact_through_phone
		"""

		if contact_through_phone is not None and not isinstance(contact_through_phone, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_phone EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Phone', contact_through_phone)

	def get_mail_sent_time(self):
		"""
		The method to get the mail_sent_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('Mail_Sent_Time')

	def set_mail_sent_time(self, mail_sent_time):
		"""
		The method to set the value to mail_sent_time

		Parameters:
			mail_sent_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if mail_sent_time is not None and not isinstance(mail_sent_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_sent_time EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('Mail_Sent_Time', mail_sent_time)

	def get_consent_date(self):
		"""
		The method to get the consent_date

		Returns:
			date: An instance of date
		"""

		return self.get_key_value('Consent_Date')

	def set_consent_date(self, consent_date):
		"""
		The method to set the value to consent_date

		Parameters:
			consent_date (date) : An instance of date
		"""

		if consent_date is not None and not isinstance(consent_date, date):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_date EXPECTED TYPE: date', None, None)
		
		self.add_key_value('Consent_Date', consent_date)

	def get_consent_remarks(self):
		"""
		The method to get the consent_remarks

		Returns:
			string: A string representing the consent_remarks
		"""

		return self.get_key_value('Consent_Remarks')

	def set_consent_remarks(self, consent_remarks):
		"""
		The method to set the value to consent_remarks

		Parameters:
			consent_remarks (string) : A string representing the consent_remarks
		"""

		if consent_remarks is not None and not isinstance(consent_remarks, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_remarks EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Consent_Remarks', consent_remarks)

	def get_consent_through(self):
		"""
		The method to get the consent_through

		Returns:
			string: A string representing the consent_through
		"""

		return self.get_key_value('Consent_Through')

	def set_consent_through(self, consent_through):
		"""
		The method to set the value to consent_through

		Parameters:
			consent_through (string) : A string representing the consent_through
		"""

		if consent_through is not None and not isinstance(consent_through, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_through EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Consent_Through', consent_through)

	def get_data_processing_basis(self):
		"""
		The method to get the data_processing_basis

		Returns:
			string: A string representing the data_processing_basis
		"""

		return self.get_key_value('Data_Processing_Basis')

	def set_data_processing_basis(self, data_processing_basis):
		"""
		The method to set the value to data_processing_basis

		Parameters:
			data_processing_basis (string) : A string representing the data_processing_basis
		"""

		if data_processing_basis is not None and not isinstance(data_processing_basis, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_processing_basis EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Data_Processing_Basis', data_processing_basis)
