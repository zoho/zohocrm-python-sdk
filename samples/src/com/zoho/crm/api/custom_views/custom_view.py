from zcrmsdk.src.com.zoho.crm.api.custom_views import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class CustomView(object):

    @staticmethod
    def get_custom_views(module_api_name):

        """
        This method is used to get the custom views data of a particular module.
        Specify the module name in your API request whose custom view data you want to retrieve.
        :param module_api_name: the API name of the required module.
        """

        """
        example
        module_api_name = "Leads";
        """

        # Get instance of CustomViewOperations Class that takes module_api_name as parameter
        custom_views_operations = CustomViewsOperations(module_api_name)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get CustomViews operation
        param_instance.add(GetCustomViewsParam.page, 1)

        param_instance.add(GetCustomViewsParam.per_page, 20)

        # Call get_custom_views method that takes ParameterMap instance as parameter
        response = custom_views_operations.get_custom_views(param_instance)

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

                    # Get the list of obtained CustomView instances
                    custom_views_list = response_object.get_custom_views()

                    for custom_view in custom_views_list:

                        # Get the ID of each CustomView
                        print('CustomView ID: ' + str(custom_view.get_id()))

                        # Get the Name of each CustomView
                        print('CustomView Name: ' + str(custom_view.get_name()))

                        # Get the System Name of each CustomView
                        print('CustomView System Name: ' + str(custom_view.get_system_name()))

                        # Get the Category of each CustomView
                        print('CustomView Category: ' + str(custom_view.get_category()))

                        # Get the DisplayValue of each CustomView
                        print('CustomView Display Value: ' + str(custom_view.get_display_value()))

                        # Get the Offline value of each CustomView
                        print('CustomView Is offline: ' + str(custom_view.get_offline()))

                        # Get the default value of each CustomView
                        print('CustomView Is default: ' + str(custom_view.get_default()))

                        # Get the SystemDefined of each CustomView
                        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))

                        if custom_view.get_favorite() is not None:
                            # Get the Favorite of each CustomView
                            print('CustomView Favorite: ' + str(custom_view.get_favorite()))

                    info = response_object.get_info()

                    if info is not None:
                        print("CustomView Info")

                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('PerPage: ' + str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('Page: ' + str(info.get_page()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords from Info
                            print('MoreRecords: ' + str(info.get_more_records()))

                        if info.get_default() is not None:
                            # Get the Default from Info
                            print('Default: ' + info.get_default())

                        if info.get_count() is not None:
                            # Get the Count from Info
                            print('Count: ' + str(info.get_count()))

                        translation = info.get_translation()

                        if translation is not None:
                            print("Translation details")

                            # Get the PublicViews of the Translation
                            print('PublicViews: ' + translation.get_public_views())

                            # Get the OtherUsersViews of the Translation
                            print('OtherUsersViews: ' + translation.get_other_users_views())

                            # Get the SharedWithMe of the Translation
                            print('SharedWithMe: ' + translation.get_shared_with_me())

                            # Get the CreatedByMe of the Translation
                            print('CreatedByMe: ' + translation.get_created_by_me())

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
    def get_custom_view(module_api_name, custom_view_id):

        """
        This method is used to get the data of any specific custom view of the module with ID
        :param module_api_name: The API name of the required module.
        :param custom_view_id: ID of the CustomView to be obtained
        :return:
        """

        """
        example
        module_api_name = "Leads"
        custom_view_id = 3409643000002955026n
        """

        # Get instance of CustomViewOperations Class that takes module_api_name as parameter
        custom_views_operations = CustomViewsOperations(module_api_name)

        # Call get_custom_view method that takes custom_view_id as parameter
        response = custom_views_operations.get_custom_view(custom_view_id)

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

                    # Get the list of obtained CustomView instances
                    custom_views_list = response_object.get_custom_views()

                    for custom_view in custom_views_list:

                        # Get the ID of each CustomView
                        print('CustomView ID: ' + str(custom_view.get_id()))

                        # Get the Name of each CustomView
                        print('CustomView Name: ' + str(custom_view.get_name()))

                        # Get the System Name of each CustomView
                        print('CustomView System Name: ' + str(custom_view.get_system_name()))

                        # Get the Category of each CustomView
                        print('CustomView Category: ' + str(custom_view.get_category()))

                        # Get the DisplayValue of each CustomView
                        print('CustomView Display Value: ' + str(custom_view.get_display_value()))

                        # Get the SharedType of each CustomView
                        print('CustomView SharedType: ' + str(custom_view.get_shared_type()))

                        shared_details = custom_view.get_shared_details()

                        if shared_details is not None:
                            for shared_detail in shared_details:

                                # Get the Name of the each SharedDetails
                                print("SharedDetails Name: " + shared_detail.get_name())

                                # Get the ID of the each SharedDetails
                                print("SharedDetails ID: " + shared_detail.get_id())

                                # Get the Type of the each SharedDetails
                                print("SharedDetails Type: " + shared_detail.get_type())

                                # Get the Subordinates of the each SharedDetails
                                print("SharedDetails Subordinates: " + str(shared_detail.get_subordinates()))

                        # Get the Offline value of each CustomView
                        print('CustomView Is offline: ' + str(custom_view.get_offline()))

                        criteria = custom_view.get_criteria()

                        if criteria is not None:
                            CustomView.print_criteria(criteria)

                        # Get the default value of each CustomView
                        print('CustomView Is default: ' + str(custom_view.get_default()))

                        # Get the SortBy of each CustomView
                        print('CustomView SortBy: ' + str(custom_view.get_sort_by()))

                        if custom_view.get_sort_order() is not None:
                            # Get the SortOrder of each CustomView
                            print('CustomView SortOrder: ' + str(custom_view.get_sort_order()))

                        # Get the SystemDefined of each CustomView
                        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))

                        if custom_view.get_favorite() is not None:
                            # Get the Favorite of each CustomView
                            print('CustomView Favorite: ' + str(custom_view.get_favorite()))

                        # Get the fields of each CustomView
                        fields = custom_view.get_fields()

                        if fields is not None:
                            print('Fields')

                            for field in fields:
                                print(field)

                    # Get the Info object from response
                    info = response_object.get_info()

                    if info is not None:
                        print("CustomView Info")

                        translation = info.get_translation()

                        if translation is not None:
                            print("Translation details")

                            # Get the PublicViews of the Translation
                            print('PublicViews: ' + translation.get_public_views())

                            # Get the OtherUsersViews of the Translation
                            print('OtherUsersViews: ' + translation.get_other_users_views())

                            # Get the SharedWithMe of the Translation
                            print('SharedWithMe: ' + translation.get_shared_with_me())

                            # Get the CreatedByMe of the Translation
                            print('CreatedByMe: ' + translation.get_created_by_me())

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
    def print_criteria(criteria):

        if criteria.get_comparator() is not None:
            # Get the Comparator of the Criteria
            print('CustomView Criteria Comparator: ' + criteria.get_comparator().get_value())

        if criteria.get_field() is not None:
            # Get the Field of the Criteria
            print('CustomView Criteria Field: ' + criteria.get_field())

        if criteria.get_value() is not None:
            # Get the Value of the Criteria
            print('CustomView Criteria Value: ' + str(criteria.get_value()))

        # Get the List of Criteria instance of each Criteria
        criteria_group = criteria.get_group()

        if criteria_group is not None:
            for each_criteria in criteria_group:
                CustomView.print_criteria(each_criteria)

        if criteria.get_group_operator() is not None:
            # Get the Group Operator of the Criteria
            print('CustomView Criteria Group Operator: ' + criteria.get_group_operator().get_value())
