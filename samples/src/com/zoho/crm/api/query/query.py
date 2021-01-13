from zcrmsdk.src.com.zoho.crm.api.query import *


class Query(object):

    @staticmethod
    def get_records():

        """
        This method is used to get records from the module through a COQL query.
        """

        # Get instance of QueryOperations Class
        query_operations = QueryOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        body_wrapper = BodyWrapper()

        select_query = "select Last_Name, Account_Name.Parent_Account, Account_Name.Parent_Account.Account_Name,First_Name, Full_Name, Created_Time from Contacts where Last_Name is not null limit 200"

        # Set the select_query to BodyWrapper instance
        body_wrapper.set_select_query(select_query)

        # Call get_records method that takes BodyWrapper instance as parameter
        response = query_operations.get_records(body_wrapper)

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

                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        # Get the ID of each Record
                        print("Record ID: " + record.get_id())

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " + created_by.get_id())

                            # Get the Email of the created_by User
                            print("Record Created By - Email: " + created_by.get_email())

                        # Get the CreatedTime of each Record
                        print("Record CreatedTime: " + str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each Record
                            print("Record ModifiedTime: " + str(record.get_modified_time()))

                        # Get the modified_by User instance of each Record
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("Record Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("Record Modified By - ID: " + modified_by.get_id())

                            # Get the Email of the modified_by User
                            print("Record Modified By - Email: " + modified_by.get_email())

                        print('Record KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):
                                print("Record KeyName : " + key_name)

                                for data in value:
                                    if isinstance(data, dict):
                                        for dict_key, dict_value in data.items():
                                            print(dict_key + " : " + str(dict_value))

                                    else:
                                        print(str(data))

                            elif isinstance(value, dict):
                                print("Record KeyName : " + key_name + " -  Value : ")

                                for dict_key, dict_value in value.items():
                                    print(dict_key + " : " + str(dict_value))

                            else:
                                print("Record KeyName : " + key_name + " -  Value : " + str(value))

                        info = response_object.get_info()

                        if info is not None:
                            if info.get_count() is not None:
                                # Get the Count from Info
                                print('Record Info Count: ' + str(info.get_count()))

                            if info.get_more_records() is not None:
                                # Get the MoreRecords from Info
                                print('Record Info MoreRecords: ' + str(info.get_more_records()))

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
