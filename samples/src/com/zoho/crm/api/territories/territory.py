from zcrmsdk.src.com.zoho.crm.api.territories import *


class Territory(object):

    @staticmethod
    def get_territories():

        """
        This method is used to get the list of territories enabled for your organization and print the response.
        """

        # Get instance of TerritoriesOperations Class
        territories_operations = TerritoriesOperations()

        # Call get_territories method
        response = territories_operations.get_territories()

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

                    # Get the list of obtained Territory instances
                    territory_list = response_object.get_territories()

                    for territory in territory_list:
                        # Get the CreatedTime of each Territory
                        print("Territory CreatedTime: " + str(territory.get_created_time()))

                        if territory.get_modified_time() is not None:
                            # Get the ModifiedTime of each Territory
                            print("Territory ModifiedTime: " + str(territory.get_modified_time()))

                        # Get the manager User instance of each Territory
                        manager = territory.get_manager()

                        # Check if manager is not null
                        if manager is not None:
                            # Get the Name of the Manager
                            print("Territory Manager User-Name: " + manager.get_name())

                            # Get the ID of the Manager
                            print("Territory Manager User-ID: " + str(manager.get_id()))

                        # Get the ParentId of each Territory
                        print("Territory ParentId: " + str(territory.get_parent_id()))

                        # Get the Criteria instance of each Territory
                        criteria = territory.get_criteria()

                        if criteria is not None:
                            Territory.print_criteria(criteria)

                        # Get the Name of each Territory
                        print("Territory Name: " + str(territory.get_name()))

                        # Get the modifiedBy User instance of each Territory
                        modified_by = territory.get_modified_by()

                        # Check if modified_by is not null
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Territory Modified By User-Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Territory Modified By User-ID: " + str(modified_by.get_id()))

                        # Get the Description of each Territory
                        print("Territory Description: " + str(territory.get_description()))

                        # Get the ID of each Territory
                        print("Territory ID: " + str(territory.get_id()))

                        # Get the createdBy User instance of each Territory
                        created_by = territory.get_created_by()

                        # Check if created_by is not null
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Territory Created By User-Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Territory Created By User-ID: " + str(created_by.get_id()))

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
    def get_territory(territory_id):

        """
        This method is used to get the single territory with id and print the response.
        :param territory_id: The ID of the Territory to be obtained
        """

        """
        example
        territory_id = 3409643000000505351
        """

        # Get instance of TerritoriesOperations Class
        territories_operations = TerritoriesOperations()

        # Call get_territory method that takes territory_id as parameter
        response = territories_operations.get_territory(territory_id)

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

                    # Get the list of obtained Territory instances
                    territory_list = response_object.get_territories()

                    for territory in territory_list:
                        # Get the CreatedTime of each Territory
                        print("Territory CreatedTime: " + str(territory.get_created_time()))

                        if territory.get_modified_time() is not None:
                            # Get the ModifiedTime of each Territory
                            print("Territory ModifiedTime: " + str(territory.get_modified_time()))

                        # Get the manager User instance of each Territory
                        manager = territory.get_manager()

                        # Check if manager is not null
                        if manager is not None:
                            # Get the Name of the Manager
                            print("Territory Manager User-Name: " + manager.get_name())

                            # Get the ID of the Manager
                            print("Territory Manager User-ID: " + manager.get_id())

                        # Get the ParentId of each Territory
                        print("Territory ParentId: " + str(territory.get_parent_id()))

                        # Get the Criteria instance of each Territory
                        criteria = territory.get_criteria()

                        if criteria is not None:
                            Territory.print_criteria(criteria)

                        # Get the Name of each Territory
                        print("Territory Name: " + territory.get_name())

                        # Get the modifiedBy User instance of each Territory
                        modified_by = territory.get_modified_by()

                        # Check if modified_by is not null
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Territory Modified By User-Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Territory Modified By User-ID: " + str(modified_by.get_id()))

                        # Get the Description of each Territory
                        print("Territory Description: " + str(territory.get_description()))

                        # Get the ID of each Territory
                        print("Territory ID: " + str(territory.get_id()))

                        # Get the createdBy User instance of each Territory
                        created_by = territory.get_created_by()

                        # Check if created_by is not null
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Territory Created By User-Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Territory Created By User-ID: " + str(created_by.get_id()))

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
            print('Territory Criteria Comparator: ' + criteria.get_comparator().get_value())

        if criteria.get_field() is not None:
            # Get the Field of the Criteria
            print('Territory Criteria Field: ' + criteria.get_field())

        if criteria.get_value() is not None:
            # Get the Value of the Criteria
            print('Territory Criteria Value: ' + str(criteria.get_value()))

        # Get the List of Criteria instance of each Criteria
        criteria_group = criteria.get_group()

        if criteria_group is not None:
            for each_criteria in criteria_group:
                Territory.print_criteria(each_criteria)

        if criteria.get_group_operator() is not None:
            # Get the Group Operator of the Criteria
            print('Territory Criteria Group Operator: ' + criteria.get_group_operator().get_value())



