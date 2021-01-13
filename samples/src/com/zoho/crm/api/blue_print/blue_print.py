from zcrmsdk.src.com.zoho.crm.api.blue_print import *
from zcrmsdk.src.com.zoho.crm.api.blue_print import BluePrint as ZCRMBluePrint
from zcrmsdk.src.com.zoho.crm.api.record import Record


class BluePrint(object):

    @staticmethod
    def get_blueprint(module_api_name, record_id):

        """
        This method is used to get a single record's Blueprint details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to get Blueprint
        """

        """
        example
        module_api_name = "Leads"
        record_id = 3409643000002469044
        """

        # Get instance of BluePrintOperations Class that takes record_id and module_api_name as parameters
        blue_print_operations = BluePrintOperations(record_id, module_api_name)

        # Call get_blueprint method
        response = blue_print_operations.get_blueprint()

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

                    # Get the obtained BluePrint instance
                    blue_print = response_object.get_blueprint()

                    # Get the ProcessInfo instance of the obtained BluePrint
                    process_info = blue_print.get_process_info()

                    # Check if ProcessInfo is not None
                    if process_info is not None:
                        # Get the ID of the ProcessInfo
                        print("ProcessInfo ID: " + str(process_info.get_id()))

                        # Get the Field ID of the ProcessInfo
                        print("ProcessInfo Field-ID: " + process_info.get_field_id())

                        # Get the isContinuous of the ProcessInfo
                        print("ProcessInfo isContinuous: " + str(process_info.get_is_continuous()))

                        # Get the API Name of the ProcessInfo
                        print("ProcessInfo API Name: " + process_info.get_api_name())

                        # Get the Continuous of the ProcessInfo
                        print("ProcessInfo Continuous: " + str(process_info.get_continuous()))

                        # Get the FieldLabel of the ProcessInfo
                        print("ProcessInfo FieldLabel: " + process_info.get_field_label())

                        # Get the Name of the ProcessInfo
                        print("ProcessInfo Name: " + process_info.get_name())

                        # Get the ColumnName of the ProcessInfo
                        print("ProcessInfo ColumnName: " + process_info.get_column_name())

                        # Get the FieldValue of the ProcessInfo
                        print("ProcessInfo FieldValue: " + process_info.get_field_value())

                        # Get the FieldName of the ProcessInfo
                        print("ProcessInfo FieldName: " + process_info.get_field_name())

                        # Get the Escalation of the ProcessInfo
                        print("ProcessInfo FieldName: " + str(process_info.get_escalation()))

                    # Get the list of transitions from BluePrint instance
                    transitions = blue_print.get_transitions()

                    for transition in transitions:
                        next_transitions = transition.get_next_transitions()

                        for next_transition in next_transitions:
                            # Get the ID of the NextTransition
                            print("NextTransition ID: " + next_transition.get_id())

                            # Get the Name of the NextTransition
                            print("NextTransition Name: " + next_transition.get_name())

                        data = transition.get_data()

                        if data is not None:
                            # Get the ID of the Record
                            print("Record ID: " + str(data.get_id()))

                            # Get the createdBy User instance of the Record
                            created_by = data.get_created_by()

                            # Check if created_by is not None
                            if created_by is not None:
                                # Get the Name of the created_by User
                                print("Record Created By - Name: " + created_by.get_name())

                                # Get the ID of the created_by User
                                print("Record Created By - ID: " + created_by.get_id())

                            # Get the CreatedTime of the Record
                            print("Record CreatedTime: " + str(data.get_created_time()))

                            if data.get_modified_time() is not None:
                                # Get the ModifiedTime of each Record
                                print("Record ModifiedTime: " + str(data.get_modified_time()))

                            # Get the modified_by User instance of the Record
                            modified_by = data.get_modified_by()

                            # Check if modified_by is not None
                            if modified_by is not None:
                                # Get the Name of the modified_by User
                                print("Record Modified By - Name: " + modified_by.get_name())

                                # Get the ID of the modified_by User
                                print("Record Modified By - ID: " + modified_by.get_id())

                            # Get the list of obtained Tag instance of the Record
                            tags = data.get_tag()

                            if tags is not None:
                                for tag in tags:
                                    # Get the Name of each Tag
                                    print("Record Tag Name: " + tag.get_name())

                                    # Get the Id of each Tag
                                    print("Record Tag ID: " + tag.get_id())

                            # Get all entries from the key_values dict
                            for key, value in data.get_key_values().items():
                                print(key + " : " + str(value))

                        # Get the NextFieldValue of the Transition
                        print("Transition NextFieldValue: " + str(transition.get_next_field_value()))

                        # Get the Name of each Transition
                        print("Transition Name: " + str(transition.get_name()))

                        # Get the CriteriaMatched of the Transition
                        print("Transition CriteriaMatched: " + str(transition.get_criteria_matched()))

                        # Get the ID of the Transition
                        print("Transition ID: " + str(transition.get_id()))

                        # Get the Execution Time of the Transition
                        print("Transition Execution Time: " + str(transition.get_execution_time()))

                        # Get the CriteriaMessage of each Transition
                        print("Transition CriteriaMessage: " + str(transition.get_criteria_message()))

                        fields = transition.get_fields()

                        print("Transition Fields")

                        for field in fields:
                            # Get the Webhook of each Field
                            print("Webhook: " + str(field.get_webhook()))

                            # Get the JsonType of each Field
                            print("JsonType: " + str(field.get_json_type()))

                            # Get the DisplayLabel of each Field
                            print("DisplayLabel: " + field.get_display_label())

                            # Get the SystemMandatory of each Field
                            print("SystemMandatory: " + str(field.get_system_mandatory()))

                            # Get the DataType of each Field
                            print("DataType: " + field.get_data_type())

                            # Get the ColumnName of each Field
                            print("ColumnName: " + str(field.get_column_name()))

                            # Get the PersonalityName of each Field
                            print("PersonalityName: " + str(field.get_personality_name()))

                            # Get the ID of each Field
                            print("ID: " + str(field.get_id()))

                            # Get the TransitionSequence of each Field
                            print("TransitionSequence: " + str(field.get_transition_sequence()))

                            if field.get_mandatory() is not None:
                                # Get the Mandatory of each Field
                                print("Mandatory: " + str(field.get_mandatory()))

                            # Get the obtained Layout instance
                            layout = field.get_layouts()

                            # Check if layout is not null
                            if layout is not None:
                                # Get the ID of the Layout
                                print("Layout ID: " + str(layout.get_id()))

                                # Get the Name of the Layout
                                print("Layout Name: " + str(layout.get_name()))

                            # Get the APIName of each Field
                            print("APIName : " + str(field.get_api_name()))

                            # Get the Content of each Field
                            print("Content: " + str(field.get_content()))

                            # Get the Message of each Field
                            print("Message :" + str(field.get_message()))

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
                            print("FieldLabel: " + str(field.get_field_label()))

                            tool_tip = field.get_tooltip()

                            if tool_tip is not None:
                                # Get the Name of the ToolTip
                                print("ToolTip Name: " + tool_tip.get_name())

                                # Get the Value of the ToolTip
                                print("ToolTip Value: " + tool_tip.get_value())

                            # Get the CreatedSource of each Field
                            print("CreatedSource: " + str(field.get_created_source()))

                            # Get the FieldReadOnly of each Field
                            print("FieldReadOnly: " + str(field.get_field_read_only()))

                            # Get the Criteria of each Field
                            criteria = field.get_criteria()

                            if criteria is not None:
                                BluePrint.print_criteria(criteria)

                            # Get the Related Details of each Field
                            related_details = field.get_related_details()

                            if related_details is not None:
                                # Get the display label of related detail
                                if related_details.get_display_label() is not None:
                                    print("RelatedDetails Display Label: " + related_details.get_display_label())

                                # Get the API Name of related detail
                                print("Related Details API Name: " + str(related_details.get_api_name()))

                                # Get the module of related detail
                                if related_details.get_module() is not None:
                                    module = related_details.get_module()

                                    # Get the layout of the module
                                    if module.get_layout() is not None:
                                        layout = module.get_layout()

                                        print("Related Details Module Layout ID: " + layout.get_id())

                                        print("Related Details Module Layout Name: " + layout.get_name())

                                    # Get the display label of the module
                                    if module.get_display_label() is not None:
                                        print("Related Details Module Display Label: " + module.get_display_label())

                                    # Get the Module API Name of the Related detail module
                                    print("Related Details Module API Name: " + str(module.get_api_name()))

                                    # Get the Module of the Related detail module
                                    print("Related Details Module: " + str(module.get_module()))

                                    # Get the Module Name of the Related detail module
                                    print("Related Details Module Name: " + module.get_module_name())

                                # Get the ID of the Related detail
                                print("Related Details ID: " + str(related_details.get_id()))

                                # Get the Type of the Related detail
                                print("Related Details Type: " + str(related_details.get_type()))

                            # Get the ReadOnly of each Field
                            if field.get_read_only() is not None:
                                print("ReadOnly: " + str(field.get_read_only()))

                            # Get the obtained AssociationDetails instance
                            association_details = field.get_association_details()

                            if association_details is not None:

                                # Get the obtained LookupField instance
                                lookup_field = association_details.get_lookup_field()

                                if lookup_field is not None:
                                    # Get the ID of the LookupField
                                    print("AssociationDetails LookupField ID: " + lookup_field.get_id())

                                    # Get the Name of the LookupField
                                    print('AssociationDetails LookupField Name: ' + lookup_field.get_name())

                                # Get the obtained LookupField instance
                                related_field = association_details.get_related_field()

                                if related_field is not None:
                                    # Get the ID of the RelatedField
                                    print("AssociationDetails RelatedField ID: " + related_field.get_id())

                                    # Get the Name of the RelatedField
                                    print('AssociationDetails RelatedField Name: ' + related_field.get_name())

                            if field.get_quick_sequence_number() is not None:
                                # Get the QuickSequenceNumber of each Field
                                print('QuickSequenceNumber: ' + str(field.get_quick_sequence_number()))

                            # Get the DisplayLabel of each Field
                            print("DisplayLabel: " + field.get_display_label())

                            if field.get_custom_field() is not None:
                                # Get if the Field is a CustomField
                                print("CustomField: " + str(field.get_custom_field()))

                            if field.get_visible() is not None:
                                # Get the Visible of each Field
                                print("Visible: " + str(field.get_visible()))

                            if field.get_length() is not None:
                                # Get the Length of each Field
                                print("Length: " + str(field.get_length()))

                            if field.get_decimal_place() is not None:
                                # Get the DecimalPlace of each Field
                                print("DecimalPlace: " + str(field.get_decimal_place()))

                            # Get the ViewType of each Field
                            view_type = field.get_view_type()

                            if view_type is not None:
                                # Get the View of the ViewType
                                print("View: " + str(view_type.get_view()))

                                # Get the Edit of the ViewType
                                print("Edit: " + str(view_type.get_edit()))

                                # Get the Create of the ViewType
                                print("Create: " + str(view_type.get_create()))

                                # Get the QuickCreate of the ViewType
                                print("QuickCreate: " + str(view_type.get_quick_create()))

                            pick_list_values = field.get_pick_list_values()

                            if pick_list_values is not None:
                                for pick_list_value in pick_list_values:

                                    # Get the DisplayValue of each PickListValue
                                    print("DisplayValue: " + pick_list_value.get_display_value())

                                    if pick_list_value.get_sequence_number() is not None:
                                        # Get the SequenceNumber of each PickListValue
                                        print("SequenceNumber: " + str(
                                            pick_list_value.get_sequence_number()))

                                    # Get the ExpectedDataType of each PickListValue
                                    print("ExpectedDataType: " + str(pick_list_value.get_expected_data_type()))

                                    # Get the ActualValue of each PickListValue
                                    print("ActualValue: " + pick_list_value.get_actual_value())

                                    if pick_list_value.get_maps() is not None:
                                        # Get each value from the map
                                        for map in pick_list_value.get_maps():
                                            print(map)

                                    # Get the SysRefName of each PickListValues
                                    print("SysRefName: " + str(pick_list_value.get_sys_ref_name()))

                                    # Get the Type of each PickListValues
                                    print("Type: " + str(pick_list_value.get_type()))

                            multi_select_lookup = field.get_multiselectlookup()

                            # Check if multiSelectLookup is not None
                            if multi_select_lookup is not None:
                                # Get the DisplayLabel of the MultiSelectLookup
                                print("DisplayLabel: " + str(multi_select_lookup.get_display_label()))

                                # Get the LinkingModule of the MultiSelectLookup
                                print("LinkingModule: " + str(multi_select_lookup.get_linking_module()))

                                # Get the LookupApiname of the MultiSelectLookup
                                print("LookupApiname: " + str(multi_select_lookup.get_lookup_apiname()))

                                # Get the APIName of the MultiSelectLookup
                                print("APIName: " + str(multi_select_lookup.get_api_name()))

                                # Get the ConnectedlookupApiname of the MultiSelectLookup
                                print("ConnectedlookupApiname: " + str(multi_select_lookup.get_connectedlookup_apiname()))

                                # Get the ID of the MultiSelectLookup
                                print("ID: " + str(multi_select_lookup.get_id()))

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
    def update_blueprint(module_api_name, record_id, transition_id):

        """
        This method is used to update a single record's Blueprint details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to update Blueprint
        :param transition_id: The ID of the Blueprint transition Id
        """

        """
        example
        module_api_name = "Leads"
        record_id = 3409643000002469044
        transition_id = 3409643000001172075
        """

        # Get instance of BluePrintOperations Class that takes module_api_name and record_id as parameter
        blue_print_operations = BluePrintOperations(record_id, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to contain BluePrint instances
        blue_print_list = []

        # Get instance of BluePrint Class
        blue_print = ZCRMBluePrint()

        # Set transitionId to the BluePrint instance
        blue_print.set_transition_id(transition_id)

        # Get instance of Record Class
        data = Record()

        lookup = dict()

        lookup['id'] = '8940372937'

        data.add_key_value('Data_3', lookup)

        data.add_key_value('Phone', '8940372937')

        data.add_key_value("Notes", "Updated via blueprint")

        check_list_item = {'item1': True}

        check_list_item_2 = {'item1': True}

        check_list_item_3 = {'item1': True}

        check_lists = [check_list_item, check_list_item_2, check_list_item_3]

        data.add_key_value("CheckLists", check_lists)

        # Set data to the BluePrint instance
        blue_print.set_data(data)

        # Add BluePrint instance to the list
        blue_print_list.append(blue_print)

        # Set the list to bluePrint in BodyWrapper instance
        request.set_blueprint(blue_print_list)

        # Call update_blueprint method that takes BodyWrapper instance as parameter
        response = blue_print_operations.update_blueprint(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected SuccessResponse instance is received.
                if isinstance(response_object, SuccessResponse):

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
    def print_criteria(criteria):

        if criteria.get_comparator() is not None:
            # Get the Comparator of the Criteria
            print('Field Criteria Comparator: ' + criteria.get_comparator().get_value())

        if criteria.get_field() is not None:
            # Get the Field of the Criteria
            print('Field Criteria Field: ' + criteria.get_field())

        if criteria.get_value() is not None:
            # Get the Value of the Criteria
            print('Field Criteria Value: ' + str(criteria.get_value()))

        # Get the List of Criteria instance of each Criteria
        criteria_group = criteria.get_group()

        if criteria_group is not None:
            for each_criteria in criteria_group:
                BluePrint.print_criteria(each_criteria)

        if criteria.get_group_operator() is not None:
            # Get the Group Operator of the Criteria
            print('Field Criteria Group Operator: ' + criteria.get_group_operator().get_value())
