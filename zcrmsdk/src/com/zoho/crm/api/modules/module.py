try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Module(object):
	def __init__(self):
		"""Creates an instance of Module"""

		self.__name = None
		self.__global_search_supported = None
		self.__kanban_view = None
		self.__deletable = None
		self.__description = None
		self.__creatable = None
		self.__filter_status = None
		self.__inventory_template_supported = None
		self.__modified_time = None
		self.__plural_label = None
		self.__presence_sub_menu = None
		self.__triggers_supported = None
		self.__id = None
		self.__related_list_properties = None
		self.__properties = None
		self.__per_page = None
		self.__visibility = None
		self.__convertable = None
		self.__editable = None
		self.__emailtemplate_support = None
		self.__profiles = None
		self.__filter_supported = None
		self.__display_field = None
		self.__search_layout_fields = None
		self.__kanban_view_supported = None
		self.__show_as_tab = None
		self.__web_link = None
		self.__sequence_number = None
		self.__singular_label = None
		self.__viewable = None
		self.__api_supported = None
		self.__api_name = None
		self.__quick_create = None
		self.__modified_by = None
		self.__generated_type = None
		self.__feeds_required = None
		self.__scoring_supported = None
		self.__webform_supported = None
		self.__arguments = None
		self.__module_name = None
		self.__business_card_field_limit = None
		self.__custom_view = None
		self.__parent_module = None
		self.__territory = None
		self.__key_modified = dict()

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

	def get_global_search_supported(self):
		"""
		The method to get the global_search_supported

		Returns:
			bool: A bool representing the global_search_supported
		"""

		return self.__global_search_supported

	def set_global_search_supported(self, global_search_supported):
		"""
		The method to set the value to global_search_supported

		Parameters:
			global_search_supported (bool) : A bool representing the global_search_supported
		"""

		if global_search_supported is not None and not isinstance(global_search_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: global_search_supported EXPECTED TYPE: bool', None, None)
		
		self.__global_search_supported = global_search_supported
		self.__key_modified['global_search_supported'] = 1

	def get_kanban_view(self):
		"""
		The method to get the kanban_view

		Returns:
			bool: A bool representing the kanban_view
		"""

		return self.__kanban_view

	def set_kanban_view(self, kanban_view):
		"""
		The method to set the value to kanban_view

		Parameters:
			kanban_view (bool) : A bool representing the kanban_view
		"""

		if kanban_view is not None and not isinstance(kanban_view, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: kanban_view EXPECTED TYPE: bool', None, None)
		
		self.__kanban_view = kanban_view
		self.__key_modified['kanban_view'] = 1

	def get_deletable(self):
		"""
		The method to get the deletable

		Returns:
			bool: A bool representing the deletable
		"""

		return self.__deletable

	def set_deletable(self, deletable):
		"""
		The method to set the value to deletable

		Parameters:
			deletable (bool) : A bool representing the deletable
		"""

		if deletable is not None and not isinstance(deletable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deletable EXPECTED TYPE: bool', None, None)
		
		self.__deletable = deletable
		self.__key_modified['deletable'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

	def get_creatable(self):
		"""
		The method to get the creatable

		Returns:
			bool: A bool representing the creatable
		"""

		return self.__creatable

	def set_creatable(self, creatable):
		"""
		The method to set the value to creatable

		Parameters:
			creatable (bool) : A bool representing the creatable
		"""

		if creatable is not None and not isinstance(creatable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: creatable EXPECTED TYPE: bool', None, None)
		
		self.__creatable = creatable
		self.__key_modified['creatable'] = 1

	def get_filter_status(self):
		"""
		The method to get the filter_status

		Returns:
			bool: A bool representing the filter_status
		"""

		return self.__filter_status

	def set_filter_status(self, filter_status):
		"""
		The method to set the value to filter_status

		Parameters:
			filter_status (bool) : A bool representing the filter_status
		"""

		if filter_status is not None and not isinstance(filter_status, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filter_status EXPECTED TYPE: bool', None, None)
		
		self.__filter_status = filter_status
		self.__key_modified['filter_status'] = 1

	def get_inventory_template_supported(self):
		"""
		The method to get the inventory_template_supported

		Returns:
			bool: A bool representing the inventory_template_supported
		"""

		return self.__inventory_template_supported

	def set_inventory_template_supported(self, inventory_template_supported):
		"""
		The method to set the value to inventory_template_supported

		Parameters:
			inventory_template_supported (bool) : A bool representing the inventory_template_supported
		"""

		if inventory_template_supported is not None and not isinstance(inventory_template_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inventory_template_supported EXPECTED TYPE: bool', None, None)
		
		self.__inventory_template_supported = inventory_template_supported
		self.__key_modified['inventory_template_supported'] = 1

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

	def get_plural_label(self):
		"""
		The method to get the plural_label

		Returns:
			string: A string representing the plural_label
		"""

		return self.__plural_label

	def set_plural_label(self, plural_label):
		"""
		The method to set the value to plural_label

		Parameters:
			plural_label (string) : A string representing the plural_label
		"""

		if plural_label is not None and not isinstance(plural_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: plural_label EXPECTED TYPE: str', None, None)
		
		self.__plural_label = plural_label
		self.__key_modified['plural_label'] = 1

	def get_presence_sub_menu(self):
		"""
		The method to get the presence_sub_menu

		Returns:
			bool: A bool representing the presence_sub_menu
		"""

		return self.__presence_sub_menu

	def set_presence_sub_menu(self, presence_sub_menu):
		"""
		The method to set the value to presence_sub_menu

		Parameters:
			presence_sub_menu (bool) : A bool representing the presence_sub_menu
		"""

		if presence_sub_menu is not None and not isinstance(presence_sub_menu, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: presence_sub_menu EXPECTED TYPE: bool', None, None)
		
		self.__presence_sub_menu = presence_sub_menu
		self.__key_modified['presence_sub_menu'] = 1

	def get_triggers_supported(self):
		"""
		The method to get the triggers_supported

		Returns:
			bool: A bool representing the triggers_supported
		"""

		return self.__triggers_supported

	def set_triggers_supported(self, triggers_supported):
		"""
		The method to set the value to triggers_supported

		Parameters:
			triggers_supported (bool) : A bool representing the triggers_supported
		"""

		if triggers_supported is not None and not isinstance(triggers_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: triggers_supported EXPECTED TYPE: bool', None, None)
		
		self.__triggers_supported = triggers_supported
		self.__key_modified['triggers_supported'] = 1

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

	def get_related_list_properties(self):
		"""
		The method to get the related_list_properties

		Returns:
			RelatedListProperties: An instance of RelatedListProperties
		"""

		return self.__related_list_properties

	def set_related_list_properties(self, related_list_properties):
		"""
		The method to set the value to related_list_properties

		Parameters:
			related_list_properties (RelatedListProperties) : An instance of RelatedListProperties
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.modules.related_list_properties import RelatedListProperties
		except Exception:
			from .related_list_properties import RelatedListProperties

		if related_list_properties is not None and not isinstance(related_list_properties, RelatedListProperties):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list_properties EXPECTED TYPE: RelatedListProperties', None, None)
		
		self.__related_list_properties = related_list_properties
		self.__key_modified['related_list_properties'] = 1

	def get_properties(self):
		"""
		The method to get the properties

		Returns:
			list: An instance of list
		"""

		return self.__properties

	def set_properties(self, properties):
		"""
		The method to set the value to properties

		Parameters:
			properties (list) : An instance of list
		"""

		if properties is not None and not isinstance(properties, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: properties EXPECTED TYPE: list', None, None)
		
		self.__properties = properties
		self.__key_modified['$properties'] = 1

	def get_per_page(self):
		"""
		The method to get the per_page

		Returns:
			int: An int representing the per_page
		"""

		return self.__per_page

	def set_per_page(self, per_page):
		"""
		The method to set the value to per_page

		Parameters:
			per_page (int) : An int representing the per_page
		"""

		if per_page is not None and not isinstance(per_page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: per_page EXPECTED TYPE: int', None, None)
		
		self.__per_page = per_page
		self.__key_modified['per_page'] = 1

	def get_visibility(self):
		"""
		The method to get the visibility

		Returns:
			int: An int representing the visibility
		"""

		return self.__visibility

	def set_visibility(self, visibility):
		"""
		The method to set the value to visibility

		Parameters:
			visibility (int) : An int representing the visibility
		"""

		if visibility is not None and not isinstance(visibility, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: visibility EXPECTED TYPE: int', None, None)
		
		self.__visibility = visibility
		self.__key_modified['visibility'] = 1

	def get_convertable(self):
		"""
		The method to get the convertable

		Returns:
			bool: A bool representing the convertable
		"""

		return self.__convertable

	def set_convertable(self, convertable):
		"""
		The method to set the value to convertable

		Parameters:
			convertable (bool) : A bool representing the convertable
		"""

		if convertable is not None and not isinstance(convertable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convertable EXPECTED TYPE: bool', None, None)
		
		self.__convertable = convertable
		self.__key_modified['convertable'] = 1

	def get_editable(self):
		"""
		The method to get the editable

		Returns:
			bool: A bool representing the editable
		"""

		return self.__editable

	def set_editable(self, editable):
		"""
		The method to set the value to editable

		Parameters:
			editable (bool) : A bool representing the editable
		"""

		if editable is not None and not isinstance(editable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editable EXPECTED TYPE: bool', None, None)
		
		self.__editable = editable
		self.__key_modified['editable'] = 1

	def get_emailtemplate_support(self):
		"""
		The method to get the emailtemplate_support

		Returns:
			bool: A bool representing the emailtemplate_support
		"""

		return self.__emailtemplate_support

	def set_emailtemplate_support(self, emailtemplate_support):
		"""
		The method to set the value to emailtemplate_support

		Parameters:
			emailtemplate_support (bool) : A bool representing the emailtemplate_support
		"""

		if emailtemplate_support is not None and not isinstance(emailtemplate_support, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: emailtemplate_support EXPECTED TYPE: bool', None, None)
		
		self.__emailtemplate_support = emailtemplate_support
		self.__key_modified['emailTemplate_support'] = 1

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

	def get_filter_supported(self):
		"""
		The method to get the filter_supported

		Returns:
			bool: A bool representing the filter_supported
		"""

		return self.__filter_supported

	def set_filter_supported(self, filter_supported):
		"""
		The method to set the value to filter_supported

		Parameters:
			filter_supported (bool) : A bool representing the filter_supported
		"""

		if filter_supported is not None and not isinstance(filter_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filter_supported EXPECTED TYPE: bool', None, None)
		
		self.__filter_supported = filter_supported
		self.__key_modified['filter_supported'] = 1

	def get_display_field(self):
		"""
		The method to get the display_field

		Returns:
			string: A string representing the display_field
		"""

		return self.__display_field

	def set_display_field(self, display_field):
		"""
		The method to set the value to display_field

		Parameters:
			display_field (string) : A string representing the display_field
		"""

		if display_field is not None and not isinstance(display_field, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_field EXPECTED TYPE: str', None, None)
		
		self.__display_field = display_field
		self.__key_modified['display_field'] = 1

	def get_search_layout_fields(self):
		"""
		The method to get the search_layout_fields

		Returns:
			list: An instance of list
		"""

		return self.__search_layout_fields

	def set_search_layout_fields(self, search_layout_fields):
		"""
		The method to set the value to search_layout_fields

		Parameters:
			search_layout_fields (list) : An instance of list
		"""

		if search_layout_fields is not None and not isinstance(search_layout_fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: search_layout_fields EXPECTED TYPE: list', None, None)
		
		self.__search_layout_fields = search_layout_fields
		self.__key_modified['search_layout_fields'] = 1

	def get_kanban_view_supported(self):
		"""
		The method to get the kanban_view_supported

		Returns:
			bool: A bool representing the kanban_view_supported
		"""

		return self.__kanban_view_supported

	def set_kanban_view_supported(self, kanban_view_supported):
		"""
		The method to set the value to kanban_view_supported

		Parameters:
			kanban_view_supported (bool) : A bool representing the kanban_view_supported
		"""

		if kanban_view_supported is not None and not isinstance(kanban_view_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: kanban_view_supported EXPECTED TYPE: bool', None, None)
		
		self.__kanban_view_supported = kanban_view_supported
		self.__key_modified['kanban_view_supported'] = 1

	def get_show_as_tab(self):
		"""
		The method to get the show_as_tab

		Returns:
			bool: A bool representing the show_as_tab
		"""

		return self.__show_as_tab

	def set_show_as_tab(self, show_as_tab):
		"""
		The method to set the value to show_as_tab

		Parameters:
			show_as_tab (bool) : A bool representing the show_as_tab
		"""

		if show_as_tab is not None and not isinstance(show_as_tab, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_as_tab EXPECTED TYPE: bool', None, None)
		
		self.__show_as_tab = show_as_tab
		self.__key_modified['show_as_tab'] = 1

	def get_web_link(self):
		"""
		The method to get the web_link

		Returns:
			string: A string representing the web_link
		"""

		return self.__web_link

	def set_web_link(self, web_link):
		"""
		The method to set the value to web_link

		Parameters:
			web_link (string) : A string representing the web_link
		"""

		if web_link is not None and not isinstance(web_link, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: web_link EXPECTED TYPE: str', None, None)
		
		self.__web_link = web_link
		self.__key_modified['web_link'] = 1

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

	def get_singular_label(self):
		"""
		The method to get the singular_label

		Returns:
			string: A string representing the singular_label
		"""

		return self.__singular_label

	def set_singular_label(self, singular_label):
		"""
		The method to set the value to singular_label

		Parameters:
			singular_label (string) : A string representing the singular_label
		"""

		if singular_label is not None and not isinstance(singular_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: singular_label EXPECTED TYPE: str', None, None)
		
		self.__singular_label = singular_label
		self.__key_modified['singular_label'] = 1

	def get_viewable(self):
		"""
		The method to get the viewable

		Returns:
			bool: A bool representing the viewable
		"""

		return self.__viewable

	def set_viewable(self, viewable):
		"""
		The method to set the value to viewable

		Parameters:
			viewable (bool) : A bool representing the viewable
		"""

		if viewable is not None and not isinstance(viewable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: viewable EXPECTED TYPE: bool', None, None)
		
		self.__viewable = viewable
		self.__key_modified['viewable'] = 1

	def get_api_supported(self):
		"""
		The method to get the api_supported

		Returns:
			bool: A bool representing the api_supported
		"""

		return self.__api_supported

	def set_api_supported(self, api_supported):
		"""
		The method to set the value to api_supported

		Parameters:
			api_supported (bool) : A bool representing the api_supported
		"""

		if api_supported is not None and not isinstance(api_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_supported EXPECTED TYPE: bool', None, None)
		
		self.__api_supported = api_supported
		self.__key_modified['api_supported'] = 1

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

	def get_quick_create(self):
		"""
		The method to get the quick_create

		Returns:
			bool: A bool representing the quick_create
		"""

		return self.__quick_create

	def set_quick_create(self, quick_create):
		"""
		The method to set the value to quick_create

		Parameters:
			quick_create (bool) : A bool representing the quick_create
		"""

		if quick_create is not None and not isinstance(quick_create, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: quick_create EXPECTED TYPE: bool', None, None)
		
		self.__quick_create = quick_create
		self.__key_modified['quick_create'] = 1

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

	def get_generated_type(self):
		"""
		The method to get the generated_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__generated_type

	def set_generated_type(self, generated_type):
		"""
		The method to set the value to generated_type

		Parameters:
			generated_type (Choice) : An instance of Choice
		"""

		if generated_type is not None and not isinstance(generated_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: generated_type EXPECTED TYPE: Choice', None, None)
		
		self.__generated_type = generated_type
		self.__key_modified['generated_type'] = 1

	def get_feeds_required(self):
		"""
		The method to get the feeds_required

		Returns:
			bool: A bool representing the feeds_required
		"""

		return self.__feeds_required

	def set_feeds_required(self, feeds_required):
		"""
		The method to set the value to feeds_required

		Parameters:
			feeds_required (bool) : A bool representing the feeds_required
		"""

		if feeds_required is not None and not isinstance(feeds_required, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: feeds_required EXPECTED TYPE: bool', None, None)
		
		self.__feeds_required = feeds_required
		self.__key_modified['feeds_required'] = 1

	def get_scoring_supported(self):
		"""
		The method to get the scoring_supported

		Returns:
			bool: A bool representing the scoring_supported
		"""

		return self.__scoring_supported

	def set_scoring_supported(self, scoring_supported):
		"""
		The method to set the value to scoring_supported

		Parameters:
			scoring_supported (bool) : A bool representing the scoring_supported
		"""

		if scoring_supported is not None and not isinstance(scoring_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scoring_supported EXPECTED TYPE: bool', None, None)
		
		self.__scoring_supported = scoring_supported
		self.__key_modified['scoring_supported'] = 1

	def get_webform_supported(self):
		"""
		The method to get the webform_supported

		Returns:
			bool: A bool representing the webform_supported
		"""

		return self.__webform_supported

	def set_webform_supported(self, webform_supported):
		"""
		The method to set the value to webform_supported

		Parameters:
			webform_supported (bool) : A bool representing the webform_supported
		"""

		if webform_supported is not None and not isinstance(webform_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: webform_supported EXPECTED TYPE: bool', None, None)
		
		self.__webform_supported = webform_supported
		self.__key_modified['webform_supported'] = 1

	def get_arguments(self):
		"""
		The method to get the arguments

		Returns:
			list: An instance of list
		"""

		return self.__arguments

	def set_arguments(self, arguments):
		"""
		The method to set the value to arguments

		Parameters:
			arguments (list) : An instance of list
		"""

		if arguments is not None and not isinstance(arguments, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: arguments EXPECTED TYPE: list', None, None)
		
		self.__arguments = arguments
		self.__key_modified['arguments'] = 1

	def get_module_name(self):
		"""
		The method to get the module_name

		Returns:
			string: A string representing the module_name
		"""

		return self.__module_name

	def set_module_name(self, module_name):
		"""
		The method to set the value to module_name

		Parameters:
			module_name (string) : A string representing the module_name
		"""

		if module_name is not None and not isinstance(module_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_name EXPECTED TYPE: str', None, None)
		
		self.__module_name = module_name
		self.__key_modified['module_name'] = 1

	def get_business_card_field_limit(self):
		"""
		The method to get the business_card_field_limit

		Returns:
			int: An int representing the business_card_field_limit
		"""

		return self.__business_card_field_limit

	def set_business_card_field_limit(self, business_card_field_limit):
		"""
		The method to set the value to business_card_field_limit

		Parameters:
			business_card_field_limit (int) : An int representing the business_card_field_limit
		"""

		if business_card_field_limit is not None and not isinstance(business_card_field_limit, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: business_card_field_limit EXPECTED TYPE: int', None, None)
		
		self.__business_card_field_limit = business_card_field_limit
		self.__key_modified['business_card_field_limit'] = 1

	def get_custom_view(self):
		"""
		The method to get the custom_view

		Returns:
			CustomView: An instance of CustomView
		"""

		return self.__custom_view

	def set_custom_view(self, custom_view):
		"""
		The method to set the value to custom_view

		Parameters:
			custom_view (CustomView) : An instance of CustomView
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.customviews import CustomView
		except Exception:
			from ..custom_views import CustomView

		if custom_view is not None and not isinstance(custom_view, CustomView):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom_view EXPECTED TYPE: CustomView', None, None)
		
		self.__custom_view = custom_view
		self.__key_modified['custom_view'] = 1

	def get_parent_module(self):
		"""
		The method to get the parent_module

		Returns:
			Module: An instance of Module
		"""

		return self.__parent_module

	def set_parent_module(self, parent_module):
		"""
		The method to set the value to parent_module

		Parameters:
			parent_module (Module) : An instance of Module
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.modules.module import Module
		except Exception:
			from .module import Module

		if parent_module is not None and not isinstance(parent_module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_module EXPECTED TYPE: Module', None, None)
		
		self.__parent_module = parent_module
		self.__key_modified['parent_module'] = 1

	def get_territory(self):
		"""
		The method to get the territory

		Returns:
			Territory: An instance of Territory
		"""

		return self.__territory

	def set_territory(self, territory):
		"""
		The method to set the value to territory

		Parameters:
			territory (Territory) : An instance of Territory
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.modules.territory import Territory
		except Exception:
			from .territory import Territory

		if territory is not None and not isinstance(territory, Territory):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: Territory', None, None)
		
		self.__territory = territory
		self.__key_modified['territory'] = 1

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
