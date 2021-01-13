from zcrmsdk.src.com.zoho.crm.api.share_records import *
from zcrmsdk.src.com.zoho.crm.api.share_records import ShareRecord as ZCRMShareRecord
from zcrmsdk.src.com.zoho.crm.api.users import User
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class ShareRecord(object):

    @staticmethod
    def get_shared_record_details(module_api_name, record_id):

        """
        This method is used to get the details of a shared record and print the response.
        :param module_api_name: The API Name of the module to get shared record details.
        :param record_id: The ID of the record to be obtain shared information
        :return:
        """

        """
        example
        module_api_name = Contacts
        record_id = 3409643000002112011
        """

        # Get instance of ShareRecordsOperations Class that takes module_api_name and record_id as parameter
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get Shared Record Details operation

        # Allowed values - summary, manage
        param_instance.add(GetSharedRecordDetailsParam.view, 'manage')

        # param_instance.add(GetSharedRecordDetailsParam.sharedto, 3409643000000302031)

        # Call get_shared_record_details method that takes ParameterMap instance as parameter
        response = shared_records_operations.get_shared_record_details(param_instance)

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

                    # Get the list of obtained ShareRecord instances
                    share_records_list = response_object.get_share()

                    for share_record in share_records_list:
                        # Get the ShareRelatedRecords of each ShareRecord
                        print("ShareRecord ShareRelatedRecords: " + str(share_record.get_share_related_records()))

                        # Get the SharedThrough instance of each ShareRecord
                        shared_through = share_record.get_shared_through()

                        # Check if sharedThrough is not null
                        if shared_through is not None:
                            # Get the Module instance of each ShareRecord
                            module = shared_through.get_module()

                            if module is not None:
                                # Get the ID of the Module
                                print("ShareRecord SharedThrough Module ID: " + str(module.get_id()))

                                # Get the Name of the Module
                                print("ShareRecord SharedThrough Module Name: " + str(module.get_name()))

                            # Get the ID of the SharedThrough
                            print("ShareRecord SharedThrough ID: " + str(shared_through.get_id()))

                        # Get the Permission of each ShareRecord
                        print("ShareRecord Permission: " + str(share_record.get_permission()))

                        # Get the SharedTime of each ShareRecord
                        print("ShareRecord SharedTime: " + str(share_record.get_shared_time()))

                        # Get the SharedBy User instance
                        shared_by = share_record.get_shared_by()

                        if shared_by is not None:
                            # Get the ID of the  User
                            print("ShareRecord SharedBy-ID: " + str(shared_by.get_id()))

                            # Get the FullName of the  User
                            print("ShareRecord SharedBy-FullName: " + shared_by.get_full_name())

                            # Get the Zuid of the  User
                            print("ShareRecord SharedBy-Zuid: " + str(shared_by.get_zuid()))

                        # Get the shared User instance of each ShareRecord
                        user = share_record.get_user()

                        if user is not None:
                            # Get the ID of the shared User
                            print("ShareRecord User-ID: " + str(user.get_id()))

                            # Get the FullName of the shared User
                            print("ShareRecord User-FullName: " + str(user.get_full_name()))

                            # Get the Zuid of the shared User
                            print("ShareRecord User-Zuid: " + str(user.get_zuid()))

                    # Get the list of obtained Shareable User instances
                    shareable_users = response_object.get_shareable_user()

                    if shareable_users is not None:
                        for shareable_user in shareable_users:
                            # Get the ID of the shareable User
                            print("Shareable User-ID: " + str(shareable_user.get_id()))

                            # Get the FullName of the shareable User
                            print("Shareable User-FullName: " + str(shareable_user.get_full_name()))

                            # Get the Zuid of the shareable User
                            print("Shareable User-Zuid: " + str(shareable_user.get_zuid()))

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
    def share_record(module_api_name, record_id):

        """
        This method is used to share the record and print the response.
        :param module_api_name: The API Name of the module to share record.
        :param record_id: The ID of the record to be shared
        """

        """
        example
        module_api_name = Contacts
        record_id = 3409643000002112011
        """

        # Get instance of ShareRecordsOperations Class that takes module_api_name and record_id as parameter
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold ShareRecord instances
        share_record_list = []

        # Get instance of ShareRecord Class
        share_record = ZCRMShareRecord()

        # Set boolean value to share related records
        share_record.set_share_related_records(True)

        # Set the permission. Possible values - full_access, read_only, read_write
        share_record.set_permission('read_write')

        # Get instance of User Class
        user = User()

        # Set User ID
        user.set_id(3409643000000302042)

        # Set the User instance to user
        share_record.set_user(user)

        # Add the instance to list
        share_record_list.append(share_record)

        # Set the list to share of BodyWrapper instance
        request.set_share(share_record_list)

        # Call share_record method that takes BodyWrapper instance as parameter
        response = shared_records_operations.share_record(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_share()

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
    def update_share_permissions(module_api_name, record_id):

        """
        This method is used to update the sharing permissions of a record granted to users as Read-Write, Read-only, or grant full access.
        :param module_api_name: The API Name of the module to update share permissions.
        :param record_id: The ID of the record
        """

        """
        example
        module_api_name = Contacts
        record_id = 3409643000002112011
        """

        # Get instance of ShareRecordsOperations Class that takes module_api_name and record_id as parameter
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold ShareRecord instances
        share_record_list = []

        # Get instance of ShareRecord Class
        share_record = ZCRMShareRecord()

        # Set boolean value to share related records
        share_record.set_share_related_records(True)

        # Set the permission. Possible values - full_access, read_only, read_write
        share_record.set_permission('full_access')

        # Get instance of User Class
        user = User()

        # Set User ID
        user.set_id(3409643000000302042)

        # Set the User instance to user
        share_record.set_user(user)

        # Add the instance to list
        share_record_list.append(share_record)

        # Set the list to share of BodyWrapper instance
        request.set_share(share_record_list)

        # Call update_share_permissions method that takes BodyWrapper instance as parameter
        response = shared_records_operations.update_share_permissions(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_share()

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
    def revoke_shared_record(module_api_name, record_id):

        """
        This method is used to revoke access to a shared record that was shared to users and print the response.
        :param module_api_name: The API Name of the module to revoke shared record.
        :param record_id: The ID of the record
        """

        """
        example
        module_api_name = Contacts
        record_id = 3409643000002112011
        """

        # Get instance of ShareRecordsOperations Class that takes module_api_name and record_id as parameter
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)

        # Call revoke_shared_record method
        response = shared_records_operations.revoke_shared_record()

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected DeleteActionWrapper instance is received.
                if isinstance(response_object, DeleteActionWrapper):

                    # Get the obtained ActionResponse instance
                    action_response = response_object.get_share()

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
