from zcrmsdk.src.com.zoho.crm.api.roles import *


class Role(object):

    @staticmethod
    def get_roles():

        """
        This method is used to retrieve the data of roles through an API request and print the response.
        """

        # Get instance of RolesOperations Class
        roles_operations = RolesOperations()

        # Call get_roles method
        response = roles_operations.get_roles()

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

                    # Get the list of obtained Role instances
                    roles_list = response_object.get_roles()

                    for role in roles_list:
                        # Get the DisplayLabel of each Role
                        print("Role DisplayLabel: " + str(role.get_display_label()))

                        # Get the forecastManager User instance of each Role
                        forecast_manager = role.get_forecast_manager()

                        # Check if forecastManager is not None
                        if forecast_manager is not None:

                            # Get the ID of the forecast Manager
                            print("Role Forecast Manager User-ID: " + str(forecast_manager.get_id()))

                            # Get the name of the forecast Manager
                            print("Role Forecast Manager User-Name: " + str(forecast_manager.get_name()))

                        # Get the ShareWithPeers of each Role
                        print("Role ShareWithPeers: " + str(role.get_share_with_peers()))

                        # Get the Name of each Role
                        print("Role Name: " + role.get_name())

                        # Get the Description of each Role
                        print("Role Description: " + str(role.get_description()))

                        # Get the Id of each Role
                        print("Role ID: " + str(role.get_id()))

                        # Get the reporting_to User instance of each Role
                        reporting_to = role.get_reporting_to()

                        # Check if reporting_to is not None
                        if reporting_to is not None:
                            # Get the ID of the reporting_to User
                            print("Role ReportingTo User-ID: " + str(reporting_to.get_id()))

                            # Get the name of the reporting_to User
                            print("Role ReportingTo User-Name: " + str(reporting_to.get_name()))

                        # Get the AdminUser of each Role
                        print("Role AdminUser: " + str(role.get_admin_user()))

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
    def get_role(role_id):

        """
        This method is used to retrieve the data of single role with ID and print the response.
        :param role_id: The ID of the role to be obtained
        """

        """
        example
        role_id = 3409643000000026005
        """

        # Get instance of RolesOperations Class
        roles_operations = RolesOperations()

        # Call get_role method that takes role_id as parameter
        response = roles_operations.get_role(role_id)

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

                    # Get the list of obtained Role instances
                    roles_list = response_object.get_roles()

                    for role in roles_list:
                        # Get the DisplayLabel of each Role
                        print("Role DisplayLabel: " + role.get_display_label())

                        # Get the forecastManager User instance of each Role
                        forecast_manager = role.get_forecast_manager()

                        # Check if forecastManager is not None
                        if forecast_manager is not None:

                            # Get the ID of the forecast Manager
                            print("Role Forecast Manager User-ID: " + str(forecast_manager.get_id()))

                            # Get the name of the forecast Manager
                            print("Role Forecast Manager User-Name: " + forecast_manager.get_name())

                        # Get the ShareWithPeers of each Role
                        print("Role ShareWithPeers: " + str(role.get_share_with_peers()))

                        # Get the Name of each Role
                        print("Role Name: " + role.get_name())

                        # Get the Description of each Role
                        print("Role Description: " + role.get_description())

                        # Get the Id of each Role
                        print("Role ID: " + str(role.get_id()))

                        # Get the reporting_to User instance of each Role
                        reporting_to = role.get_reporting_to()

                        # Check if reporting_to is not None
                        if reporting_to is not None:
                            # Get the ID of the reporting_to User
                            print("Role ReportingTo User-ID: " + str(reporting_to.get_id()))

                            # Get the name of the reporting_to User
                            print("Role ReportingTo User-Name: " + reporting_to.get_name())

                        # Get the AdminUser of each Role
                        print("Role AdminUser: " + str(role.get_admin_user()))

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
