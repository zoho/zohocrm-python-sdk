from zcrmsdk.src.com.zoho.crm.api.taxes import *
from zcrmsdk.src.com.zoho.crm.api.taxes import Tax as ZCRMTax
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Tax(object):

    @staticmethod
    def get_taxes():

        """
        This method is used to get all the Organization Taxes and print the response.
        """

        # Get instance of TaxesOperations Class
        taxes_operations = TaxesOperations()

        # Call get_taxes method
        response = taxes_operations.get_taxes()

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

                    # Get the list of obtained Tax instances
                    taxes_list = response_object.get_taxes()

                    for tax in taxes_list:
                        # Get the DisplayLabel of each Tax
                        print("Tax DisplayLabel: " + tax.get_display_label())

                        # Get the Name of each Tax
                        print("Tax Name: " + tax.get_name())

                        # Get the ID of each Tax
                        print("Tax ID: " + str(tax.get_id()))

                        # Get the Value of each Tax
                        print("Tax Value: " + str(tax.get_value()))

                    preference = response_object.get_preference()

                    if preference is not None:
                        # Get the AutoPopulateTax of each Preference
                        print("Preference AutoPopulateTax: " + str(preference.get_auto_populate_tax()))

                        # Get the ModifyTaxRates of each Preference
                        print("Preference ModifyTaxRates: " + str(preference.get_modify_tax_rates()))

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
    def get_tax(tax_id):

        """
        This method is used to get the Organization Tax with ID and print the response.
        :param tax_id: The ID of the tax to be obtained
        """

        """
        example
        tax_id = 3409643000002317003
        """

        # Get instance of TaxesOperations Class
        taxes_operations = TaxesOperations()

        # Call get_tax method that takes tax_id as parameter
        response = taxes_operations.get_tax(tax_id)

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

                    # Get the list of obtained Tax instances
                    taxes_list = response_object.get_taxes()

                    for tax in taxes_list:
                        # Get the DisplayLabel of each Tax
                        print("Tax DisplayLabel: " + tax.get_display_label())

                        # Get the Name of each Tax
                        print("Tax Name: " + tax.get_name())

                        # Get the ID of each Tax
                        print("Tax ID: " + str(tax.get_id()))

                        # Get the Value of each Tax
                        print("Tax Value: " + str(tax.get_value()))

                    preference = response_object.get_preference()

                    if preference is not None:
                        # Get the AutoPopulateTax of each Preference
                        print("Preference AutoPopulateTax: " + str(preference.get_auto_populate_tax()))

                        # Get the ModifyTaxRates of each Preference
                        print("Preference ModifyTaxRates: " + str(preference.get_modify_tax_rates()))

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
    def create_taxes():

        """
        This method is used to create Organization Taxes and print the response.
        """

        # Get instance of TaxesOperations Class
        taxes_operations = TaxesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Tax instances
        tax_list = []

        # Get instance of Tax Class
        tax_1 = ZCRMTax()

        # Set Name
        tax_1.set_name('MyTax123')

        # Set sequence number
        tax_1.set_sequence_number(2)

        # Set value
        tax_1.set_value(10.0)

        # Add the instance to list
        tax_list.append(tax_1)

        # Get instance of Tax Class
        tax_2 = ZCRMTax()

        # Set Name
        tax_2.set_name('MyTax1234')

        # Set sequence number
        tax_2.set_sequence_number(3)

        # Set value
        tax_2.set_value(11.0)

        # Add the instance to list
        tax_list.append(tax_2)

        # Set the list to taxes in BodyWrapper instance
        request.set_taxes(tax_list)

        # Call create_taxes method that takes BodyWrapper class instance as parameter
        response = taxes_operations.create_taxes(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_taxes()

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
    def update_taxes():

        """
        This method is used to update Organization Taxes and print the response.
        """

        # Get instance of TaxesOperations Class
        taxes_operations = TaxesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Tax instances
        tax_list = []

        # Get instance of Tax Class
        tax_1 = ZCRMTax()

        # Set ID
        tax_1.set_id(3409643000002317003)

        # Set Name
        tax_1.set_name('Modified - MyTax22')

        # Set sequence number
        tax_1.set_sequence_number(2)

        # Set value
        tax_1.set_value(10.0)

        # Add the instance to list
        tax_list.append(tax_1)

        # Get instance of Tax Class
        tax_2 = ZCRMTax()

        # Set ID
        tax_2.set_id(3409643000002317004)

        # Set Name
        tax_2.set_name('Modified - MyTax33')

        # Set sequence number
        tax_2.set_sequence_number(4)

        # Set value
        tax_2.set_value(12.0)

        # Add the instance to list
        tax_list.append(tax_2)

        # Set the list to taxes in BodyWrapper instance
        request.set_taxes(tax_list)

        # Call update_taxes method that takes BodyWrapper class instance as parameter
        response = taxes_operations.update_taxes(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_taxes()

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
    def delete_taxes(tax_ids):

        """
        This method is used to delete Organization Taxes and print the response.
        :param tax_ids: The List of the tax IDs to be deleted
        :return:
        """

        """
        example
        tax_ids = [3409643000002407046, 3409643000002407047]
        """

        # Get instance of TaxesOperations Class
        taxes_operations = TaxesOperations()

        # Get instance of TaxesOperations Class
        param_instance = ParameterMap()

        # Possible parameters for Delete Taxes operation
        for tax_id in tax_ids:
            param_instance.add(DeleteTaxesParam.ids, tax_id)

        # Call delete_taxes method that takes ParameterMap instance as parameter
        response = taxes_operations.delete_taxes(param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_taxes()

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
    def delete_tax(tax_id):

        """
        This method is used to delete Organization Tax and print the response.
        :param tax_id: The ID of the tax to be deleted
        """

        """
        example
        tax_id = 3409643000002407046
        """

        # Get instance of TaxesOperations Class
        taxes_operations = TaxesOperations()

        # Call delete_tax method that takes tax_id as parameter
        response = taxes_operations.delete_tax(tax_id)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_taxes()

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
