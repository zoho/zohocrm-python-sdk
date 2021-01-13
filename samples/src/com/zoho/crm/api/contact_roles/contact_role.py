from zcrmsdk.src.com.zoho.crm.api.contact_roles import *
from zcrmsdk.src.com.zoho.crm.api.contact_roles import ContactRole as ZCRMContactRole
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class ContactRole(object):

    @staticmethod
    def get_contact_roles():

        """
        This method is used to get all the Contact Roles and print the response.
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Call get_contact_roles method
        response = contact_roles_operations.get_contact_roles()

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

                    # Get the list of ContactRole instances
                    contact_roles_list = response_object.get_contact_roles()

                    for contact_role in contact_roles_list:

                        # Get the ID of each ContactRole
                        print("ID: " + str(contact_role.get_id()))

                        # Get the name of each ContactRole
                        print("Name: " + str(contact_role.get_name()))

                        # Get the sequence number of each ContactRole
                        print("Sequence Number: " + str(contact_role.get_sequence_number()))

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
    def get_contact_role(contact_role_id):

        """
        This method is used to get single Contact Role with ID and print the response.
        :param contact_role_id: The ID of the ContactRole to be obtained
        """

        """
        example
		contact_role_id = 3409643000002212003
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Call get_contact_role method that takes contact_role_id as parameter
        response = contact_roles_operations.get_contact_role(contact_role_id)

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
                    contact_roles_list = response_object.get_contact_roles()

                    for contact_role in contact_roles_list:
                        # Get the ID of each ContactRole
                        print("ID: " + str(contact_role.get_id()))

                        # Get the name of each ContactRole
                        print("Name: " + str(contact_role.get_name()))

                        # Get the sequence number of each ContactRole
                        print("Sequence Number: " + str(contact_role.get_sequence_number()))

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
    def create_contact_roles():

        """
        This method is used to create Contact Roles and print the response.
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold ContactRole instances
        contact_roles_list = []

        for i in range(0, 3):

            # Get instance of ContactRole Class
            contact_role = ZCRMContactRole()

            # Set name of the Contact Role
            contact_role.set_name("contactRole-py" + str(i))

            # Set sequence number of the Contact Role
            contact_role.set_sequence_number(i)

            # Add ContactRole instance to the array
            contact_roles_list.append(contact_role)

        # Set the list of contactRoles in BodyWrapper instance
        request.set_contact_roles(contact_roles_list)

        # Call create_contact_roles method that takes BodyWrapper instance as parameter
        response = contact_roles_operations.create_contact_roles(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()

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
    def update_contact_roles():

        """
        This method is used to update Contact Roles and print the response.
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold ContactRole instances
        contact_roles_list = []

        # Get instance of ContactRole Class
        cr_1 = ZCRMContactRole()

        # Set ID to the ContactRole instance
        cr_1.set_id(3409643000001792004)

        # Set name to the ContactRole instance
        cr_1.set_name("Edited12")

        contact_roles_list.append(cr_1)

        # Get instance of ContactRole Class
        cr_2 = ZCRMContactRole()

        # Set ID to the ContactRole instance
        cr_2.set_id(3409643000001794001)

        # Set name to the ContactRole instance
        cr_2.set_name("Edited1")

        contact_roles_list.append(cr_2)

        # Set the list to contactRoles in BodyWrapper instance
        request.set_contact_roles(contact_roles_list)

        # Call update_contact_roles method that takes BodyWrapper instance as parameter
        response = contact_roles_operations.update_contact_roles(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()

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
    def delete_contact_roles(contact_role_ids):

        """
        This method is used to delete Contact Roles and print the response.
        :param contact_role_ids: The list of ContactRole IDs to be deleted.
        """

        """
        example
        contact_role_ids = [3409643000002157002, 3409643000001619001, 3409643000000006883]
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Add ids to ParameterMap instance
        for contact_role_id in contact_role_ids:
            param_instance.add(DeleteContactRolesParam.ids, contact_role_id)

        # Call delete_contact_roles method that takes ParameterMap instance as parameter
        response = contact_roles_operations.delete_contact_roles(param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()

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
    def update_contact_role(contact_role_id):

        """
        This method is used to update single Contact Role with ID and print the response.
        :param contact_role_id: The ID of the ContactRole to be updated
        """

        """
        example
        contact_role_id = 3409643000002212003
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold ContactRole instances
        contact_roles_list = []

        # Get instance of ContactRole Class
        cr_1 = ZCRMContactRole()

        # Set name to the ContactRole instance
        cr_1.set_name("Edited1")

        contact_roles_list.append(cr_1)

        # Set the list to contactRoles in BodyWrapper instance
        request.set_contact_roles(contact_roles_list)

        # Call update_contact_role method that takes BodyWrapper instance and contact_role_id as parameters
        response = contact_roles_operations.update_contact_role(contact_role_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()

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
    def delete_contact_role(contact_role_id):

        """
        This method is used to delete single Contact Role with ID and print the response.
        :param contact_role_id: ID of the ContactRole to be deleted
        """

        """
        example
        contact_role_id = 3409643000002212003
        """

        # Get instance of ContactRolesOperations Class
        contact_roles_operations = ContactRolesOperations()

        # Call delete_contact_role which takes contact_role_id as parameter
        response = contact_roles_operations.delete_contact_role(contact_role_id)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()

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