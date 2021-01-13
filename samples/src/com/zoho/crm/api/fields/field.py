from zcrmsdk.src.com.zoho.crm.api.fields import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Field(object):

    @staticmethod
    def get_fields(module_api_name):

        """
        This method is used to get metadata about all the fields of a module and print the response.
        :param module_api_name: The API Name of the module to get fields
        """

        """
        example
        module_api_name = "Leads";
        """

        # Get instance of FieldsOperations Class that takes module_api_name as parameter
        fields_operations = FieldsOperations(module_api_name)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for get_fields operation
        # param_instance.add(GetFieldsParam.type, "Unused")

        # Call get_fields method that takes paramInstance as parameter
        response = fields_operations.get_fields(param_instance)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Field instances
                    fields_list = response_object.get_fields()

                    for field in fields_list:

                        # Get the ID of each Field
                        print('Field ID: ' + str(field.get_id()))

                        # Get the SystemMandatory of each Field
                        print("Field SystemMandatory: " + str(field.get_system_mandatory()))

                        # Get the Webhook of each Field
                        print("Field Webhook: " + str(field.get_webhook()))

                        # Get the JsonType of each Field
                        print("Field JsonType: " + str(field.get_json_type()))

                        # Get the private info of each field
                        private = field.get_private()

                        if private is not None:
                            # Get the type
                            print("Field Private Type: " + str(private.get_type()))

                            # Get the Export
                            print("Field Private Export: " + str(private.get_export()))

                            # Get the Restricted
                            print("Field Private Restricted: " + str(private.get_restricted()))

                        # Get the obtained Crypt instance
                        crypt = field.get_crypt()

                        if crypt is not None:
                            print("Crypt Details")

                            # Get the Crypt Mode
                            print("Mode: " + crypt.get_mode())

                            # Get the Crypt Column
                            print("Column: " + crypt.get_column())

                            # Get the Crypt Table
                            print("Table: " + crypt.get_table())

                            # Get the Crypt Status
                            print("Status: " + str(crypt.get_status()))

                        # Get the FieldLabel of each Field
                        print("Field FieldLabel: " + field.get_field_label())

                        tool_tip = field.get_tooltip()

                        if tool_tip is not None:
                            # Get the Name of the ToolTip
                            print("Field ToolTip Name: " + tool_tip.get_name())

                            # Get the Value of the ToolTip
                            print("Field ToolTip Value: " + tool_tip.get_value())

                        # Get the CreatedSource of each Field
                        print("Field CreatedSource: " + field.get_created_source())

                        # Get the FieldReadOnly of each Field
                        print("Field FieldReadOnly: " + str(field.get_field_read_only()))

                        # Get the DisplayLabel of each Field
                        print("Field DisplayLabel: " + field.get_display_label())

                        # Get the ReadOnly of each Field
                        print("Field ReadOnly: " + str(field.get_read_only()))

                        # Get the obtained AssociationDetails instance
                        association_details = field.get_association_details()

                        if association_details is not None:

                            # Get the obtained LookupField instance
                            lookup_field = association_details.get_lookup_field()

                            if lookup_field is not None:
                                # Get the ID of the LookupField
                                print("Field AssociationDetails LookupField ID: " + str(lookup_field.get_id()))

                                # Get the Name of the LookupField
                                print('Field AssociationDetails LookupField Name: ' + lookup_field.get_name())

                            # Get the obtained LookupField instance
                            related_field = association_details.get_related_field()

                            if related_field is not None:
                                # Get the ID of the RelatedField
                                print("Field AssociationDetails RelatedField ID: " + str(related_field.get_id()))

                                # Get the Name of the RelatedField
                                print('Field AssociationDetails RelatedField Name: ' + related_field.get_name())

                        if field.get_quick_sequence_number() is not None:
                            # Get the QuickSequenceNumber of each Field
                            print('Field QuickSequenceNumber: ' + str(field.get_quick_sequence_number()))

                        if field.get_businesscard_supported() is not None:
                            # Get the BusinesscardSupported of each Field
                            print('Field BusinesscardSupported: ' + str(field.get_businesscard_supported()))

                        # Check if MultiModuleLookup is not None
                        if field.get_multi_module_lookup() is not None:
                            # Get the MultiModuleLookup dict
                            for key, value in field.get_multi_module_lookup().items():
                                print(key + " : " + value)

                        # Get the obtained Currency instance
                        currency = field.get_currency()

                        if currency is not None:
                            # Get the RoundingOption of the Currency
                            print("Field Currency RoundingOption: " + str(currency.get_rounding_option()))

                            if currency.get_precision() is not None:
                                # Get the Precision of the Currency
                                print("Field Currency Precision: " + str(currency.get_precision()))

                        if field.get_custom_field() is not None:
                            # Get if the Field is a CustomField
                            print("Field CustomField: " + str(field.get_custom_field()))

                        lookup = field.get_lookup()

                        if lookup is not None:
                            # Get the obtained Layout instance
                            layout = lookup.get_layout()

                            # Check if layout is not null
                            if layout is not None:
                                # Get the ID of the Layout
                                print("Field ModuleLookup Layout ID: " + str(layout.get_id()))

                                # Get the Name of the Layout
                                print("Field ModuleLookup Layout Name: " + layout.get_name())

                            # Get the DisplayLabel of the Module
                            print("Field ModuleLookup DisplayLabel: " + str(lookup.get_display_label()))

                            # Get the APIName of the Module
                            print("Field ModuleLookup APIName: " + str(lookup.get_api_name()))

                            # Get the Module of the ModuleLookup
                            print("Field ModuleLookup Module: " + str(lookup.get_module()))

                            if lookup.get_id() is not None:
                                # Get the ID of the Module
                                print("Field ModuleLookup ID: " + str(lookup.get_id()))

                        if field.get_visible() is not None:
                            # Get the Visible of each Field
                            print("Field Visible: " + str(field.get_visible()))

                        if field.get_length() is not None:
                            # Get the Length of each Field
                            print("Field Length: " + str(field.get_length()))

                        view_type = field.get_view_type()

                        if view_type is not None:
                            # Get the View of the ViewType
                            print("Field ViewType View: " + str(view_type.get_view()))

                            # Get the Edit of the ViewType
                            print("Field ViewType Edit: " + str(view_type.get_edit()))

                            # Get the Create of the ViewType
                            print("Field ViewType Create: " + str(view_type.get_create()))

                            # Get the QuickCreate of the ViewType
                            print("Field ViewType QuickCreate: " + str(view_type.get_quick_create()))

                        subform = field.get_subform()

                        if subform is not None:
                            # Get the obtained Layout instance
                            layout = subform.get_layout()

                            # Check if layout is not null
                            if layout is not None:
                                # Get the ID of the Layout
                                print("Field Subform Layout ID: " + str(layout.get_id()))

                                # Get the Name of the Layout
                                print("Field Subform Layout Name: " + layout.get_name())

                            # Get the DisplayLabel of the Module
                            print("Field Subform DisplayLabel: " + str(subform.get_display_label()))

                            # Get the APIName of the Module
                            print("Field Subform APIName: " + str(subform.get_api_name()))

                            # Get the Module of the ModuleLookup
                            print("Field Subform Module: " + str(subform.get_module()))

                            if subform.get_id() is not None:
                                # Get the ID of the Module
                                print("Field Subform ID: " + str(subform.get_id()))

                        # Get the APIName of each Field
                        print("Field APIName : " + field.get_api_name())

                        # Get the obtained Unique instance
                        unique = field.get_unique()

                        if unique is not None:
                            # Get the Casesensitive of the Unique
                            print("Field Unique Casesensitive : " + str(unique.get_casesensitive()))

                        if field.get_history_tracking() is not None:
                            # Get the HistoryTracking of each Field
                            print("Field HistoryTracking: " + str(field.get_history_tracking()))

                        # Get the DataType of each Field
                        print("Field DataType: " + field.get_data_type())

                        # Get the obtained Formula instance
                        formula = field.get_formula()

                        # Check if formula is not null
                        if formula is not None:
                            # Get the ReturnType of the Formula
                            print('Field Formula ReturnType : ' + str(formula.get_return_type()))

                            if formula.get_expression() is not None:
                                # Get the Expression of the Formula
                                print("Field Formula Expression : " + str(formula.get_expression()))

                        if field.get_decimal_place() is not None:
                            # Get the DecimalPlace of each Field
                            print("Field DecimalPlace: " + str(field.get_decimal_place()))

                        # Get the MassUpdate of each Field
                        print("Field MassUpdate: " + str(field.get_mass_update()))

                        if field.get_blueprint_supported() is not None:
                            # Get the BlueprintSupported of each Field
                            print("Field BlueprintSupported: " + str(field.get_blueprint_supported()))

                        multi_select_lookup = field.get_multiselectlookup()

                        # Check if multiSelectLookup is not None
                        if multi_select_lookup is not None:
                            # Get the DisplayLabel of the MultiSelectLookup
                            print("Field MultiSelectLookup DisplayLabel: " + str(multi_select_lookup.get_display_label()))

                            # Get the LinkingModule of the MultiSelectLookup
                            print("Field MultiSelectLookup LinkingModule: " + str(multi_select_lookup.get_linking_module()))

                            # Get the LookupApiname of the MultiSelectLookup
                            print("Field MultiSelectLookup LookupApiname: " + str(multi_select_lookup.get_lookup_apiname()))

                            # Get the APIName of the MultiSelectLookup
                            print("Field MultiSelectLookup APIName: " + str(multi_select_lookup.get_api_name()))

                            # Get the ConnectedlookupApiname of the MultiSelectLookup
                            print("Field MultiSelectLookup ConnectedlookupApiname: " + str(multi_select_lookup.get_connectedlookup_apiname()))

                            # Get the ID of the MultiSelectLookup
                            print("Field MultiSelectLookup ID: " + str(multi_select_lookup.get_id()))

                        pick_list_values = field.get_pick_list_values()

                        if pick_list_values is not None:
                            for pick_list_value in pick_list_values:

                                # Get the DisplayValue of each PickListValue
                                print("Field PickListValue DisplayValue: " + pick_list_value.get_display_value())

                                if pick_list_value.get_sequence_number() is not None:
                                    # Get the SequenceNumber of each PickListValue
                                    print("Field PickListValue SequenceNumber: " + str(pick_list_value.get_sequence_number()))

                                # Get the ExpectedDataType of each PickListValue
                                print("Field PickListValue ExpectedDataType: " + str(pick_list_value.get_expected_data_type()))

                                # Get the ActualValue of each PickListValue
                                print("Field PickListValue ActualValue: " + pick_list_value.get_actual_value())

                                if pick_list_value.get_maps() is not None:
                                    # Get each value from the map
                                    for map in pick_list_value.get_maps():
                                        print(map)

                                # Get the SysRefName of each PickListValues
                                print("Field PickListValue SysRefName: " + str(pick_list_value.get_sys_ref_name()))

                                # Get the Type of each PickListValues
                                print("Field PickListValue Type: " + str(pick_list_value.get_type()))

                        auto_number = field.get_auto_number()

                        # Check if autoNumber is not None
                        if auto_number is not None:
                            # Get the Prefix of the AutoNumber
                            print('Prefix: ' + str(auto_number.get_prefix()))

                            # Get the Suffix of the AutoNumber
                            print('Suffix: ' + str(auto_number.get_suffix()))

                            if auto_number.get_start_number() is not None:
                                # Get the StartNumber of the AutoNumber
                                print('Start Number: ' + str(auto_number.get_start_number()))

                        if field.get_default_value() is not None:
                            # Get the DefaultValue of each Field
                            print("Field DefaultValue: " + str(field.get_default_value()))

                        if field.get_section_id() is not None:
                            # Get the SectionId of each Field
                            print("Field SectionId: " + str(field.get_section_id()))

                        # Check if ValidationRule is not None
                        if field.get_validation_rule() is not None:
                            # Get the validationRule dict
                            for key, value in field.get_validation_rule().items():
                                print(key + " : " + value)

                        # Check if ConvertMapping is not None
                        if field.get_convert_mapping() is not None:
                            # Get the ConvertMapping dict
                            for key, value in field.get_convert_mapping().items():
                                print(key + " : " + str(value))

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
    def get_field(module_api_name, field_id):

        """
        This method is used to get metadata about a single field of a module with fieldID and print the response.
        :param module_api_name: The API Name of the field's module
        :param field_id: The ID of the field to be obtained
        """

        """
        example
        module_api_name = "Leads"
        field_id = 3409643000002293043
        """

        # Get instance of FieldsOperations Class that takes module_api_name as parameter
        fields_operations = FieldsOperations(module_api_name)

        # Call get_field method which takes field_id as parameter
        response = fields_operations.get_field(field_id)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Field instances
                    fields_list = response_object.get_fields()

                    for field in fields_list:

                        # Get the ID of each Field
                        print('Field ID: ' + str(field.get_id()))

                        # Get the SystemMandatory of each Field
                        print("Field SystemMandatory: " + str(field.get_system_mandatory()))

                        # Get the Webhook of each Field
                        print("Field Webhook: " + str(field.get_webhook()))

                        # Get the JsonType of each Field
                        print("Field JsonType: " + str(field.get_json_type()))

                        # Get the private info of each field
                        private = field.get_private()

                        if private is not None:
                            # Get the type
                            print("Field Private Type: " + str(private.get_type()))

                            # Get the Export
                            print("Field Private Export: " + str(private.get_export()))

                            # Get the Restricted
                            print("Field Private Restricted: " + str(private.get_restricted()))

                        # Get the obtained Crypt instance
                        crypt = field.get_crypt()

                        if crypt is not None:
                            print("Crypt Details")

                            # Get the Crypt Mode
                            print("Mode: " + crypt.get_mode())

                            # Get the Crypt Column
                            print("Column: " + crypt.get_column())

                            # Get the Crypt Table
                            print("Table: " + crypt.get_table())

                            # Get the Crypt Status
                            print("Status: " + str(crypt.get_status()))

                        # Get the FieldLabel of each Field
                        print("Field FieldLabel: " + field.get_field_label())

                        tool_tip = field.get_tooltip()

                        if tool_tip is not None:
                            # Get the Name of the ToolTip
                            print("Field ToolTip Name: " + tool_tip.get_name())

                            # Get the Value of the ToolTip
                            print("Field ToolTip Value: " + tool_tip.get_value())

                        # Get the CreatedSource of each Field
                        print("Field CreatedSource: " + field.get_created_source())

                        # Get the FieldReadOnly of each Field
                        print("Field FieldReadOnly: " + str(field.get_field_read_only()))

                        # Get the DisplayLabel of each Field
                        print("Field DisplayLabel: " + field.get_display_label())

                        # Get the ReadOnly of each Field
                        print("Field ReadOnly: " + str(field.get_read_only()))

                        # Get the obtained AssociationDetails instance
                        association_details = field.get_association_details()

                        if association_details is not None:

                            # Get the obtained LookupField instance
                            lookup_field = association_details.get_lookup_field()

                            if lookup_field is not None:
                                # Get the ID of the LookupField
                                print("Field AssociationDetails LookupField ID: " + str(lookup_field.get_id()))

                                # Get the Name of the LookupField
                                print('Field AssociationDetails LookupField Name: ' + lookup_field.get_name())

                            # Get the obtained LookupField instance
                            related_field = association_details.get_related_field()

                            if related_field is not None:
                                # Get the ID of the RelatedField
                                print("Field AssociationDetails RelatedField ID: " + str(related_field.get_id()))

                                # Get the Name of the RelatedField
                                print('Field AssociationDetails RelatedField Name: ' + related_field.get_name())

                        if field.get_quick_sequence_number() is not None:
                            # Get the QuickSequenceNumber of each Field
                            print('Field QuickSequenceNumber: ' + str(field.get_quick_sequence_number()))

                        if field.get_businesscard_supported() is not None:
                            # Get the BusinesscardSupported of each Field
                            print('Field BusinesscardSupported: ' + str(field.get_businesscard_supported()))

                        # Check if MultiModuleLookup is not None
                        if field.get_multi_module_lookup() is not None:
                            # Get the MultiModuleLookup dict
                            for key, value in field.get_multi_module_lookup().items():
                                print(key + " : " + value)

                        # Get the obtained Currency instance
                        currency = field.get_currency()

                        if currency is not None:
                            # Get the RoundingOption of the Currency
                            print("Field Currency RoundingOption: " + str(currency.get_rounding_option()))

                            if currency.get_precision() is not None:
                                # Get the Precision of the Currency
                                print("Field Currency Precision: " + str(currency.get_precision()))

                        if field.get_custom_field() is not None:
                            # Get if the Field is a CustomField
                            print("Field CustomField: " + str(field.get_custom_field()))

                        lookup = field.get_lookup()

                        if lookup is not None:
                            # Get the obtained Layout instance
                            layout = lookup.get_layout()

                            # Check if layout is not null
                            if layout is not None:
                                # Get the ID of the Layout
                                print("Field ModuleLookup Layout ID: " + str(layout.get_id()))

                                # Get the Name of the Layout
                                print("Field ModuleLookup Layout Name: " + layout.get_name())

                            # Get the DisplayLabel of the Module
                            print("Field ModuleLookup DisplayLabel: " + str(lookup.get_display_label()))

                            # Get the APIName of the Module
                            print("Field ModuleLookup APIName: " + str(lookup.get_api_name()))

                            # Get the Module of the ModuleLookup
                            print("Field ModuleLookup Module: " + str(lookup.get_module()))

                            if lookup.get_id() is not None:
                                # Get the ID of the Module
                                print("Field ModuleLookup ID: " + str(lookup.get_id()))

                        if field.get_visible() is not None:
                            # Get the Visible of each Field
                            print("Field Visible: " + str(field.get_visible()))

                        if field.get_length() is not None:
                            # Get the Length of each Field
                            print("Field Length: " + str(field.get_length()))

                        view_type = field.get_view_type()

                        if view_type is not None:
                            # Get the View of the ViewType
                            print("Field ViewType View: " + str(view_type.get_view()))

                            # Get the Edit of the ViewType
                            print("Field ViewType Edit: " + str(view_type.get_edit()))

                            # Get the Create of the ViewType
                            print("Field ViewType Create: " + str(view_type.get_create()))

                            # Get the QuickCreate of the ViewType
                            print("Field ViewType QuickCreate: " + str(view_type.get_quick_create()))

                        subform = field.get_subform()

                        if subform is not None:
                            # Get the obtained Layout instance
                            layout = subform.get_layout()

                            # Check if layout is not null
                            if layout is not None:
                                # Get the ID of the Layout
                                print("Field Subform Layout ID: " + str(layout.get_id()))

                                # Get the Name of the Layout
                                print("Field Subform Layout Name: " + layout.get_name())

                            # Get the DisplayLabel of the Module
                            print("Field Subform DisplayLabel: " + str(subform.get_display_label()))

                            # Get the APIName of the Module
                            print("Field Subform APIName: " + str(subform.get_api_name()))

                            # Get the Module of the ModuleLookup
                            print("Field Subform Module: " + str(subform.get_module()))

                            if subform.get_id() is not None:
                                # Get the ID of the Module
                                print("Field Subform ID: " + str(subform.get_id()))

                        # Get the APIName of each Field
                        print("Field APIName : " + field.get_api_name())

                        # Get the obtained Unique instance
                        unique = field.get_unique()

                        if unique is not None:
                            # Get the Casesensitive of the Unique
                            print("Field Unique Casesensitive : " + str(unique.get_casesensitive()))

                        if field.get_history_tracking() is not None:
                            # Get the HistoryTracking of each Field
                            print("Field HistoryTracking: " + str(field.get_history_tracking()))

                        # Get the DataType of each Field
                        print("Field DataType: " + field.get_data_type())

                        # Get the obtained Formula instance
                        formula = field.get_formula()

                        # Check if formula is not null
                        if formula is not None:
                            # Get the ReturnType of the Formula
                            print('Field Formula ReturnType : ' + str(formula.get_return_type()))

                            if formula.get_expression() is not None:
                                # Get the Expression of the Formula
                                print("Field Formula Expression : " + str(formula.get_expression()))

                        if field.get_decimal_place() is not None:
                            # Get the DecimalPlace of each Field
                            print("Field DecimalPlace: " + str(field.get_decimal_place()))

                        # Get the MassUpdate of each Field
                        print("Field MassUpdate: " + str(field.get_mass_update()))

                        if field.get_blueprint_supported() is not None:
                            # Get the BlueprintSupported of each Field
                            print("Field BlueprintSupported: " + str(field.get_blueprint_supported()))

                        multi_select_lookup = field.get_multiselectlookup()

                        # Check if multiSelectLookup is not None
                        if multi_select_lookup is not None:
                            # Get the DisplayLabel of the MultiSelectLookup
                            print(
                                "Field MultiSelectLookup DisplayLabel: " + str(multi_select_lookup.get_display_label()))

                            # Get the LinkingModule of the MultiSelectLookup
                            print("Field MultiSelectLookup LinkingModule: " + str(
                                multi_select_lookup.get_linking_module()))

                            # Get the LookupApiname of the MultiSelectLookup
                            print("Field MultiSelectLookup LookupApiname: " + str(
                                multi_select_lookup.get_lookup_apiname()))

                            # Get the APIName of the MultiSelectLookup
                            print("Field MultiSelectLookup APIName: " + str(multi_select_lookup.get_api_name()))

                            # Get the ConnectedlookupApiname of the MultiSelectLookup
                            print("Field MultiSelectLookup ConnectedlookupApiname: " + str(
                                multi_select_lookup.get_connectedlookup_apiname()))

                            # Get the ID of the MultiSelectLookup
                            print("Field MultiSelectLookup ID: " + str(multi_select_lookup.get_id()))

                        pick_list_values = field.get_pick_list_values()

                        if pick_list_values is not None:
                            for pick_list_value in pick_list_values:

                                # Get the DisplayValue of each PickListValue
                                print("Field PickListValue DisplayValue: " + pick_list_value.get_display_value())

                                if pick_list_value.get_sequence_number() is not None:
                                    # Get the SequenceNumber of each PickListValue
                                    print("Field PickListValue SequenceNumber: " + str(
                                        pick_list_value.get_sequence_number()))

                                # Get the ExpectedDataType of each PickListValue
                                print("Field PickListValue ExpectedDataType: " + str(
                                    pick_list_value.get_expected_data_type()))

                                # Get the ActualValue of each PickListValue
                                print("Field PickListValue ActualValue: " + pick_list_value.get_actual_value())

                                if pick_list_value.get_maps() is not None:
                                    # Get each value from the map
                                    for map in pick_list_value.get_maps():
                                        print(map)

                                # Get the SysRefName of each PickListValues
                                print("Field PickListValue SysRefName: " + str(pick_list_value.get_sys_ref_name()))

                                # Get the Type of each PickListValues
                                print("Field PickListValue Type: " + str(pick_list_value.get_type()))

                        auto_number = field.get_auto_number()

                        # Check if autoNumber is not None
                        if auto_number is not None:
                            # Get the Prefix of the AutoNumber
                            print('Prefix: ' + str(auto_number.get_prefix()))

                            # Get the Suffix of the AutoNumber
                            print('Suffix: ' + str(auto_number.get_suffix()))

                            if auto_number.get_start_number() is not None:
                                # Get the StartNumber of the AutoNumber
                                print('Start Number: ' + str(auto_number.get_start_number()))

                        if field.get_default_value() is not None:
                            # Get the DefaultValue of each Field
                            print("Field DefaultValue: " + str(field.get_default_value()))

                        if field.get_section_id() is not None:
                            # Get the SectionId of each Field
                            print("Field SectionId: " + str(field.get_section_id()))

                        # Check if ValidationRule is not None
                        if field.get_validation_rule() is not None:
                            # Get the validationRule dict
                            for key, value in field.get_validation_rule().items():
                                print(key + " : " + value)

                        # Check if ConvertMapping is not None
                        if field.get_convert_mapping() is not None:
                            # Get the ConvertMapping dict
                            for key, value in field.get_convert_mapping().items():
                                print(key + " : " + str(value))

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
