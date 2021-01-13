try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from ..record import Record


class User(Record):
	def __init__(self):
		"""Creates an instance of User"""
		super().__init__()


	def get_country(self):
		"""
		The method to get the country

		Returns:
			string: A string representing the country
		"""

		return self.get_key_value('country')

	def set_country(self, country):
		"""
		The method to set the value to country

		Parameters:
			country (string) : A string representing the country
		"""

		if country is not None and not isinstance(country, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country EXPECTED TYPE: str', None, None)
		
		self.add_key_value('country', country)

	def get_customize_info(self):
		"""
		The method to get the customize_info

		Returns:
			CustomizeInfo: An instance of CustomizeInfo
		"""

		return self.get_key_value('customize_info')

	def set_customize_info(self, customize_info):
		"""
		The method to set the value to customize_info

		Parameters:
			customize_info (CustomizeInfo) : An instance of CustomizeInfo
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users.customize_info import CustomizeInfo
		except Exception:
			from .customize_info import CustomizeInfo

		if customize_info is not None and not isinstance(customize_info, CustomizeInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: customize_info EXPECTED TYPE: CustomizeInfo', None, None)
		
		self.add_key_value('customize_info', customize_info)

	def get_role(self):
		"""
		The method to get the role

		Returns:
			Role: An instance of Role
		"""

		return self.get_key_value('role')

	def set_role(self, role):
		"""
		The method to set the value to role

		Parameters:
			role (Role) : An instance of Role
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.roles import Role
		except Exception:
			from ..roles import Role

		if role is not None and not isinstance(role, Role):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: role EXPECTED TYPE: Role', None, None)
		
		self.add_key_value('role', role)

	def get_signature(self):
		"""
		The method to get the signature

		Returns:
			string: A string representing the signature
		"""

		return self.get_key_value('signature')

	def set_signature(self, signature):
		"""
		The method to set the value to signature

		Parameters:
			signature (string) : A string representing the signature
		"""

		if signature is not None and not isinstance(signature, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signature EXPECTED TYPE: str', None, None)
		
		self.add_key_value('signature', signature)

	def get_city(self):
		"""
		The method to get the city

		Returns:
			string: A string representing the city
		"""

		return self.get_key_value('city')

	def set_city(self, city):
		"""
		The method to set the value to city

		Parameters:
			city (string) : A string representing the city
		"""

		if city is not None and not isinstance(city, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: city EXPECTED TYPE: str', None, None)
		
		self.add_key_value('city', city)

	def get_name_format(self):
		"""
		The method to get the name_format

		Returns:
			string: A string representing the name_format
		"""

		return self.get_key_value('name_format')

	def set_name_format(self, name_format):
		"""
		The method to set the value to name_format

		Parameters:
			name_format (string) : A string representing the name_format
		"""

		if name_format is not None and not isinstance(name_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name_format EXPECTED TYPE: str', None, None)
		
		self.add_key_value('name_format', name_format)

	def get_personal_account(self):
		"""
		The method to get the personal_account

		Returns:
			bool: A bool representing the personal_account
		"""

		return self.get_key_value('personal_account')

	def set_personal_account(self, personal_account):
		"""
		The method to set the value to personal_account

		Parameters:
			personal_account (bool) : A bool representing the personal_account
		"""

		if personal_account is not None and not isinstance(personal_account, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: personal_account EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('personal_account', personal_account)

	def get_default_tab_group(self):
		"""
		The method to get the default_tab_group

		Returns:
			string: A string representing the default_tab_group
		"""

		return self.get_key_value('default_tab_group')

	def set_default_tab_group(self, default_tab_group):
		"""
		The method to set the value to default_tab_group

		Parameters:
			default_tab_group (string) : A string representing the default_tab_group
		"""

		if default_tab_group is not None and not isinstance(default_tab_group, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_tab_group EXPECTED TYPE: str', None, None)
		
		self.add_key_value('default_tab_group', default_tab_group)

	def get_language(self):
		"""
		The method to get the language

		Returns:
			string: A string representing the language
		"""

		return self.get_key_value('language')

	def set_language(self, language):
		"""
		The method to set the value to language

		Parameters:
			language (string) : A string representing the language
		"""

		if language is not None and not isinstance(language, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: language EXPECTED TYPE: str', None, None)
		
		self.add_key_value('language', language)

	def get_locale(self):
		"""
		The method to get the locale

		Returns:
			string: A string representing the locale
		"""

		return self.get_key_value('locale')

	def set_locale(self, locale):
		"""
		The method to set the value to locale

		Parameters:
			locale (string) : A string representing the locale
		"""

		if locale is not None and not isinstance(locale, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locale EXPECTED TYPE: str', None, None)
		
		self.add_key_value('locale', locale)

	def get_microsoft(self):
		"""
		The method to get the microsoft

		Returns:
			bool: A bool representing the microsoft
		"""

		return self.get_key_value('microsoft')

	def set_microsoft(self, microsoft):
		"""
		The method to set the value to microsoft

		Parameters:
			microsoft (bool) : A bool representing the microsoft
		"""

		if microsoft is not None and not isinstance(microsoft, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: microsoft EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('microsoft', microsoft)

	def get_isonline(self):
		"""
		The method to get the isonline

		Returns:
			bool: A bool representing the isonline
		"""

		return self.get_key_value('Isonline')

	def set_isonline(self, isonline):
		"""
		The method to set the value to isonline

		Parameters:
			isonline (bool) : A bool representing the isonline
		"""

		if isonline is not None and not isinstance(isonline, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: isonline EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Isonline', isonline)

	def get_street(self):
		"""
		The method to get the street

		Returns:
			string: A string representing the street
		"""

		return self.get_key_value('street')

	def set_street(self, street):
		"""
		The method to set the value to street

		Parameters:
			street (string) : A string representing the street
		"""

		if street is not None and not isinstance(street, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: street EXPECTED TYPE: str', None, None)
		
		self.add_key_value('street', street)

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

	def get_alias(self):
		"""
		The method to get the alias

		Returns:
			string: A string representing the alias
		"""

		return self.get_key_value('alias')

	def set_alias(self, alias):
		"""
		The method to set the value to alias

		Parameters:
			alias (string) : A string representing the alias
		"""

		if alias is not None and not isinstance(alias, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: alias EXPECTED TYPE: str', None, None)
		
		self.add_key_value('alias', alias)

	def get_theme(self):
		"""
		The method to get the theme

		Returns:
			Theme: An instance of Theme
		"""

		return self.get_key_value('theme')

	def set_theme(self, theme):
		"""
		The method to set the value to theme

		Parameters:
			theme (Theme) : An instance of Theme
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users.theme import Theme
		except Exception:
			from .theme import Theme

		if theme is not None and not isinstance(theme, Theme):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: theme EXPECTED TYPE: Theme', None, None)
		
		self.add_key_value('theme', theme)

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.get_key_value('state')

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.add_key_value('state', state)

	def get_fax(self):
		"""
		The method to get the fax

		Returns:
			string: A string representing the fax
		"""

		return self.get_key_value('fax')

	def set_fax(self, fax):
		"""
		The method to set the value to fax

		Parameters:
			fax (string) : A string representing the fax
		"""

		if fax is not None and not isinstance(fax, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fax EXPECTED TYPE: str', None, None)
		
		self.add_key_value('fax', fax)

	def get_country_locale(self):
		"""
		The method to get the country_locale

		Returns:
			string: A string representing the country_locale
		"""

		return self.get_key_value('country_locale')

	def set_country_locale(self, country_locale):
		"""
		The method to set the value to country_locale

		Parameters:
			country_locale (string) : A string representing the country_locale
		"""

		if country_locale is not None and not isinstance(country_locale, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country_locale EXPECTED TYPE: str', None, None)
		
		self.add_key_value('country_locale', country_locale)

	def get_first_name(self):
		"""
		The method to get the first_name

		Returns:
			string: A string representing the first_name
		"""

		return self.get_key_value('first_name')

	def set_first_name(self, first_name):
		"""
		The method to set the value to first_name

		Parameters:
			first_name (string) : A string representing the first_name
		"""

		if first_name is not None and not isinstance(first_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: first_name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('first_name', first_name)

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.get_key_value('email')

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.add_key_value('email', email)

	def get_reporting_to(self):
		"""
		The method to get the reporting_to

		Returns:
			User: An instance of User
		"""

		return self.get_key_value('Reporting_To')

	def set_reporting_to(self, reporting_to):
		"""
		The method to set the value to reporting_to

		Parameters:
			reporting_to (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users.user import User
		except Exception:
			from .user import User

		if reporting_to is not None and not isinstance(reporting_to, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reporting_to EXPECTED TYPE: User', None, None)
		
		self.add_key_value('Reporting_To', reporting_to)

	def get_decimal_separator(self):
		"""
		The method to get the decimal_separator

		Returns:
			string: A string representing the decimal_separator
		"""

		return self.get_key_value('decimal_separator')

	def set_decimal_separator(self, decimal_separator):
		"""
		The method to set the value to decimal_separator

		Parameters:
			decimal_separator (string) : A string representing the decimal_separator
		"""

		if decimal_separator is not None and not isinstance(decimal_separator, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: decimal_separator EXPECTED TYPE: str', None, None)
		
		self.add_key_value('decimal_separator', decimal_separator)

	def get_zip(self):
		"""
		The method to get the zip

		Returns:
			string: A string representing the zip
		"""

		return self.get_key_value('zip')

	def set_zip(self, zip):
		"""
		The method to set the value to zip

		Parameters:
			zip (string) : A string representing the zip
		"""

		if zip is not None and not isinstance(zip, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zip EXPECTED TYPE: str', None, None)
		
		self.add_key_value('zip', zip)

	def get_website(self):
		"""
		The method to get the website

		Returns:
			string: A string representing the website
		"""

		return self.get_key_value('website')

	def set_website(self, website):
		"""
		The method to set the value to website

		Parameters:
			website (string) : A string representing the website
		"""

		if website is not None and not isinstance(website, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: website EXPECTED TYPE: str', None, None)
		
		self.add_key_value('website', website)

	def get_time_format(self):
		"""
		The method to get the time_format

		Returns:
			string: A string representing the time_format
		"""

		return self.get_key_value('time_format')

	def set_time_format(self, time_format):
		"""
		The method to set the value to time_format

		Parameters:
			time_format (string) : A string representing the time_format
		"""

		if time_format is not None and not isinstance(time_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: time_format EXPECTED TYPE: str', None, None)
		
		self.add_key_value('time_format', time_format)

	def get_offset(self):
		"""
		The method to get the offset

		Returns:
			int: An int representing the offset
		"""

		return self.get_key_value('offset')

	def set_offset(self, offset):
		"""
		The method to set the value to offset

		Parameters:
			offset (int) : An int representing the offset
		"""

		if offset is not None and not isinstance(offset, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: offset EXPECTED TYPE: int', None, None)
		
		self.add_key_value('offset', offset)

	def get_profile(self):
		"""
		The method to get the profile

		Returns:
			Profile: An instance of Profile
		"""

		return self.get_key_value('profile')

	def set_profile(self, profile):
		"""
		The method to set the value to profile

		Parameters:
			profile (Profile) : An instance of Profile
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.profiles import Profile
		except Exception:
			from ..profiles import Profile

		if profile is not None and not isinstance(profile, Profile):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: profile EXPECTED TYPE: Profile', None, None)
		
		self.add_key_value('profile', profile)

	def get_mobile(self):
		"""
		The method to get the mobile

		Returns:
			string: A string representing the mobile
		"""

		return self.get_key_value('mobile')

	def set_mobile(self, mobile):
		"""
		The method to set the value to mobile

		Parameters:
			mobile (string) : A string representing the mobile
		"""

		if mobile is not None and not isinstance(mobile, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mobile EXPECTED TYPE: str', None, None)
		
		self.add_key_value('mobile', mobile)

	def get_last_name(self):
		"""
		The method to get the last_name

		Returns:
			string: A string representing the last_name
		"""

		return self.get_key_value('last_name')

	def set_last_name(self, last_name):
		"""
		The method to set the value to last_name

		Parameters:
			last_name (string) : A string representing the last_name
		"""

		if last_name is not None and not isinstance(last_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('last_name', last_name)

	def get_time_zone(self):
		"""
		The method to get the time_zone

		Returns:
			string: A string representing the time_zone
		"""

		return self.get_key_value('time_zone')

	def set_time_zone(self, time_zone):
		"""
		The method to set the value to time_zone

		Parameters:
			time_zone (string) : A string representing the time_zone
		"""

		if time_zone is not None and not isinstance(time_zone, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: time_zone EXPECTED TYPE: str', None, None)
		
		self.add_key_value('time_zone', time_zone)

	def get_zuid(self):
		"""
		The method to get the zuid

		Returns:
			string: A string representing the zuid
		"""

		return self.get_key_value('zuid')

	def set_zuid(self, zuid):
		"""
		The method to set the value to zuid

		Parameters:
			zuid (string) : A string representing the zuid
		"""

		if zuid is not None and not isinstance(zuid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zuid EXPECTED TYPE: str', None, None)
		
		self.add_key_value('zuid', zuid)

	def get_confirm(self):
		"""
		The method to get the confirm

		Returns:
			bool: A bool representing the confirm
		"""

		return self.get_key_value('confirm')

	def set_confirm(self, confirm):
		"""
		The method to set the value to confirm

		Parameters:
			confirm (bool) : A bool representing the confirm
		"""

		if confirm is not None and not isinstance(confirm, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: confirm EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('confirm', confirm)

	def get_full_name(self):
		"""
		The method to get the full_name

		Returns:
			string: A string representing the full_name
		"""

		return self.get_key_value('full_name')

	def set_full_name(self, full_name):
		"""
		The method to set the value to full_name

		Parameters:
			full_name (string) : A string representing the full_name
		"""

		if full_name is not None and not isinstance(full_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: full_name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('full_name', full_name)

	def get_territories(self):
		"""
		The method to get the territories

		Returns:
			list: An instance of list
		"""

		return self.get_key_value('territories')

	def set_territories(self, territories):
		"""
		The method to set the value to territories

		Parameters:
			territories (list) : An instance of list
		"""

		if territories is not None and not isinstance(territories, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territories EXPECTED TYPE: list', None, None)
		
		self.add_key_value('territories', territories)

	def get_phone(self):
		"""
		The method to get the phone

		Returns:
			string: A string representing the phone
		"""

		return self.get_key_value('phone')

	def set_phone(self, phone):
		"""
		The method to set the value to phone

		Parameters:
			phone (string) : A string representing the phone
		"""

		if phone is not None and not isinstance(phone, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: phone EXPECTED TYPE: str', None, None)
		
		self.add_key_value('phone', phone)

	def get_dob(self):
		"""
		The method to get the dob

		Returns:
			string: A string representing the dob
		"""

		return self.get_key_value('dob')

	def set_dob(self, dob):
		"""
		The method to set the value to dob

		Parameters:
			dob (string) : A string representing the dob
		"""

		if dob is not None and not isinstance(dob, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dob EXPECTED TYPE: str', None, None)
		
		self.add_key_value('dob', dob)

	def get_date_format(self):
		"""
		The method to get the date_format

		Returns:
			string: A string representing the date_format
		"""

		return self.get_key_value('date_format')

	def set_date_format(self, date_format):
		"""
		The method to set the value to date_format

		Parameters:
			date_format (string) : A string representing the date_format
		"""

		if date_format is not None and not isinstance(date_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: date_format EXPECTED TYPE: str', None, None)
		
		self.add_key_value('date_format', date_format)

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.get_key_value('status')

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.add_key_value('status', status)

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
