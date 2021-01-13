from zcrmsdk.src.com.zoho.crm.api.tags import *
from zcrmsdk.src.com.zoho.crm.api.tags import Tag as ZCRMTag
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Tag(object):

    @staticmethod
    def get_tags(module_api_name):

        """
        This method is used to get all the tags in a module
        :param module_api_name: The API Name of the module to get tags.
        """

        """
        example
        module_api_name = "Leads"
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get Tags operation
        param_instance.add(GetTagsParam.module, module_api_name)

        # param_instance.add(GetTagsParam.my_tags, 'true')

        # Call get_tags method that takes ParameterMap instance as parameter
        response = tags_operations.get_tags(param_instance)

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

                    # Get the list of obtained Tag instances
                    tags_list = response_object.get_tags()

                    for tag in tags_list:
                        # Get the CreatedTime of each Tag
                        print("Tag CreatedTime: " + str(tag.get_created_time()))

                        if tag.get_modified_time() is not None:
                            # Get the ModifiedTime of each Tag
                            print("Tag ModifiedTime: " + str(tag.get_modified_time()))

                        # Get the Name of each Tag
                        print("Tag Name: " + tag.get_name())

                        # Get the modifiedBy User instance of each Tag
                        modified_by = tag.get_modified_by()

                        # Check if modifiedBy is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Tag Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Tag Modified By - ID: " + str(modified_by.get_id()))

                        # Get the ID of each Tag
                        print("Tag ID: " + str(tag.get_id()))

                        # Get the createdBy User instance of each Tag
                        created_by = tag.get_created_by()

                        # Check if createdBy is not None
                        if created_by is not None:
                            # Get the Name of the createdBy User
                            print("Tag Created By - Name: " + created_by.get_name())

                            # Get the ID of the createdBy User
                            print("Tag Created By - ID: " + str(created_by.get_id()))

                    # Get the obtained Info object
                    info = response_object.get_info()

                    # Check if info is not None
                    if info is not None:

                        if info.get_count() is not None:
                            # Get the Count of the Info
                            print("Tag Info Count: " + str(info.get_count()))

                        if info.get_allowed_count() is not None:
                            # Get the AllowedCount of the Info
                            print("Tag Info AllowedCount: " + str(info.get_allowed_count()))

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
    def create_tags(module_api_name):

        """
        This method is used to create new tags and print the response.
        :param module_api_name: The API Name of the module to create tags.
        """

        """
        example
        module_api_name = "Leads"
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Create Tags operation
        param_instance.add(CreateTagsParam.module, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Tag instances
        tags_list = []

        for i in range(1,3):
            # Get instance of Tag Class
            tag = ZCRMTag()

            # Set Name to tag
            tag.set_name("python-tags" + str(i))

            # Add the Tag instance to list
            tags_list.append(tag)

        # Set the list to tags in BodyWrapper instance
        request.set_tags(tags_list)

        # Call create_tags method that takes BodyWrapper instance and ParameterMap instance as parameter
        response = tags_operations.create_tags(request, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_tags()

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
    def update_tags(module_api_name):

        """
        This method is used to update multiple tags simultaneously and print the response.
        :param module_api_name: The API Name of the module to update tags
        """

        """
        example
        module_api_name = "Leads"
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Update Tags operation
        param_instance.add(UpdateTagsParam.module, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Tag instances
        tags_list = []

        # Get instance of Tag Class
        tag_1 = ZCRMTag()

        # Set ID
        tag_1.set_id(3409643000000661047)

        # Set name
        tag_1.set_name("edited-tagname")

        # Add the instance to list
        tags_list.append(tag_1)

        # Get instance of Tag Class
        tag_2 = ZCRMTag()

        # Set ID
        tag_2.set_id(3409643000000661048)

        # Set name
        tag_2.set_name("edited-tagname")

        # Add the instance to list
        tags_list.append(tag_2)

        # Set the list to tags in BodyWrapper instance
        request.set_tags(tags_list)

        # Call update_tags method that takes BodyWrapper instance and ParameterMap instance as parameter
        response = tags_operations.update_tags(request, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_tags()

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
    def update_tag(module_api_name, tag_id):

        """
        This method is used to update single tag and print the response.
        :param module_api_name: The API Name of the module to update tag.
        :param tag_id: The ID of the tag to be updated
        """

        """
        example
        module_api_name = "Leads"
        tag_id = 3409643000000661047
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Update Tag operation
        param_instance.add(UpdateTagParam.module, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Tag instances
        tags_list = []

        # Get instance of Tag Class
        tag_1 = ZCRMTag()

        # Set name
        tag_1.set_name("py- tagname")

        # Add the instance to list
        tags_list.append(tag_1)

        # Set the list to tags in BodyWrapper instance
        request.set_tags(tags_list)

        # Call update_tag method that takes BodyWrapper instance, ParameterMap instance and tag_id as parameter
        response = tags_operations.update_tag(tag_id, request, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_tags()

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
    def delete_tag(tag_id):

        """
        This method is used to delete a tag from the module and print the response.
        :param tag_id: The ID of the tag to be deleted
        """

        """
        example
        tag_id = 3409643000000661047
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Call delete_tag method that takes tag_id as parameter
        response = tags_operations.delete_tag(tag_id)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_tags()

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
    def merge_tags(tag_id, conflict_id):

        """
        This method is used to merge tags and put all the records under the two tags into a single tag and print the response.
        :param tag_id: The ID of the tag
        :param conflict_id: The ID of the conflict tag.
        """

        """
        example
        tag_id = 3409643000000661047
        conflict_id = '3409643000000661026'
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of MergeWrapper Class that will contain the request body
        request = MergeWrapper()

        # List to hold ConflictWrapper instances
        tag_list = []

        # Get instance of ConflictWrapper Class
        conflict_wrapper = ConflictWrapper()

        # Set the conflict ID
        conflict_wrapper.set_conflict_id(conflict_id)

        # Add the instance to list
        tag_list.append(conflict_wrapper)

        # Set the list to tags in BodyWrapper instance
        request.set_tags(tag_list)

        # Call merge_tags method that takes MergeWrapper instance and tag_id as parameter
        response = tags_operations.merge_tags(tag_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_tags()

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
    def add_tags_to_record(module_api_name, record_id, tag_names):

        """
        This method is used to add tags to a specific record and print the response.
        :param module_api_name: The API Name of the module to add tag.
        :param record_id: The ID of the record to add tag
        :param tag_names: The list of tag names
        """

        """
        example
        module_api_name = "Leads"
        record_id = 3409643000002157023
        tag_names = ["addtag1,addtag12"]
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Add Tags to Record operation
        for tag_name in tag_names:
            param_instance.add(AddTagsToRecordParam.tag_names, tag_name)

        param_instance.add(AddTagsToRecordParam.over_write, 'false')

        # Call add_tags_to_record method that takes ParameterMap instance, module_api_name and record_id as parameter
        response = tags_operations.add_tags_to_record(record_id, module_api_name, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected RecordActionWrapper instance is received.
                if isinstance(response_object, RecordActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_data()

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
    def add_tags_to_multiple_records(module_api_name, record_ids, tag_names):

        """
        This method is used to add tags to multiple records simultaneously and print the response.
        :param module_api_name: The API Name of the module to add tags.
        :param record_ids: The list of the record IDs to add tags
        :param tag_names: The list of tag names to be added
        """

        """
        example
        module_api_name = "Leads"
        record_ids = [3409643000002157023, 3409643000002157045]
        tag_names = ["addtag1,addtag12"]
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Add Tags To Multiple Records operation
        for record_id in record_ids:
            param_instance.add(AddTagsToMultipleRecordsParam.ids, record_id)

        for tag_name in tag_names:
            param_instance.add(AddTagsToMultipleRecordsParam.tag_names, tag_name)

        param_instance.add(AddTagsToMultipleRecordsParam.over_write, 'false')

        # Call add_tags_to_multiple_records method that takes ParameterMap instance and module_api_name as parameter
        response = tags_operations.add_tags_to_multiple_records(module_api_name, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected RecordActionWrapper instance is received.
                if isinstance(response_object, RecordActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_data()

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
    def remove_tags_from_record(module_api_name, record_id, tag_names):

        """
        This method is used to delete the tags associated with a specific record and print the response.
        :param module_api_name: The API Name of the module to remove tags
        :param record_id: The ID of the record to delete tags
        :param tag_names: The list of the tag names to be removed.
        :return:
        """

        """
        example
        module_api_name = "Leads"
        record_id = 3409643000002157023
        tag_names = ["addtag1,addtag12"]
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Remove Tags from Record operation
        for tag_name in tag_names:
            param_instance.add(RemoveTagsFromRecordParam.tag_names, tag_name)

        # Call remove_tags_from_record method that takes ParameterMap instance, module_api_name and record_id as parameter
        response = tags_operations.remove_tags_from_record(record_id, module_api_name, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected RecordActionWrapper instance is received.
                if isinstance(response_object, RecordActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_data()

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
    def remove_tags_from_multiple_records(module_api_name, record_ids, tag_names):

        """
        This method is used to delete the tags associated with multiple records and print the response.
        :param module_api_name: The API Name of the module to remove tags.
        :param record_ids: The list of record IDs to remove tags.
        :param tag_names: The list of tag names to be removed
        """

        """
        example
        module_api_name = "Leads"
        record_ids = [3409643000002157023, 3409643000002157025, 3409643000002157020]
        tag_names = ["addtag1,addtag12"]
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Remove Tags from Multiple Records operation
        for record_id in record_ids:
            param_instance.add(RemoveTagsFromMultipleRecordsParam.ids, record_id)

        for tag_name in tag_names:
            param_instance.add(RemoveTagsFromMultipleRecordsParam.tag_names, tag_name)

        # Call remove_tags_from_multiple_records method that takes ParameterMap instance, module_api_name as parameters
        response = tags_operations.remove_tags_from_multiple_records(module_api_name, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected RecordActionWrapper instance is received.
                if isinstance(response_object, RecordActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_data()

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
    def get_record_count_for_tag(module_api_name, tag_id):

        """
        This method is used to get the total number of records under a tag and print the response.
        :param module_api_name: The API Name of the module.
        :param tag_id: The ID of the tag to get the count
        """

        """
        example
        module_api_name = "Leads"
        tag_id = 3409643000000661047
        """

        # Get instance of TagsOperations Class
        tags_operations = TagsOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Record Count operation
        param_instance.add(GetRecordCountForTagParam.module, module_api_name)

        # Call get_record_count_for_tag method that takes param_instance and tag_id as parameter
        response = tags_operations.get_record_count_for_tag(tag_id, param_instance)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected CountWrapper instance is received.
                if isinstance(response_object, CountWrapper):
                    # Get the obtained tag count
                    print("Tag Count: " + response_object.get_count())

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
