from zcrmsdk.src.com.zoho.crm.api.modules import *
from zcrmsdk.src.com.zoho.crm.api.modules import Module as ZCRMModule
from zcrmsdk.src.com.zoho.crm.api.profiles import Profile
from zcrmsdk.src.com.zoho.crm.api import HeaderMap
from datetime import datetime


class Module(object):

    @staticmethod
    def get_modules():

        """
        This method is used to get metadata about all the modules and print the response.
        """

        # Get instance of ModulesOperations Class
        modules_operations = ModulesOperations()

        # Get the instance of HeaderMap Class
        header_instance = HeaderMap()

        # Add header to HeaderMap instance, if necessary
        header_instance.add(GetModulesHeader.if_modified_since, datetime(2020, 1, 1, 10, 1, 1))

        # Call get_modules method that takes header_instance as parameter
        response = modules_operations.get_modules(header_instance)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Module instances
                    modules_list = response_object.get_modules()

                    for module in modules_list:
                        # Get the ID of each module
                        print("Module ID: " + str(module.get_id()))

                        # Get the API Name of each module
                        print("Module API Name: " + str(module.get_api_name()))

                        # Get the Name of each Module
                        print("Module Name: " + str(module.get_module_name()))

                        # Get the Convertable of each Module
                        print("Module Is Convertable: " + str(bool(module.get_convertable())))

                        # Get the Editable of each Module
                        print("Module Is editable: " + str(bool(module.get_editable())))

                        # Get the Deletable of each Module
                        print("Module Is deletable: " + str(bool(module.get_deletable())))

                        # Get the WebLink of each Module
                        print("Module Web Link: " + str(module.get_web_link()))

                        # Get the SingularLabel of each Module
                        print("Module Singular Label: " + str(module.get_singular_label()))

                        if module.get_modified_time() is not None:
                            # Get the ModifiedTime of each Module
                            print("Module Modified Time: " + str(module.get_modified_time()))

                        # Get the Viewable of each Module
                        print("Module Is viewable: " + str(bool(module.get_viewable())))

                        # Get the APISupported of each Module
                        print("Module Is API supported: " + str(bool(module.get_api_supported())))

                        # Get the Creatable of each Module
                        print("Module Is creatable: " + str(module.get_creatable()))

                        # Get the PluralLabel of each Module
                        print("Module Plural Label: " + str(bool(module.get_plural_label())))

                        # Get the GeneratedType of each Module
                        print("Module Generated Type: " + str(bool(module.get_generated_type())))

                        # Get the list of Argument instance of each Module
                        arguments = module.get_arguments()

                        # Check if arguments is not None
                        if arguments is not None:

                            for argument in arguments:
                                # Get the Name of each Argument
                                print('Module Argument Name: ' + argument.get_name())

                                # Get the Value of each Argument
                                print("Module Argument Value: " + argument.get_value())

                        # Get the modifiedBy User instance of each Module
                        modified_by_user = module.get_modified_by()

                        # Check if modified_by_user is not None
                        if modified_by_user is not None:

                            # Get the ID of the modifiedBy User
                            print("Module Modified By User-ID: " + str(modified_by_user.get_id()))

                            # Get the name of the modifiedBy User
                            print("Module Modified By User-Name: " + str(modified_by_user.get_name()))

                        # Get the GlobalSearchSupported of each Module
                        print("Module Is Global Search Supported: " + str(bool(module.get_global_search_supported())))

                        # Get the PresenceSubMenu of each Module
                        print("Module Presence Sub Menu: " + str(bool(module.get_presence_sub_menu())))

                        # Get the TriggersSupported of each Module
                        print("Module Is Triggers Supported: " + str(bool(module.get_triggers_supported())))

                        # Get the FeedsRequired of each Module
                        print("Module Is Feeds Required: " + str(bool(module.get_feeds_required())))

                        # Get the ScoringSupported of each Module
                        print("Module Is Scoring Supported: " + str(bool(module.get_scoring_supported())))

                        # Get the WebformSupported of each Module
                        print("Module Is Webform Supported: " + str(bool(module.get_webform_supported())))

                        # Get the KanbanView of each Module
                        if module.get_kanban_view() is not None:
                            print("Module Is Kanban view: " + str(bool(module.get_kanban_view())))

                        # Get the KanbanViewSupported of each Module
                        print("Module Is Kanban view Supported: " + str(bool(module.get_kanban_view_supported())))

                        # Get the ShowAsTab of each Module
                        print("Module Show as tab: " + str(bool(module.get_show_as_tab())))

                        # Get the FilterStatus of each Module
                        print("Module Filter Status: " + str(bool(module.get_filter_status())))

                        # Get the QuickCreate of each Module
                        print("Module Quick Create: " + str(bool(module.get_quick_create())))

                        # Get the EmailtemplateSupport of each Module
                        print("Module Is email template Supported: " + str(bool(module.get_emailtemplate_support())))

                        # Get the InventoryTemplateSupported of each Module
                        print("Module Is inventory template Supported: " + str(
                            bool(module.get_inventory_template_supported())))

                        # Get the Description of each Module
                        print("Module Description: " + str(module.get_description()))

                        # Get the DisplayField of each Module
                        print("Module Display Field: " + str(module.get_display_field()))

                        # Get the Visibility of each Module
                        print("Module Visibility: " + str(module.get_visibility()))

                        # Get the BusinessCardFieldLimit of each Module
                        print("Module Business card field limit: " + str(module.get_business_card_field_limit()))

                        # Get the PerPage of each Module
                        print("Module Per page: " + str(module.get_per_page()))

                        # Get the SequenceNumber of each Module
                        print("Module Sequence Number: " + str(module.get_sequence_number()))

                        # Get the list of Profile instance of each Module
                        profiles = module.get_profiles()

                        # Check if profiles is not null
                        if profiles is not None and len(profiles) > 0:
                            for profile in profiles:
                                # Get the Name of each Profile
                                print('Name: ' + str(profile.get_name()))

                                # Get the Id of each Profile
                                print('ID: ' + str(profile.get_id()))

                        # Get List of SearchLayoutFields APIName
                        search_layout_fields = module.get_search_layout_fields()

                        if search_layout_fields is not None:
                            print("Module SearchLayoutFields Fields: ")

                            for field in search_layout_fields:
                                print(field, end=",")

                            print('\n')

                        # Get the RelatedListProperties instance of each Module
                        related_list_properties = module.get_related_list_properties()

                        # Check if relatedListProperties is not None
                        if related_list_properties is not None:
                            # Get the SortBy of RelatedListProperties
                            print('Module RelatedListProperties Sort By:' + str(related_list_properties.get_sort_by()))

                            # Get the SortOrder of RelatedListProperties
                            print('Module RelatedListProperties Sort Order:' + str(related_list_properties.get_sort_order()))

                            # Get List of fields APIName
                            fields = related_list_properties.get_fields()

                            # Check if fields is not None
                            if fields is not None:
                                print('Module RelatedListProperties Fields')

                                for field in fields:
                                    print(field, end=",")

                                print('\n')

                        # Get List of properties field APIName
                        properties = module.get_properties()

                        # Check if properties is not None
                        if properties is not None:
                            print("Module Properties Fields: ")

                            # Get the Field Name
                            for property in properties:
                                print(property, end=',')

                            print('\n')

                        # Get the parentModule Module instance of each Module
                        parent_module = module.get_parent_module()

                        # Check if parentModule is not null
                        if parent_module is not None and parent_module.get_api_name() is not None:
                            # Get the ID of Parent Module
                            print('Module Parent Module Id: ' + str(parent_module.get_id()))

                            # Get the Name of Parent Module
                            print('Module Parent Module Name: ' + str(parent_module.get_api_name()))

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def get_module(module_api_name):

        """
        This method is used to get metadata about single module with it's API Name and print the response.
        :param module_api_name: The API Name of the module to obtain metadata
        """

        """
        example
        module_api_name = "Leads";
        """

        # Get instance of ModulesOperations Class
        modules_operations = ModulesOperations()

        # Call get_module method that takes module_api_name as parameter
        response = modules_operations.get_module(module_api_name)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Module instances
                    modules_list = response_object.get_modules()

                    for module in modules_list:
                        # Get the ID of each module
                        print("Module ID: " + str(module.get_id()))

                        # Get the API Name of each module
                        print("Module API Name: " + str(module.get_api_name()))

                        # Get the Name of each Module
                        print("Module Name: " + str(module.get_module_name()))

                        # Get the Convertable of each Module
                        print("Module Is Convertable: " + str(bool(module.get_convertable())))

                        # Get the Editable of each Module
                        print("Module Is editable: " + str(bool(module.get_editable())))

                        # Get the Deletable of each Module
                        print("Module Is deletable: " + str(bool(module.get_deletable())))

                        # Get the WebLink of each Module
                        print("Module Web Link: " + str(module.get_web_link()))

                        # Get the SingularLabel of each Module
                        print("Module Singular Label: " + str(module.get_singular_label()))

                        if module.get_modified_time() is not None:
                            # Get the ModifiedTime of each Module
                            print("Module Modified Time: " + str(module.get_modified_time()))

                        # Get the Viewable of each Module
                        print("Module Is viewable: " + str(bool(module.get_viewable())))

                        # Get the APISupported of each Module
                        print("Module Is API supported: " + str(bool(module.get_api_supported())))

                        # Get the Creatable of each Module
                        print("Module Is creatable: " + str(module.get_creatable()))

                        # Get the PluralLabel of each Module
                        print("Module Plural Label: " + str(bool(module.get_plural_label())))

                        # Get the GeneratedType of each Module
                        print("Module Generated Type: " + str(bool(module.get_generated_type())))

                        # Get the list of Argument instance of each Module
                        arguments = module.get_arguments()

                        # Check if arguments is not None
                        if arguments is not None:

                            for argument in arguments:
                                # Get the Name of each Argument
                                print('Module Argument Name: ' + argument.get_name())

                                # Get the Value of each Argument
                                print("Module Argument Value: " + argument.get_value())

                        # Get the modifiedBy User instance of each Module
                        modified_by_user = module.get_modified_by()

                        # Check if modified_by_user is not None
                        if modified_by_user is not None:
                            # Get the ID of the modifiedBy User
                            print("Module Modified By User-ID: " + str(modified_by_user.get_id()))

                            # Get the name of the modifiedBy User
                            print("Module Modified By User-Name: " + str(modified_by_user.get_name()))

                        # Get the GlobalSearchSupported of each Module
                        print("Module Is Global Search Supported: " + str(bool(module.get_global_search_supported())))

                        # Get the PresenceSubMenu of each Module
                        print("Module Presence Sub Menu: " + str(bool(module.get_presence_sub_menu())))

                        # Get the TriggersSupported of each Module
                        print("Module Is Triggers Supported: " + str(bool(module.get_triggers_supported())))

                        # Get the FeedsRequired of each Module
                        print("Module Is Feeds Required: " + str(bool(module.get_feeds_required())))

                        # Get the ScoringSupported of each Module
                        print("Module Is Scoring Supported: " + str(bool(module.get_scoring_supported())))

                        # Get the WebformSupported of each Module
                        print("Module Is Webform Supported: " + str(bool(module.get_webform_supported())))

                        # Get the KanbanView of each Module
                        print("Module Is Kanban view: " + str(bool(module.get_kanban_view())))

                        # Get the KanbanViewSupported of each Module
                        if module.get_kanban_view_supported() is not None:
                            print("Module Is Kanban view Supported: " + str(bool(module.get_kanban_view_supported())))

                        # Get the ShowAsTab of each Module
                        print("Module Show as tab: " + str(bool(module.get_show_as_tab())))

                        # Get the FilterStatus of each Module
                        print("Module Filter Status: " + str(bool(module.get_filter_status())))

                        # Get the QuickCreate of each Module
                        print("Module Quick Create: " + str(bool(module.get_quick_create())))

                        # Get the EmailtemplateSupport of each Module
                        print("Module Is email template Supported: " + str(bool(module.get_emailtemplate_support())))

                        # Get the InventoryTemplateSupported of each Module
                        print("Module Is inventory template Supported: " + str(
                            bool(module.get_inventory_template_supported())))

                        # Get the Description of each Module
                        print("Module Description: " + str(module.get_description()))

                        # Get the DisplayField of each Module
                        print("Module Display Field: " + str(module.get_display_field()))

                        # Get the Visibility of each Module
                        print("Module Visibility: " + str(module.get_visibility()))

                        # Get the BusinessCardFieldLimit of each Module
                        print("Module Business card field limit: " + str(module.get_business_card_field_limit()))

                        # Get the PerPage of each Module
                        print("Module Per page: " + str(module.get_per_page()))

                        # Get the SequenceNumber of each Module
                        print("Module Sequence Number: " + str(module.get_sequence_number()))

                        # Get the CustomView instance of each Module
                        custom_view = module.get_custom_view()

                        if custom_view is not None:
                            Module.print_custom_view(custom_view)

                        # Get the list of Profile instance of each Module
                        profiles = module.get_profiles()

                        # Check if profiles is not null
                        if profiles is not None and len(profiles) > 0:
                            for profile in profiles:
                                # Get the Name of each Profile
                                print('Name: ' + str(profile.get_name()))

                                # Get the Id of each Profile
                                print('ID: ' + str(profile.get_id()))

                        # Get List of SearchLayoutFields APIName
                        search_layout_fields = module.get_search_layout_fields()

                        if search_layout_fields is not None:
                            print("Module SearchLayoutFields Fields: ")

                            for field in search_layout_fields:
                                print(field, end=",")

                            print('\n')

                        # Get the RelatedListProperties instance of each Module
                        related_list_properties = module.get_related_list_properties()

                        # Check if relatedListProperties is not None
                        if related_list_properties is not None:
                            # Get the SortBy of RelatedListProperties
                            print('Module RelatedListProperties Sort By:' + str(related_list_properties.get_sort_by()))

                            # Get the SortOrder of RelatedListProperties
                            print('Module RelatedListProperties Sort Order:' + str(
                                related_list_properties.get_sort_order()))

                            # Get List of fields APIName
                            fields = related_list_properties.get_fields()

                            # Check if fields is not None
                            if fields is not None:
                                print('Module RelatedListProperties Fields')

                                for field in fields:
                                    print(field, end=",")

                                print('\n')

                        # Get List of properties field APIName
                        properties = module.get_properties()

                        # Check if properties is not None
                        if properties is not None:
                            print("Module Properties Fields: ")

                            # Get the Field Name
                            for property in properties:
                                print(property, end=',')

                            print('\n')

                        # Get the parentModule Module instance of each Module
                        parent_module = module.get_parent_module()

                        # Check if parentModule is not null
                        if parent_module is not None and parent_module.get_api_name() is not None:
                            # Get the ID of Parent Module
                            print('Module Parent Module Id: ' + str(parent_module.get_id()))

                            # Get the Name of Parent Module
                            print('Module Parent Module Name: ' + str(parent_module.get_api_name()))

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def update_module_by_api_name(module_api_name):

        """
        This method is used to update module details using module APIName and print the response.
        :param module_api_name: The API Name of the module to update
        """

        """
        example
        module_api_name = "Leads";
        """

        # Get instance of ModulesOperations Class
        modules_operations = ModulesOperations()

        modules_list = []

        profiles_list = []

        # Get instance of Profile Class
        profile = Profile()

        # To set the Profile Id
        profile.set_id(3409643000000395047)

        # Add Profile instance to the list
        profiles_list.append(profile)

        # Get instance of Module Class
        module = ZCRMModule()

        # Set the list to profiles in Module instance
        module.set_profiles(profiles_list)

        # Add the Module instance to list
        modules_list.append(module)

        # Get instance of BodyWrapper Class which contains the request body
        request = BodyWrapper()

        # Set the list to modules in BodyWrapper instance
        request.set_modules(modules_list)

        # Call update_module_by_api_name method that takes BodyWrapper instance and module_api_name as parameter
        response = modules_operations.update_module_by_api_name(module_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_modules()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessResponse):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " + action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " + action_response.get_message().get_value())

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def update_module_by_id(module_id):

        """
        This method is used to update module details using module Id and print the response.
        :param module_id: The id of the module to update
        """

        """
        example
        module_id = 3409643000000252001
        """

        # Get instance of ModulesOperations Class
        modules_operations = ModulesOperations()

        modules_list = []

        profiles_list = []

        # Get instance of Profile Class
        profile = Profile()

        # To set the Profile Id
        profile.set_id(3409643000000395047)

        profile.set_delete(True)

        # Add Profile instance to the list
        profiles_list.append(profile)

        # Get instance of Module Class
        module = ZCRMModule()

        # Set the list to profiles in Module instance
        module.set_profiles(profiles_list)

        # Add the Module instance to list
        modules_list.append(module)

        # Get instance of BodyWrapper Class which contains the request body
        request = BodyWrapper()

        # Set the list to modules in BodyWrapper instance
        request.set_modules(modules_list)

        # Call update_module_by_id method that takes BodyWrapper instance and module_id as parameter
        response = modules_operations.update_module_by_id(module_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_modules()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessResponse):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " + action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " + action_response.get_message().get_value())

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_custom_view(custom_view):
        # Get the ID of the CustomView
        print('CustomView ID: ' + str(custom_view.get_id()))

        # Get the Name of the CustomView
        print('CustomView Name: ' + str(custom_view.get_name()))

        # Get the System Name of the CustomView
        print('CustomView System Name: ' + str(custom_view.get_system_name()))

        # Get the DisplayValue of the CustomView
        print('CustomView Display Value: ' + str(custom_view.get_display_value()))

        # Get the SharedType of the CustomView
        print('CustomView SharedType: ' + str(custom_view.get_shared_type()))

        # Get the Offline value of the CustomView
        print('CustomView Is offline: ' + str(custom_view.get_offline()))

        # Get the default value of the CustomView
        print('CustomView Is default: ' + str(custom_view.get_default()))

        # Get the SortOrder of the CustomView
        print('CustomView SortBy: ' + str(custom_view.get_sort_by()))

        if custom_view.get_sort_order() is not None:
            # Get the SortOrder of the CustomView
            print('CustomView SortOrder: ' + str(custom_view.get_sort_order()))

        # Get the SystemDefined of the CustomView
        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))

        if custom_view.get_favorite() is not None:
            # Get the Favorite of the CustomView
            print('CustomView Favorite: ' + str(custom_view.get_favorite()))

        # Get the Criteria instance of the CustomView
        criteria = custom_view.get_criteria()

        if criteria is not None:
            Module.print_criteria(criteria)

        # # Get the fields of the CustomView
        fields = custom_view.get_fields()

        if fields is not None:
            print('Fields')

            for field in fields:
                print(field)

        shared_details = custom_view.get_shared_details()

        if shared_details is not None:
            for shared_detail in shared_details:
                # Get the Name of the each SharedDetails
                print("SharedDetails Name: " + shared_detail.get_name())

                # Get the ID of the each SharedDetails
                print("SharedDetails ID: " + shared_detail.get_id())

                # Get the Type of the each SharedDetails
                print("SharedDetails Type: " + shared_detail.get_type())

                # Get the Subordinates of the each SharedDetails
                print("SharedDetails Subordinates: " + str(shared_detail.get_subordinates()))

    @staticmethod
    def print_criteria(criteria):

        if criteria.get_comparator() is not None:
            # Get the Comparator of the Criteria
            print('CustomView Criteria Comparator: ' + criteria.get_comparator().get_value())

        if criteria.get_field() is not None:
            # Get the Field of the Criteria
            print('CustomView Criteria Field: ' + criteria.get_field())

        if criteria.get_value() is not None:
            # Get the Value of the Criteria
            print('CustomView Criteria Value: ' + str(criteria.get_value()))

        # Get the List of Criteria instance of each Criteria
        criteria_group = criteria.get_group()

        if criteria_group is not None:
            for each_criteria in criteria_group:
                Module.print_criteria(each_criteria)

        if criteria.get_group_operator() is not None:
            # Get the Group Operator of the Criteria
            print('CustomView Criteria Group Operator: ' + criteria.get_group_operator().get_value())




