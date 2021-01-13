try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TabTheme(object):
	def __init__(self):
		"""Creates an instance of TabTheme"""

		self.__font_color = None
		self.__background = None
		self.__key_modified = dict()

	def get_font_color(self):
		"""
		The method to get the font_color

		Returns:
			string: A string representing the font_color
		"""

		return self.__font_color

	def set_font_color(self, font_color):
		"""
		The method to set the value to font_color

		Parameters:
			font_color (string) : A string representing the font_color
		"""

		if font_color is not None and not isinstance(font_color, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_color EXPECTED TYPE: str', None, None)
		
		self.__font_color = font_color
		self.__key_modified['font_color'] = 1

	def get_background(self):
		"""
		The method to get the background

		Returns:
			string: A string representing the background
		"""

		return self.__background

	def set_background(self, background):
		"""
		The method to set the value to background

		Parameters:
			background (string) : A string representing the background
		"""

		if background is not None and not isinstance(background, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: background EXPECTED TYPE: str', None, None)
		
		self.__background = background
		self.__key_modified['background'] = 1

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
