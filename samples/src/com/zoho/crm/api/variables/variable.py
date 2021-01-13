from zcrmsdk.src.com.zoho.crm.api.variables import *
from zcrmsdk.src.com.zoho.crm.api.variables import Variable as ZCRMVariable
from zcrmsdk.src.com.zoho.crm.api.variable_groups import VariableGroup
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Variable(object):

    @staticmethod
    def get_variables():

        """
        This method is used to retrieve all the available variables through an API request and print the response.
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get Variables operation
        param_instance.add(GetVariablesParam.group, 'General')

        # Call get_variables method that takes ParameterMap instance as parameter
        response = variables_operations.get_variables(param_instance)

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

                    # Get the list of obtained Variable instances
                    variable_list = response_object.get_variables()

                    for variable in variable_list:
                        # Get the ID of each Variable
                        print("Variable ID: " + str(variable.get_id()))

                        # Get the APIName of each Variable
                        print("Variable APIName: " + variable.get_api_name())

                        # Get the Name of each Variable
                        print("Variable Name: " + variable.get_name())

                        # Get the Description of each Variable
                        print("Variable Description: " + variable.get_description())

                        # Get the Type of each Variable
                        print("Variable Type: " + variable.get_type())

                        # Get the VariableGroup instance of each Variable
                        variable_group = variable.get_variable_group()

                        if variable_group is not None:
                            # Get the APIName of the VariableGroup
                            print("Variable VariableGroup APIName: " + variable_group.get_api_name())

                            # Get the ID of the VariableGroup
                            print("Variable VariableGroup ID: " + str(variable_group.get_id()))

                        # Get the Value of each Variable
                        print("Variable Value: " + variable.get_value())

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
    def get_variable_by_id(variable_id):

        """
        This method is used to get the details of any specific variable with ID and print the response
        :param variable_id: The ID of the Variable to be obtained
        """

        """
        example
        variable_id = 3409643000002275025
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get Variable By ID operation
        param_instance.add(GetVariableByIDParam.group, '3409643000002275023')

        # Call get_variable_by_id method that takes ParameterMap instance and variable_id as parameters
        response = variables_operations.get_variable_by_id(variable_id, param_instance)

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

                    # Get the list of obtained Variable instances
                    variable_list = response_object.get_variables()

                    for variable in variable_list:
                        # Get the ID of each Variable
                        print("Variable ID: " + str(variable.get_id()))

                        # Get the APIName of each Variable
                        print("Variable APIName: " + variable.get_api_name())

                        # Get the Name of each Variable
                        print("Variable Name: " + variable.get_name())

                        # Get the Description of each Variable
                        print("Variable Description: " + variable.get_description())

                        # Get the Type of each Variable
                        print("Variable Type: " + variable.get_type())

                        # Get the VariableGroup instance of each Variable
                        variable_group = variable.get_variable_group()

                        if variable_group is not None:
                            # Get the APIName of the VariableGroup
                            print("Variable VariableGroup APIName: " + variable_group.get_api_name())

                            # Get the ID of the VariableGroup
                            print("Variable VariableGroup ID: " + variable_group.get_id())

                        # Get the Value of each Variable
                        print("Variable Value: " + variable.get_value())

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
    def get_variable_for_api_name(variable_api_name):

        """
        This method is used to get the details of any specific variable with API Name
        :param variable_api_name: The API name of the Variable to be obtained
        """

        """
        example
        variable_api_name = 'Variable55'
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get Variable For API Name operation
        param_instance.add(GetVariableForAPINameParam.group, '3409643000002275023')

        # Call get_variable_for_api_name method that takes ParameterMap instance and variable_api_name as parameters
        response = variables_operations.get_variable_for_api_name(variable_api_name, param_instance)

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

                    # Get the list of obtained Variable instances
                    variable_list = response_object.get_variables()

                    for variable in variable_list:
                        # Get the ID of each Variable
                        print("Variable ID: " + str(variable.get_id()))

                        # Get the APIName of each Variable
                        print("Variable APIName: " + variable.get_api_name())

                        # Get the Name of each Variable
                        print("Variable Name: " + variable.get_name())

                        # Get the Description of each Variable
                        print("Variable Description: " + variable.get_description())

                        # Get the Type of each Variable
                        print("Variable Type: " + variable.get_type())

                        # Get the VariableGroup instance of each Variable
                        variable_group = variable.get_variable_group()

                        if variable_group is not None:
                            # Get the APIName of the VariableGroup
                            print("Variable VariableGroup APIName: " + variable_group.get_api_name())

                            # Get the ID of the VariableGroup
                            print("Variable VariableGroup ID: " + variable_group.get_id())

                        # Get the Value of each Variable
                        print("Variable Value: " + variable.get_value())

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
    def create_variables():

        """
        This method is used to create variables and print the response.
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Variable instances
        variable_list = []

        # Get instance of Variable Class
        variable_1 = ZCRMVariable()

        # Set the API name to variable
        variable_1.set_api_name('Variable1234')

        # Set the name to variable
        variable_1.set_name('Variable1234')

        # Get instance of VariableGroup Class
        variable_group = VariableGroup()

        # Set ID to variable_group
        variable_group.set_id(3409643000002275023)

        # Set the VariableGroup to Variable instance
        variable_1.set_variable_group(variable_group)

        # Set the type to Variable
        variable_1.set_type('integer')

        # Set the value
        variable_1.set_value('55')

        variable_1.set_description('This denotes variable 5 description')

        # Add the variable instance to the array
        variable_list.append(variable_1)

        # Get instance of Variable Class
        variable_2 = ZCRMVariable()

        # Set the API name to variable
        variable_2.set_api_name('Variablenew1')

        # Set the name to variable
        variable_2.set_name('Variablenew1')

        # Get instance of VariableGroup Class
        variable_group = VariableGroup()

        # Set ID to variable_group
        # variable_group.set_id(3409643000002275023)

        variable_group.set_name("New VG")

        # Set the VariableGroup to Variable instance
        variable_2.set_variable_group(variable_group)

        # Set the type to Variable
        variable_2.set_type('text')

        # Set the value
        variable_2.set_value('Python')

        variable_2.set_description('This denotes variable 5 description')

        # Add the variable instance to the array
        variable_list.append(variable_2)

        # Set the list to variables in BodyWrapper instance
        request.set_variables(variable_list)

        # Call create_variables method that takes BodyWrapper instance as parameter
        response = variables_operations.create_variables(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_variables()

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
    def update_variables():

        """
        This method is used to update details of variables in CRM and print the response.
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Variable instances
        variable_list = []

        # Get instance of Variable Class
        variable_1 = ZCRMVariable()

        # Set the ID
        variable_1.set_id(3409643000002275025)

        # Set the value
        variable_1.set_value('50')

        # Add the variable instance to the array
        variable_list.append(variable_1)

        # Get instance of Variable Class
        variable_2 = ZCRMVariable()

        # Set the ID
        variable_2.set_id(3409643000002275035)

        variable_2.set_description('This is a new description')

        # Add the variable instance to the array
        variable_list.append(variable_2)

        # Set the list to variables in BodyWrapper instance
        request.set_variables(variable_list)

        # Call update_variables method that takes BodyWrapper instance as parameter
        response = variables_operations.update_variables(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_variables()

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
    def update_variable_by_id(variable_id):

        """
        This method is used to update details of a specific variable in CRM and print the response.
        :param variable_id: The ID of the Variable to be updated
        :return:
        """

        """
        example
        variable_id = 3409643000002275025
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Variable instances
        variable_list = []

        # Get instance of Variable Class
        variable_1 = ZCRMVariable()

        # Set the value
        variable_1.set_value('98')

        # Add the variable instance to the array
        variable_list.append(variable_1)

        # Set the list to variables in BodyWrapper instance
        request.set_variables(variable_list)

        # Call update_variable_by_id method that takes BodyWrapper instance and variable_id as parameters
        response = variables_operations.update_variable_by_id(variable_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_variables()

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
    def update_variable_by_api_name(variable_api_name):

        """
        This method is used to update details of a specific variable in CRM with API Name and print the response.
        :param variable_api_name: The API name of the Variable to be updated
        """

        """
        example
        variable_api_name = 'Variable55'
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Variable instances
        variable_list = []

        # Get instance of Variable Class
        variable_1 = ZCRMVariable()

        # Set the value
        variable_1.set_value('98')

        # Set the API Name
        variable_1.set_api_name('Edited-variable55')

        # Add the variable instance to the array
        variable_list.append(variable_1)

        # Set the list to variables in BodyWrapper instance
        request.set_variables(variable_list)

        # Call update_variable_by_api_name method that takes BodyWrapper instance and variable_api_name as parameters
        response = variables_operations.update_variable_by_api_name(variable_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_variables()

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
    def delete_variable(variable_id):

        """
        This method is used to delete details of a specific variable in CRM and print the response.
        :param variable_id: The ID of the Variable to be deleted
        """

        """
        example
        variable_id = 3409643000002275025
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Call delete_variable method that takes variable_id as parameter
        response = variables_operations.delete_variable(variable_id)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_variables()

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
    def delete_variables(variable_ids):

        """
        This method is used to delete details of multiple variables in CRM simultaneously and print the response.
        :param variable_ids: The list of Variable IDs to be deleted
        """

        """
        example
        variable_ids = [3409643000002275025, 3409643000002275035]
        """

        # Get instance of VariablesOperations Class
        variables_operations = VariablesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Delete Variables operation
        for variable_id in variable_ids:
            param_instance.add(DeleteVariablesParam.ids, variable_id)

        # Call delete_variables method that takes ParameterMap instance as parameter
        response = variables_operations.delete_variables(param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_variables()

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


