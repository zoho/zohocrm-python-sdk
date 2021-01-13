from zcrmsdk.src.com.zoho.crm.api.users import *
from zcrmsdk.src.com.zoho.crm.api.users import User as ZCRMUser
from zcrmsdk.src.com.zoho.crm.api.roles import Role
from zcrmsdk.src.com.zoho.crm.api.profiles import Profile
from zcrmsdk.src.com.zoho.crm.api import ParameterMap, HeaderMap
from datetime import datetime


class User(object):

    @staticmethod
    def get_users():

        """
        This method is used to retrieve the users data specified in the API request.
        """

        # Get instance of UsersOperations Class
        users_operations = UsersOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Users operation
        param_instance.add(GetUsersParam.page, 1)

        param_instance.add(GetUsersParam.per_page, 200)

        param_instance.add(GetUsersParam.type, 'ActiveConfirmedUsers')

        # Get instance of ParameterMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Users operation
        header_instance.add(GetUsersHeader.if_modified_since, datetime.fromisoformat('2019-07-07T10:00:00+05:30'))

        # Call get_users method that takes ParameterMap instance and HeaderMap instance as parameters
        response = users_operations.get_users(param_instance, header_instance)

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

                    # Get the list of obtained User instances
                    user_list = response_object.get_users()

                    for user in user_list:
                        # Get the Country of each User
                        print("User Country: " + str(user.get_country()))

                        # Get the CustomizeInfo instance of each User
                        customize_info = user.get_customize_info()

                        # Check if customizeInfo is not None
                        if customize_info is not None:
                            if customize_info.get_notes_desc() is not None:
                                # Get the NotesDesc of each User
                                print("User CustomizeInfo NotesDesc: " + str(customize_info.get_notes_desc()))

                            if customize_info.get_show_right_panel() is not None:
                                # Get the ShowRightPanel of each User
                                print("User CustomizeInfo ShowRightPanel: " + str(customize_info.get_show_right_panel()))

                            if customize_info.get_bc_view() is not None:
                                # Get the BcView of each User
                                print("User CustomizeInfo BcView: " + str(customize_info.get_bc_view()))

                            if customize_info.get_show_home() is not None:
                                # Get the ShowHome of each User
                                print("User CustomizeInfo ShowHome: " + str(customize_info.get_show_home()))

                            if customize_info.get_show_detail_view() is not None:
                                # Get the ShowDetailView of each User
                                print("User CustomizeInfo ShowDetailView: " + str(customize_info.get_show_detail_view()))

                            if customize_info.get_unpin_recent_item() is not None:
                                # Get the UnpinRecentItem of each User
                                print("User CustomizeInfo UnpinRecentItem: " + str(customize_info.get_unpin_recent_item()))

                        # Get the Role instance of each User
                        role = user.get_role()

                        if role is not None:
                            # Get the Name of Role
                            print("User Role Name: " + str(role.get_name()))

                            # Get the ID of Role
                            print("User Role ID: " + str(role.get_id()))

                        # Get the Signature of each User
                        print("User Signature: " + str(user.get_signature()))

                        # Get the City of each User
                        print("User City: " + str(user.get_city()))

                        # Get the NameFormat of each User
                        print("User NameFormat: " + str(user.get_name_format()))

                        # Get the Language of each User
                        print("User Language: " + str(user.get_language()))

                        # Get the Locale of each User
                        print("User Locale: " + str(user.get_locale()))

                        # Get the Microsoft of each User
                        print("User Microsoft: " + str(user.get_microsoft()))

                        if user.get_personal_account() is not None:
                            # Get the PersonalAccount of each User
                            print("User PersonalAccount: " + str(user.get_personal_account()))

                        # Get the DefaultTabGroup of each User
                        print("User DefaultTabGroup: " + str(user.get_default_tab_group()))

                        # Get the Isonline of each User
                        print("User Isonline: " + str(user.get_isonline()))

                        # Get the modifiedBy User instance of each User
                        modified_by = user.get_modified_by()

                        # Check if modified_by is not null
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("User Modified By User-Name: " + str(modified_by.get_name()))

                            # Get the ID of the modifiedBy User
                            print("User Modified By User-ID: " + str(modified_by.get_id()))

                        # Get the Street of each User
                        print("User Street: " + str(user.get_street()))

                        # Get the Currency of each User
                        print("User Currency: " + str(user.get_currency()))

                        # Get the Alias of each User
                        print("User Alias: " + str(user.get_alias()))

                        # Get the Theme instance of each User
                        theme = user.get_theme()

                        # Check if theme is not None
                        if theme is not None:
                            # Get the TabTheme instance of Theme
                            normal_tab = theme.get_normal_tab()

                            # Check if normal_tab is not null
                            if normal_tab is not None:
                                # Get the FontColor of NormalTab
                                print("User Theme NormalTab FontColor: " + str(normal_tab.get_font_color()))

                                # Get the Background of NormalTab
                                print("User Theme NormalTab Background: " + str(normal_tab.get_background()))

                            # Get the TabTheme instance of Theme
                            selected_tab = theme.get_selected_tab()

                            # Check if selected_tab is not null
                            if selected_tab is not None:
                                # Get the FontColor of selected_tab
                                print("User Theme Selected Tab FontColor: " + str(selected_tab.get_font_color()))

                                # Get the Background of selected_tab
                                print("User Theme Selected Tab Background: " + str(selected_tab.get_background()))

                            # Get the NewBackground of each Theme
                            print("User Theme NewBackground: " + str(theme.get_new_background()))

                            # Get the Background of each Theme
                            print("User Theme Background: " + str(theme.get_background()))

                            # Get the Screen of each Theme
                            print("User Theme Screen: " + str(theme.get_screen()))

                            # Get the Type of each Theme
                            print("User Theme Type: " + str(theme.get_type()))

                        # Get the ID of each User
                        print("User ID: " + str(user.get_id()))

                        # Get the State of each User
                        print("User State: " + str(user.get_state()))

                        # Get the Fax of each User
                        print("User Fax: " + str(user.get_fax()))

                        # Get the CountryLocale of each User
                        print("User CountryLocale: " + str(user.get_country_locale()))

                        # Get the FirstName of each User
                        print("User FirstName: " + str(user.get_first_name()))

                        # Get the Email of each User
                        print("User Email: " + str(user.get_email()))

                        # Get the reportingTo User instance of each User
                        reporting_to = user.get_reporting_to()

                        # Check if reporting_to is not None
                        if reporting_to is not None:
                            # Get the Name of the reporting_to User
                            print("User ReportingTo User-Name: " + str(reporting_to.get_name()))

                            # Get the ID of the reporting_to User
                            print("User ReportingTo User-ID: " + str(reporting_to.get_id()))

                        # Get the DecimalSeparator of each User
                        print("User DecimalSeparator: " + str(user.get_decimal_separator()))

                        # Get the Zip of each User
                        print("User Zip: " + str(user.get_zip()))

                        # Get the CreatedTime of each User
                        print("User CreatedTime: " + str(user.get_created_time()))

                        # Get the Website of each User
                        print("User Website: " + str(user.get_website()))

                        if user.get_modified_time() is not None:
                            # Get the ModifiedTime of each User
                            print("User ModifiedTime: " + str(user.get_modified_time()))

                        # Get the TimeFormat of each User
                        print("User TimeFormat: " + str(user.get_time_format()))

                        # Get the Offset of each User
                        print("User Offset: " + str(user.get_offset()))

                        # Get the Profile instance of each User
                        profile = user.get_profile()

                        # Check if profile is not None
                        if profile is not None:
                            # Get the Name of the profile
                            print("User Profile Name: " + str(profile.get_name()))

                            # Get the ID of the profile
                            print("User Profile ID: " + str(profile.get_id()))

                        # Get the Mobile of each User
                        print("User Mobile: " + str(user.get_mobile()))

                        # Get the LastName of each User
                        print("User LastName: " + str(user.get_last_name()))

                        # Get the TimeZone of each User
                        print("User TimeZone: " + str(user.get_time_zone()))

                        # Get the Custom Fields, if any
                        print("Custom Field: " + str(user.get_key_value('Custom_Field')))

                        # Get the created_by User instance of each User
                        created_by = user.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("User Created By User-Name: " + str(created_by.get_name()))

                            # Get the ID of the created_by User
                            print("User Created By User-ID: " + str(created_by.get_id()))

                        # Get the Zuid of each User
                        print("User Zuid: " + str(user.get_zuid()))

                        # Get the Confirm of each User
                        print("User Confirm: " + str(user.get_confirm()))

                        # Get the FullName of each User
                        print("User FullName: " + str(user.get_full_name()))

                        # Get the list of obtained Territory instances
                        territories = user.get_territories()

                        # Check if territories is not None
                        if territories is not None:
                            for territory in territories:
                                # Get the Manager of the Territory
                                print("User Territory Manager: " + str(territory.get_manager()))

                                # Get the Name of the Territory
                                print("User Territory Name: " + str(territory.get_name()))

                                # Get the ID of the Territory
                                print("User Territory ID: " + str(territory.get_id()))

                        # Get the Phone of each User
                        print("User Phone: " + str(user.get_phone()))

                        # Get the DOB of each User
                        print("User DOB: " + str(user.get_dob()))

                        # Get the DateFormat of each User
                        print("User DateFormat: " + str(user.get_date_format()))

                        # Get the Status of each User
                        print("User Status: " + str(user.get_status()))

                    # Get the obtained Info object
                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage of the Info
                            print("User Info PerPage: " + str(info.get_per_page()))

                        if info.get_count() is not None:
                            # Get the Count of the Info
                            print("User Info Count: " + str(info.get_count()))

                        if info.get_page() is not None:
                            # Get the Page of the Info
                            print("User Info Page: " + str(info.get_page()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords of the Info
                            print("User Info MoreRecords: " + str(info.get_more_records()))

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
    def get_user(user_id):

        """
        This method is used to get the details of any specific user with ID
        :param user_id: The ID of the User to be obtained
        """

        """
        example
        user_id = 3409643000000302031
        """

        # Get instance of UsersOperations Class
        users_operations = UsersOperations()

        # Get instance of ParameterMap Class
        header_instance = HeaderMap()

        # Possible headers for Get User operation
        header_instance.add(GetUserHeader.if_modified_since, datetime.fromisoformat('2019-07-07T10:00:00+05:30'))

        # Call get_user method that takes HeaderMap instance and user_id as parameters
        response = users_operations.get_user(user_id, header_instance)

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

                    # Get the list of obtained User instances
                    user_list = response_object.get_users()

                    for user in user_list:
                        # Get the Country of each User
                        print("User Country: " + str(user.get_country()))

                        # Get the CustomizeInfo instance of each User
                        customize_info = user.get_customize_info()

                        # Check if customizeInfo is not None
                        if customize_info is not None:
                            if customize_info.get_notes_desc() is not None:
                                # Get the NotesDesc of each User
                                print("User CustomizeInfo NotesDesc: " + str(customize_info.get_notes_desc()))

                            if customize_info.get_show_right_panel() is not None:
                                # Get the ShowRightPanel of each User
                                print(
                                    "User CustomizeInfo ShowRightPanel: " + str(customize_info.get_show_right_panel()))

                            if customize_info.get_bc_view() is not None:
                                # Get the BcView of each User
                                print("User CustomizeInfo BcView: " + str(customize_info.get_bc_view()))

                            if customize_info.get_show_home() is not None:
                                # Get the ShowHome of each User
                                print("User CustomizeInfo ShowHome: " + str(customize_info.get_show_home()))

                            if customize_info.get_show_detail_view() is not None:
                                # Get the ShowDetailView of each User
                                print(
                                    "User CustomizeInfo ShowDetailView: " + str(customize_info.get_show_detail_view()))

                            if customize_info.get_unpin_recent_item() is not None:
                                # Get the UnpinRecentItem of each User
                                print("User CustomizeInfo UnpinRecentItem: " + str(
                                    customize_info.get_unpin_recent_item()))

                        # Get the Role instance of each User
                        role = user.get_role()

                        if role is not None:
                            # Get the Name of Role
                            print("User Role Name: " + str(role.get_name()))

                            # Get the ID of Role
                            print("User Role ID: " + str(role.get_id()))

                        # Get the Signature of each User
                        print("User Signature: " + str(user.get_signature()))

                        # Get the City of each User
                        print("User City: " + str(user.get_city()))

                        # Get the NameFormat of each User
                        print("User NameFormat: " + str(user.get_name_format()))

                        # Get the Language of each User
                        print("User Language: " + str(user.get_language()))

                        # Get the Locale of each User
                        print("User Locale: " + str(user.get_locale()))

                        # Get the Microsoft of each User
                        print("User Microsoft: " + str(user.get_microsoft()))

                        if user.get_personal_account() is not None:
                            # Get the PersonalAccount of each User
                            print("User PersonalAccount: " + str(user.get_personal_account()))

                        # Get the DefaultTabGroup of each User
                        print("User DefaultTabGroup: " + str(user.get_default_tab_group()))

                        # Get the Isonline of each User
                        print("User Isonline: " + str(user.get_isonline()))

                        # Get the modifiedBy User instance of each User
                        modified_by = user.get_modified_by()

                        # Check if modified_by is not null
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("User Modified By User-Name: " + str(modified_by.get_name()))

                            # Get the ID of the modifiedBy User
                            print("User Modified By User-ID: " + str(modified_by.get_id()))

                        # Get the Street of each User
                        print("User Street: " + str(user.get_street()))

                        # Get the Currency of each User
                        print("User Currency: " + str(user.get_currency()))

                        # Get the Alias of each User
                        print("User Alias: " + str(user.get_alias()))

                        # Get the Theme instance of each User
                        theme = user.get_theme()

                        # Check if theme is not None
                        if theme is not None:
                            # Get the TabTheme instance of Theme
                            normal_tab = theme.get_normal_tab()

                            # Check if normal_tab is not null
                            if normal_tab is not None:
                                # Get the FontColor of NormalTab
                                print("User Theme NormalTab FontColor: " + str(normal_tab.get_font_color()))

                                # Get the Background of NormalTab
                                print("User Theme NormalTab Background: " + str(normal_tab.get_background()))

                            # Get the TabTheme instance of Theme
                            selected_tab = theme.get_selected_tab()

                            # Check if selected_tab is not null
                            if selected_tab is not None:
                                # Get the FontColor of selected_tab
                                print("User Theme Selected Tab FontColor: " + str(selected_tab.get_font_color()))

                                # Get the Background of selected_tab
                                print("User Theme Selected Tab Background: " + str(selected_tab.get_background()))

                            # Get the NewBackground of each Theme
                            print("User Theme NewBackground: " + str(theme.get_new_background()))

                            # Get the Background of each Theme
                            print("User Theme Background: " + str(theme.get_background()))

                            # Get the Screen of each Theme
                            print("User Theme Screen: " + str(theme.get_screen()))

                            # Get the Type of each Theme
                            print("User Theme Type: " + str(theme.get_type()))

                        # Get the ID of each User
                        print("User ID: " + str(user.get_id()))

                        # Get the State of each User
                        print("User State: " + str(user.get_state()))

                        # Get the Fax of each User
                        print("User Fax: " + str(user.get_fax()))

                        # Get the CountryLocale of each User
                        print("User CountryLocale: " + str(user.get_country_locale()))

                        # Get the FirstName of each User
                        print("User FirstName: " + str(user.get_first_name()))

                        # Get the Email of each User
                        print("User Email: " + str(user.get_email()))

                        # Get the reportingTo User instance of each User
                        reporting_to = user.get_reporting_to()

                        # Check if reporting_to is not None
                        if reporting_to is not None:
                            # Get the Name of the reporting_to User
                            print("User ReportingTo User-Name: " + str(reporting_to.get_name()))

                            # Get the ID of the reporting_to User
                            print("User ReportingTo User-ID: " + str(reporting_to.get_id()))

                        # Get the DecimalSeparator of each User
                        print("User DecimalSeparator: " + str(user.get_decimal_separator()))

                        # Get the Zip of each User
                        print("User Zip: " + str(user.get_zip()))

                        # Get the CreatedTime of each User
                        print("User CreatedTime: " + str(user.get_created_time()))

                        # Get the Website of each User
                        print("User Website: " + str(user.get_website()))

                        if user.get_modified_time() is not None:
                            # Get the ModifiedTime of each User
                            print("User ModifiedTime: " + str(user.get_modified_time()))

                        # Get the TimeFormat of each User
                        print("User TimeFormat: " + str(user.get_time_format()))

                        # Get the Offset of each User
                        print("User Offset: " + str(user.get_offset()))

                        # Get the Profile instance of each User
                        profile = user.get_profile()

                        # Check if profile is not None
                        if profile is not None:
                            # Get the Name of the profile
                            print("User Profile Name: " + str(profile.get_name()))

                            # Get the ID of the profile
                            print("User Profile ID: " + str(profile.get_id()))

                        # Get the Mobile of each User
                        print("User Mobile: " + str(user.get_mobile()))

                        # Get the LastName of each User
                        print("User LastName: " + str(user.get_last_name()))

                        # Get the TimeZone of each User
                        print("User TimeZone: " + str(user.get_time_zone()))

                        # Get the Custom Fields, if any
                        print("Custom Field: " + str(user.get_key_value('Custom_Field')))

                        # Get the created_by User instance of each User
                        created_by = user.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("User Created By User-Name: " + str(created_by.get_name()))

                            # Get the ID of the created_by User
                            print("User Created By User-ID: " + str(created_by.get_id()))

                        # Get the Zuid of each User
                        print("User Zuid: " + str(user.get_zuid()))

                        # Get the Confirm of each User
                        print("User Confirm: " + str(user.get_confirm()))

                        # Get the FullName of each User
                        print("User FullName: " + str(user.get_full_name()))

                        # Get the list of obtained Territory instances
                        territories = user.get_territories()

                        # Check if territories is not None
                        if territories is not None:
                            for territory in territories:
                                # Get the Manager of the Territory
                                print("User Territory Manager: " + str(territory.get_manager()))

                                # Get the Name of the Territory
                                print("User Territory Name: " + str(territory.get_name()))

                                # Get the ID of the Territory
                                print("User Territory ID: " + str(territory.get_id()))

                        # Get the Phone of each User
                        print("User Phone: " + str(user.get_phone()))

                        # Get the DOB of each User
                        print("User DOB: " + str(user.get_dob()))

                        # Get the DateFormat of each User
                        print("User DateFormat: " + str(user.get_date_format()))

                        # Get the Status of each User
                        print("User Status: " + str(user.get_status()))

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
    def update_users():

        """
        This method is used to update the details of multiple users of your organization and print the response.
        """

        # Get instance of UsersOperations Class
        users_operations = UsersOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold User instances
        user_list = []

        # Get instance of User Class
        user_1 = ZCRMUser()

        # Set ID to User instance
        user_1.set_id(3409643000000302031)

        # Get instance of Role Class
        role = Role()

        # Set ID to Role instance
        role.set_id(3409643000000026008)

        # Set role instance to role in User
        user_1.set_role(role)

        user_1.set_country_locale('en_US')

        # Add User instance to list
        user_list.append(user_1)

        # Get instance of User Class
        user_2 = ZCRMUser()

        # Set ID to User instance
        user_2.set_id(3409643000000302042)

        # Get instance of Role Class
        role = Role()

        # Set ID to Role instance
        role.set_id(3409643000000026008)

        # Set role instance to role in User
        user_2.set_role(role)

        user_2.set_country_locale('en_US')

        # Add User instance to list
        user_list.append(user_2)

        # Set the list to users in BodyWrapper
        request.set_users(user_list)

        # Call update_users method that takes BodyWrapper instance as parameter
        response = users_operations.update_users(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_users()

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
    def update_user(user_id):

        """
        This method is used to update the details of any specific user with ID
        :param user_id: The ID of the User to be updated
        """

        """
        example
        user_id = 3409643000000302031
        """

        # Get instance of UsersOperations Class
        users_operations = UsersOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold User instances
        user_list = []

        # Get instance of User Class
        user_1 = ZCRMUser()

        # Get instance of Role Class
        role = Role()

        # Set ID to Role instance
        role.set_id(3409643000000026008)

        # Set role instance to role in User
        user_1.set_role(role)

        # Add User instance to list
        user_list.append(user_1)

        # Set the list to users in BodyWrapper
        request.set_users(user_list)

        # Call update_user method that takes BodyWrapper instance and user_id as parameters
        response = users_operations.update_user(user_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_users()

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
    def delete_user(user_id):

        """
        This method is used to delete a user from your organization and print the response.
        :param user_id: The ID of the User to be deleted
        """

        """
        example
        user_id = 3409643000000302031
        """

        # Get instance of UsersOperations Class
        users_operations = UsersOperations()

        # Call delete_user method that takes user_id as parameter
        response = users_operations.delete_user(user_id)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_users()

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
    def create_user():

        """
        This method is used to add a user to your organization and print the response.
        """

        # Get instance of UsersOperations Class
        users_operations = UsersOperations()

        # Get instance of RequestWrapper Class that will contain the request body
        request = RequestWrapper()

        # List to hold User instances
        user_list = []

        # Get instance of User Class
        user = ZCRMUser()

        # Get instance of Role Class
        role = Role()

        # Set ID to Role instance
        role.set_id(3409643000000026008)

        # Set role instance to role in User
        user.set_role(role)

        user.set_country_locale('en_US')

        user.set_first_name('Test')

        user.set_last_name('User')

        user.set_email('testuser@zoho.com')

        # Get instance of Profile Class
        profile = Profile()

        # Set ID to Profile instance
        profile.set_id(3409643000000395047)

        # Set profile instance to profile in User instance
        user.set_profile(profile)

        # Add the User instance to list
        user_list.append(user)

        # Set the list to users in BodyWrapper instance
        request.set_users(user_list)

        # Call create_user method that takes RequestWrapper class instance as parameter
        response = users_operations.create_user(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_users()

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





