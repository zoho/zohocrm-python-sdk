from zcrmsdk.src.com.zoho.crm.api.variable_groups import *


class VariableGroup(object):

    @staticmethod
    def get_variable_groups():

        """
        This method is used to get the details of all the variable groups and print the response.
        """

        # Get instance of VariableGroupsOperations Class
        variable_groups_operations = VariableGroupsOperations()

        # Call get_variable_groups method
        response = variable_groups_operations.get_variable_groups()

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

                    # Get the list of obtained VariableGroup instances
                    variablegroup_list = response_object.get_variable_groups()

                    for variable_group in variablegroup_list:
                        # Get the DisplayLabel of each VariableGroup
                        print("VariableGroup DisplayLabel: " + str(variable_group.get_display_label()))

                        # Get the APIName of each VariableGroup
                        print("VariableGroup APIName: " + str(variable_group.get_api_name()))

                        # Get the Name of each VariableGroup
                        print("VariableGroup Name: " + str(variable_group.get_name()))

                        # Get the Description of each VariableGroup
                        print("VariableGroup Description: " + str(variable_group.get_description()))

                        # Get the ID of each VariableGroup
                        print("VariableGroup ID: " + str(variable_group.get_id()))

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
    def get_variable_group_by_id(variable_group_id):

        """
        This method is used to get the details of any variable group with group id and print the response.
        :param variable_group_id: The ID of the VariableGroup to be obtained
        """

        """
        example
        variable_group_id = 3409643000002275023
        """

        # Get instance of VariableGroupsOperations Class
        variable_groups_operations = VariableGroupsOperations()

        # Call get_variable_group_by_id method that takes variable_group_id as parameter
        response = variable_groups_operations.get_variable_group_by_id(variable_group_id)

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

                    # Get the list of obtained VariableGroup instances
                    variablegroup_list = response_object.get_variable_groups()

                    for variable_group in variablegroup_list:
                        # Get the DisplayLabel of each VariableGroup
                        print("VariableGroup DisplayLabel: " + str(variable_group.get_display_label()))

                        # Get the APIName of each VariableGroup
                        print("VariableGroup APIName: " + str(variable_group.get_api_name()))

                        # Get the Name of each VariableGroup
                        print("VariableGroup Name: " + str(variable_group.get_name()))

                        # Get the Description of each VariableGroup
                        print("VariableGroup Description: " + str(variable_group.get_description()))

                        # Get the ID of each VariableGroup
                        print("VariableGroup ID: " + str(variable_group.get_id()))

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
    def get_variable_group_by_api_name(variable_group_api_name):

        """
        This method is used to get the details of any variable group with group API name and print the response.
        :param variable_group_api_name: The API Name of the VariableGroup to be obtained
        """

        """
        example
        variable_group_api_name = 'General'
        """

        # Get instance of VariableGroupsOperations Class
        variable_groups_operations = VariableGroupsOperations()

        # Call get_variable_group_by_api_name method that takes variable_group_api_name as parameter
        response = variable_groups_operations.get_variable_group_by_api_name(variable_group_api_name)

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

                    # Get the list of obtained VariableGroup instances
                    variablegroup_list = response_object.get_variable_groups()

                    for variable_group in variablegroup_list:
                        # Get the DisplayLabel of each VariableGroup
                        print("VariableGroup DisplayLabel: " + str(variable_group.get_display_label()))

                        # Get the APIName of each VariableGroup
                        print("VariableGroup APIName: " + str(variable_group.get_api_name()))

                        # Get the Name of each VariableGroup
                        print("VariableGroup Name: " + str(variable_group.get_name()))

                        # Get the Description of each VariableGroup
                        print("VariableGroup Description: " + str(variable_group.get_description()))

                        # Get the ID of each VariableGroup
                        print("VariableGroup ID: " + str(variable_group.get_id()))

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
