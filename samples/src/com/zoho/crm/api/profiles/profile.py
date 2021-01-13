from zcrmsdk.src.com.zoho.crm.api.profiles import *
from datetime import datetime


class Profile(object):

    @staticmethod
    def get_profiles():

        """
        This method is used to retrieve the profiles data through an API request and print the response.
        """

        # Get instance of ProfilesOperations Class that takes an optional parameter - if_modified_since request header
        profiles_operations = ProfilesOperations(datetime(2020, 10, 10, 15, 10, 7))

        # Call get_profiles method
        response = profiles_operations.get_profiles()

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

                    # Get the list of obtained Profile instances
                    profiles_list = response_object.get_profiles()

                    for profile in profiles_list:
                        # Get the DisplayLabel of the each Profile
                        print("Profile DisplayLabel: " + profile.get_display_label())

                        if profile.get_created_time() is not None:
                            # Get the CreatedTime of each Profile
                            print("Profile CreatedTime: " + str(profile.get_created_time()))

                        if profile.get_modified_time() is not None:
                            # Get the ModifiedTime of each Profile
                            print("Profile ModifiedTime: " + str(profile.get_modified_time()))

                        # Get the Name of the each Profile
                        print("Profile Name: " + profile.get_name())

                        # Get the modifiedBy User instance of each Profile
                        modified_by = profile.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Profile Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Profile Modified By - ID: " + str(modified_by.get_id()))

                        # Get the Description of the each Profile
                        print("Profile Description: " + str(profile.get_description()))

                        # Get the ID of the each Profile
                        print("Profile ID: " + str(profile.get_id()))

                        # Get the Category of the each Profile
                        print("Profile Category: " + str(profile.get_category()))

                        # Get the created_by User instance of each Profile
                        created_by = profile.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Profile Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Profile Created By - ID: " + str(created_by.get_id()))

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
    def get_profile(profile_id):

        """
        This method is used to get the details of any specific profile with ID.
        :param profile_id: The ID of the Profile to be obtained
        """

        """
        example
        profile_id = 3409643000002280002
        """

        # Get instance of ProfilesOperations Class
        profiles_operations = ProfilesOperations()

        # Call get_profile method that takes profile_id as parameter
        response = profiles_operations.get_profile(profile_id)

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

                    # Get the list of obtained Profile instances
                    profiles_list = response_object.get_profiles()

                    for profile in profiles_list:
                        # Get the DisplayLabel of the each Profile
                        print("Profile DisplayLabel: " + profile.get_display_label())

                        if profile.get_created_time() is not None:
                            # Get the CreatedTime of each Profile
                            print("Profile CreatedTime: " + str(profile.get_created_time()))

                        if profile.get_modified_time() is not None:
                            # Get the ModifiedTime of each Profile
                            print("Profile ModifiedTime: " + str(profile.get_modified_time()))

                        # Get the Name of the each Profile
                        print("Profile Name: " + profile.get_name())

                        # Get the modifiedBy User instance of each Profile
                        modified_by = profile.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Profile Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Profile Modified By - ID: " + str(modified_by.get_id()))

                        # Get the Description of the each Profile
                        print("Profile Description: " + str(profile.get_description()))

                        # Get the ID of the each Profile
                        print("Profile ID: " + str(profile.get_id()))

                        # Get the Category of the each Profile
                        print("Profile Category: " + str(profile.get_category()))

                        # Get the created_by User instance of each Profile
                        created_by = profile.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Profile Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Profile Created By - ID: " + str(created_by.get_id()))

                        # Get the permissionsDetails of each Profile
                        permissions_details = profile.get_permissions_details()

                        if permissions_details is not None:

                            for permissions_detail in permissions_details:
                                # Get the DisplayLabel of the each PermissionDetail
                                print("Profile PermissionDetail DisplayLabel: " + str(permissions_detail.get_display_label()))

                                # Get the Module of the each PermissionDetail
                                print("Profile PermissionDetail Module: " + str(permissions_detail.get_module()))

                                # Get the Name of the each PermissionDetail
                                print("Profile PermissionDetail Name: " + str(permissions_detail.get_name()))

                                # Get the ID of the each PermissionDetail
                                print("Profile PermissionDetail ID: " + str(permissions_detail.get_id()))

                                # Get the Enabled of the each PermissionDetail
                                print("Profile PermissionDetail Enabled: " + str(permissions_detail.get_enabled()))

                        # Get the sections of each Profile
                        sections = profile.get_sections()

                        if sections is not None:
                            for section in sections:

                                # Get the Name of the each Section
                                print("Profile Section Name: " + section.get_name())

                                # Get the categories of each Section
                                categories = section.get_categories()

                                if categories is not None:
                                    for category in categories:

                                        # Get the DisplayLabel of the each Category
                                        print("Profile Section Category DisplayLabel: " + str(category.get_display_label()))

                                        # Get the permissionsDetails List of each Category
                                        category_permissions_details = category.get_permissions_details()

                                        if category_permissions_details is not None:
                                            for permissions_detail_id in category_permissions_details:
                                                # Get the permissionsDetailID of the Category
                                                print("Profile Section Category permissionsDetailID: " + permissions_detail_id)

                                        # Get the Name of the each Category
                                        print("Profile Section Category Name: " + str(category.get_name()))

                        if profile.get_delete() is not None:
                            # Get the Delete of the each Profile
                            print("Profile Delete: " + str(profile.get_delete()))

                        if profile.get_default() is not None:
                            # Get the Default of the each Profile
                            print("Profile Default: " + str(profile.get_default()))

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
