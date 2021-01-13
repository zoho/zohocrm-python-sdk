import os
from zcrmsdk.src.com.zoho.crm.api.bulk_read import *
from zcrmsdk.src.com.zoho.crm.api.util import Choice


class BulkRead(object):

    @staticmethod
    def create_bulk_read_job(module_api_name):

        """
        This method is used to create a bulk read job to export records.
        :param module_api_name: The API Name of the record's module
        """

        """
        example
        module_api_name = 'Leads'
        """

        # Get instance of BulkReadOperations Class
        bulk_read_operations = BulkReadOperations()

        # Get instance of RequestWrapper Class that will contain the request body
        request = RequestWrapper()

        # Get instance of CallBack Class
        call_back = CallBack()

        # Set valid callback URL
        call_back.set_url("https://www.example.com/callback")

        # Set the HTTP method of the callback URL. The allowed value is post.
        call_back.set_method(Choice('post'))

        # The Bulk Read Job's details is posted to this URL on successful completion / failure of the job.
        request.set_callback(call_back)

        # Get instance of Query Class
        query = Query()

        # Specifies the API Name of the module to be read.
        query.set_module(module_api_name)

        # Specifies the unique ID of the custom view, whose records you want to export.
        query.set_cvid('3409643000000087501')

        # List of field names
        field_api_names = ['Last_Name']

        # Specifies the API Name of the fields to be fetched
        query.set_fields(field_api_names)

        # To set page value, By default value is 1.
        query.set_page(1)

        # Get instance of Criteria Class
        criteria = Criteria()

        # To set API name of a field
        criteria.set_api_name('Created_Time')

        # To set comparator(eg: equal, greater_than)
        criteria.set_comparator(Choice('between'))

        time = ["2020-06-03T17:31:48+05:30", "2020-06-03T17:31:48+05:30"]

        # To set the value to be compared
        criteria.set_value(time)

        # To filter the records to be exported
        query.set_criteria(criteria)

        # Set the query object
        request.set_query(query)

        # Specify the value for this key as "ics" to export all records in the Events module as an ICS file.
        # request.set_file_type(Choice('ics'))

        # Call create_bulk_read_job method that takes RequestWrapper instance as parameter
        response = bulk_read_operations.create_bulk_read_job(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()

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
    def get_bulk_read_job_details(job_id):

        """
        This method is used to get the details of a bulk read job performed previously.
        :param job_id: The unique ID of the bulk read job.
        """

        """
        example
        job_id = 3409643000002461001
        """

        # Get instance of BulkReadOperations Class
        bulk_read_operations = BulkReadOperations()

        # Call get_bulk_read_job_details method that takes jobId as parameter
        response = bulk_read_operations.get_bulk_read_job_details(job_id)

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

                    # Get the list of JobDetail instances
                    job_details_list = response_object.get_data()

                    for job_detail in job_details_list:
                        # Get the Job ID of each jobDetail
                        print("Bulk read Job ID: " + str(job_detail.get_id()))

                        # Get the Operation of each jobDetail
                        print("Bulk read Operation: " + job_detail.get_operation())

                        # Get the State of each jobDetail
                        print("Bulk read State: " + job_detail.get_state().get_value())

                        # Get the Result instance of each jobDetail
                        result = job_detail.get_result()

                        if result is not None:
                            # Get the Page of the Result
                            print("Bulkread Result Page: " + str(result.get_page()))

                            # Get the Count of the Result
                            print("Bulkread Result Count: " + str(result.get_count()))

                            # Get the Download URL of the Result
                            print("Bulkread Result Download URL: " + result.get_download_url())

                            # Get the Per_Page of the Result
                            print("Bulkread Result Per_Page: " + str(result.get_per_page()))

                            # Get the MoreRecords of the Result
                            print("Bulkread Result MoreRecords: " + str(result.get_more_records()))

                        # Get the Query instance of each jobDetail
                        query = job_detail.get_query()

                        if query is not None:
                            # Get the Module Name of the Query
                            print("Bulk read Query Module: " + query.get_module())

                            # Get the Page of the Query
                            print("Bulk read Query Page: " + str(query.get_page()))

                            # Get the cvid of the Query
                            print("Bulk read Query cvid: " + str(query.get_cvid()))

                            # Get the fields List of the Query
                            fields = query.get_fields()

                            if fields is not None:
                                print("Bulk read fields")
                                for field in fields:
                                    print(field)

                            # Get the Criteria instance of the Query
                            criteria = query.get_criteria()

                            if criteria is not None:
                                BulkRead.print_criteria(criteria)

                            # Get the CreatedBy User instance of each jobDetail
                            created_by = job_detail.get_created_by()

                            # Check if created_by is not None
                            if created_by is not None:
                                # Get the Name of the created_by User
                                print("Bulkread Created By - Name: " + created_by.get_name())

                                # Get the ID of the created_by User
                                print("Bulkread Created By - ID: " + str(created_by.get_id()))

                            # Get the CreatedTime of each jobDetail
                            print("Bulkread CreatedTime: " + str(job_detail.get_created_time()))

                            # Get the FileType of each jobDetail
                            print("Bulkread File Type: " + job_detail.get_file_type())

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
    def download_result(job_id, destination_folder):

        """
        This method is used to download the result of Bulk Read operation
        :param job_id: The unique ID of the bulk read job.
        :param destination_folder: The absolute path where downloaded file has to be stored.
        """

        """
        example
        job_id = 3409643000002461001
        """

        # Get instance of BulkReadOperations Class
        bulk_read_operations = BulkReadOperations()

        # Call download_result method that takes job_id as parameter
        response = bulk_read_operations.download_result(job_id)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected FileBodyWrapper instance is received.
                if isinstance(response_object, FileBodyWrapper):

                    # Get StreamWrapper instance from the returned FileBodyWrapper instance
                    stream_wrapper = response_object.get_file()

                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(destination_folder, stream_wrapper.get_name())

                    # Open the destination file where the file needs to be written in 'wb' mode
                    with open(file_name, 'wb') as f:
                        # Get the stream from StreamWrapper instance
                        for chunk in stream_wrapper.get_stream():
                            f.write(chunk)

                        f.close()

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
        if criteria.get_api_name() is not None:
            # Get the API Name of the Criteria
            print('BulkRead Criteria API Name: ' + criteria.get_api_name())

        if criteria.get_comparator() is not None:
            # Get the Comparator of the Criteria
            print('BulkRead Criteria Comparator: ' + criteria.get_comparator().get_value())

        if criteria.get_value() is not None:
            # Get the Value of the Criteria
            print('BulkRead Criteria Value: ' + str(criteria.get_value()))

        # Get the List of Criteria instance of each Criteria
        criteria_group = criteria.get_group()

        if criteria_group is not None:
            for each_criteria in criteria_group:
                BulkRead.print_criteria(each_criteria)

        if criteria.get_group_operator() is not None:
            # Get the Group Operator of the Criteria
            print('BulkRead Criteria Group Operator: ' + criteria.get_group_operator().get_value())
