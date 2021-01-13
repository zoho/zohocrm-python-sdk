from zcrmsdk.src.com.zoho.crm.api.currencies import *
from zcrmsdk.src.com.zoho.crm.api.currencies import Currency as ZCRMCurrency
from zcrmsdk.src.com.zoho.crm.api.util import Choice


class Currency(object):

    @staticmethod
    def get_currencies():

        """
        This method is used to get all the available currencies in your organization.
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Call get_currencies method
        response = currencies_operations.get_currencies()

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

                    # Get the list of Currency instances
                    currencies_list = response_object.get_currencies()

                    for currency in currencies_list:

                        # Get the Id of each currency
                        print("Currency Id: " + str(currency.get_id()))

                        # Get the IsoCode of each currency
                        print("Currency IsoCode: " + str(currency.get_iso_code()))

                        # Get the Symbol of each currency
                        print("Currency Symbol: " + str(currency.get_symbol()))

                        # Get the CreatedTime of each currency
                        print("Currency CreatedTime: " + str(currency.get_created_time()))

                        # Get if the currency is active
                        print("Currency IsActive: " + str(currency.get_is_active()))

                        # Get the ExchangeRate of each currency
                        print("Currency ExchangeRate: " + str(currency.get_exchange_rate()))

                        # Get the format instance of each currency
                        format = currency.get_format()

                        if format is not None:
                            # Get the DecimalSeparator of the Format
                            print("Currency Format DecimalSeparator: " + format.get_decimal_separator().get_value())

                            # Get the ThousandSeparator of the Format
                            print("Currency Format ThousandSeparator: " + format.get_thousand_separator().get_value())

                            # Get the DecimalPlaces of the Format
                            print("Currency Format DecimalPlaces: " + format.get_decimal_places().get_value())

                        # Get the createdBy User instance of each currency
                        created_by = currency.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Currency Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Currency Created By - ID: " + str(created_by.get_id()))

                        # Get the modified_by User instance of each currency
                        modified_by = currency.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Currency Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Currency Modified By - ID: " + str(modified_by.get_id()))

                        # Get the PrefixSymbol of each currency
                        print("Currency PrefixSymbol: " + str(currency.get_prefix_symbol()))

                        # Get the IsBase of each currency
                        print("Currency IsBase: " + str(currency.get_is_base()))

                        # Get the ModifiedTime of each currency
                        print("Currency ModifiedTime: " + str(currency.get_modified_time()))

                        # Get the Name of each currency
                        print("Currency Name: " + currency.get_name())

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
    def get_currency(currency_id):

        """
        This method is used to get the details of a specific currency.
        :param currency_id: Specify the unique ID of the currency.
        """

        """
        example
        currency_id = 3409643000002293037
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Call get_currency method that takes currency_id as parameter
        response = currencies_operations.get_currency(currency_id)

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

                    # Get the list of Currency instances
                    currencies_list = response_object.get_currencies()

                    for currency in currencies_list:

                        # Get the Id of each currency
                        print("Currency Id: " + str(currency.get_id()))

                        # Get the IsoCode of each currency
                        print("Currency IsoCode: " + str(currency.get_iso_code()))

                        # Get the Symbol of each currency
                        print("Currency Symbol: " + str(currency.get_symbol()))

                        # Get the CreatedTime of each currency
                        print("Currency CreatedTime: " + str(currency.get_created_time()))

                        # Get if the currency is active
                        print("Currency IsActive: " + str(currency.get_is_active()))

                        # Get the ExchangeRate of each currency
                        print("Currency ExchangeRate: " + str(currency.get_exchange_rate()))

                        # Get the format instance of each currency
                        format = currency.get_format()

                        if format is not None:
                            # Get the DecimalSeparator of the Format
                            print("Currency Format DecimalSeparator: " + format.get_decimal_separator().get_value())

                            # Get the ThousandSeparator of the Format
                            print("Currency Format ThousandSeparator: " + format.get_thousand_separator().get_value())

                            # Get the DecimalPlaces of the Format
                            print("Currency Format DecimalPlaces: " + format.get_decimal_places().get_value())

                        # Get the createdBy User instance of each currency
                        created_by = currency.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Currency Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Currency Created By - ID: " + str(created_by.get_id()))

                        # Get the createdBy User instance of each currency
                        modified_by = currency.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Currency Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Currency Modified By - ID: " + str(modified_by.get_id()))

                        # Get the PrefixSymbol of each currency
                        print("Currency PrefixSymbol: " + str(currency.get_prefix_symbol()))

                        # Get the IsBase of each currency
                        print("Currency IsBase: " + str(currency.get_is_base()))

                        # Get the ModifiedTime of each currency
                        print("Currency ModifiedTime: " + str(currency.get_modified_time()))

                        # Get the Name of each currency
                        print("Currency Name: " + currency.get_name())

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
    def add_currencies():

        """
        This method is used to add new currencies to your organization.
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Currency instances
        currencies_list = []

        # Get instance of Currency Class
        currency = ZCRMCurrency()

        # To set the position of the ISO code in the currency.
        # True: Display ISO code before the currency value.
        # False: Display ISO code after the currency value.
        currency.set_prefix_symbol(True)

        # To set the name of the currency.
        currency.set_name("Angolan Kwanza - AOA")

        # To set the ISO code of the currency.
        currency.set_iso_code("AOA")

        # To set the symbol of the currency.
        currency.set_symbol("Kz")

        # To set the rate at which the currency has to be exchanged for home currency.
        currency.set_exchange_rate("20.000000000")

        # To set the status of the currency.
        # True: The currency is active.
        # False: The currency is inactive.
        currency.set_is_active(True)

        format = Format()

        # It can be a Period or Comma, depending on the currency.
        format.set_decimal_separator(Choice('Period'))

        # It can be a Period, Comma, or Space, depending on the currency.
        format.set_thousand_separator(Choice('Comma'))

        # To set the number of decimal places allowed for the currency. It can be 0, 2, or 3.
        format.set_decimal_places(Choice('2'))

        # To set the format of the currency
        currency.set_format(format)

        currencies_list.append(currency)

        # Set the list to Currency in BodyWrapper instance
        request.set_currencies(currencies_list)

        # Call add_currencies method that takes BodyWrapper instance as parameter
        response = currencies_operations.add_currencies(request)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the obtained ActionResponse instances
                    action_response_list = response_object.get_currencies()

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
    def update_currencies():

        """
        This method is used to update currency details.
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Currency instances
        currencies_list = []

        # Get instance of Currency Class
        currency = ZCRMCurrency()

        # To set currency Id
        currency.set_id(3409643000002293037)

        # To set the position of the ISO code in the currency.
        # True: Display ISO code before the currency value.
        # False: Display ISO code after the currency value.
        currency.set_prefix_symbol(True)

        # To set the rate at which the currency has to be exchanged for home currency.
        currency.set_exchange_rate("28.000000000")

        # To set the status of the currency.
        # True: The currency is active.
        # False: The currency is inactive.
        currency.set_is_active(True)

        format = Format()

        # It can be a Period or Comma, depending on the currency.
        format.set_decimal_separator(Choice('Period'))

        # It can be a Period, Comma, or Space, depending on the currency.
        format.set_thousand_separator(Choice('Comma'))

        # To set the number of decimal places allowed for the currency. It can be 0, 2, or 3.
        format.set_decimal_places(Choice('2'))

        # To set the format of the currency
        currency.set_format(format)

        currencies_list.append(currency)

        # Set the list to Currency in BodyWrapper instance
        request.set_currencies(currencies_list)

        # Call update_currencies method that takes BodyWrapper instance as parameter
        response = currencies_operations.update_currencies(request)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the obtained ActionResponse instances
                    action_response_list = response_object.get_currencies()

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
    def update_currency(currency_id):

        """
        This method is used to update single currency details.
        :param currency_id: Specify the unique ID of the currency.
        """

        """
        example
        currency_id = 3409643000002293037
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Currency instances
        currencies_list = []

        # Get instance of Currency Class
        currency = ZCRMCurrency()

        # To set the position of the ISO code in the currency.
        # True: Display ISO code before the currency value.
        # False: Display ISO code after the currency value.
        currency.set_prefix_symbol(True)

        # To set the rate at which the currency has to be exchanged for home currency.
        currency.set_exchange_rate("28.000000000")

        # To set the status of the currency.
        # True: The currency is active.
        # False: The currency is inactive.
        currency.set_is_active(True)

        format = Format()

        # It can be a Period or Comma, depending on the currency.
        format.set_decimal_separator(Choice('Period'))

        # It can be a Period, Comma, or Space, depending on the currency.
        format.set_thousand_separator(Choice('Comma'))

        # To set the number of decimal places allowed for the currency. It can be 0, 2, or 3.
        format.set_decimal_places(Choice('2'))

        # To set the format of the currency
        currency.set_format(format)

        currencies_list.append(currency)

        # Set the list to Currency in BodyWrapper instance
        request.set_currencies(currencies_list)

        # Call update_currency method that takes BodyWrapper instance and currency_id as parameters
        response = currencies_operations.update_currency(currency_id, request)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the obtained ActionResponse instances
                    action_response_list = response_object.get_currencies()

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
    def enable_multiple_currencies():

        """
        This method is used to enable multiple currencies for your organization.
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Get instance of BaseCurrencyWrapper Class that will contain the request body
        request = BaseCurrencyWrapper()

        # Get instance of Currency Class
        currency = ZCRMCurrency()

        # To set the position of the ISO code in the currency.
        # True: Display ISO code before the currency value.
        # False: Display ISO code after the currency value.
        currency.set_prefix_symbol(True)

        # To set the name of the currency.
        currency.set_name("Algerian Dinar-ADN")

        # To set the ISO code of the currency.
        currency.set_iso_code("DZD")

        # To set the symbol of the currency.
        currency.set_symbol("Af")

        # To set the rate at which the currency has to be exchanged for home currency.
        currency.set_exchange_rate("1.000000000")

        # To set the status of the currency.
        # True: The currency is active.
        # False: The currency is inactive.
        currency.set_is_active(True)

        format = Format()

        # It can be a Period or Comma, depending on the currency.
        format.set_decimal_separator(Choice('Period'))

        # It can be a Period, Comma, or Space, depending on the currency.
        format.set_thousand_separator(Choice('Comma'))

        # To set the number of decimal places allowed for the currency. It can be 0, 2, or 3.
        format.set_decimal_places(Choice('2'))

        # To set the format of the currency
        currency.set_format(format)

        # Set the Currency in BodyWrapper instance
        request.set_base_currency(currency)

        # Call enable_multiple_currencies method that takes BaseCurrencyWrapper instance as parameter
        response = currencies_operations.enable_multiple_currencies(request)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, BaseCurrencyActionWrapper):

                    # Get the obtained ActionResponse instances
                    action_response = response_object.get_base_currency()

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
    def update_base_currency():

        """
        This method is used to update base currency details.
        """

        # Get instance of CurrenciesOperations Class
        currencies_operations = CurrenciesOperations()

        # Get instance of BaseCurrencyWrapper Class that will contain the request body
        request = BaseCurrencyWrapper()

        # Get instance of Currency Class
        currency = ZCRMCurrency()

        # To set currency Id
        currency.set_id(3409643000002293001)

        # To set the position of the ISO code in the currency.
        # True: Display ISO code before the currency value.
        # False: Display ISO code after the currency value.
        currency.set_prefix_symbol(True)

        # To set the symbol of the currency.
        currency.set_symbol("Af")

        # To set the rate at which the currency has to be exchanged for home currency.
        currency.set_exchange_rate("1.000000000")

        # To set the status of the currency.
        # True: The currency is active.
        # False: The currency is inactive.
        currency.set_is_active(True)

        format = Format()

        # It can be a Period or Comma, depending on the currency.
        format.set_decimal_separator(Choice('Period'))

        # It can be a Period, Comma, or Space, depending on the currency.
        format.set_thousand_separator(Choice('Comma'))

        # To set the number of decimal places allowed for the currency. It can be 0, 2, or 3.
        format.set_decimal_places(Choice('3'))

        # To set the format of the currency
        currency.set_format(format)

        # Set the Currency in BodyWrapper instance
        request.set_base_currency(currency)

        # Call update_base_currency method that takes BaseCurrencyWrapper instance as parameter
        response = currencies_operations.update_base_currency(request)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected BaseCurrencyActionWrapper instance is received.
                if isinstance(response_object, BaseCurrencyActionWrapper):

                    # Get the obtained ActionResponse instance
                    action_response = response_object.get_base_currency()

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



