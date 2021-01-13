import os
from zcrmsdk.src.com.zoho.crm.api.bulk_write import *
from zcrmsdk.src.com.zoho.crm.api.util import Choice, StreamWrapper
from zcrmsdk.src.com.zoho.crm.api import HeaderMap


class BulkWrite(object):

    @staticmethod
    def upload_file(org_id, absolute_file_path):

        """
        This method is used to upload a CSV file in ZIP format for bulk write API. The response contains the file_id.
        :param org_id: The unique ID (zgid) of your organization obtained through the Organization API.
        :param absolute_file_path: The absoluteFilePath of the zip file you want to upload.
        """

        """
        example
        org_id = "673573045"
        absolute_file_path = "/Users/user_name/Documents/Leads.zip"
        """

        # Get instance of BulkWriteOperations Class
        bulk_write_operations = BulkWriteOperations()

        # Get instance of FileBodyWrapper class that will contain the request file
        file_body_wrapper = FileBodyWrapper()

        """
        StreamWrapper can be initialized in any of the following ways
    
        * param 1 -> fileName 
        * param 2 -> Read Stream.
        """
        # stream_wrapper = StreamWrapper(stream=open(absolute_file_path, 'rb'))

        """
        * param 1 -> fileName
        * param 2 -> Read Stream
        * param 3 -> Absolute File Path of the file to be attached
        """

        stream_wrapper = StreamWrapper(file_path=absolute_file_path)

        # Set file to the FileBodyWrapper instance
        file_body_wrapper.set_file(stream_wrapper)

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible parameters for upload_file operation
        header_instance.add(UploadFileHeader.feature, "bulk-write")

        header_instance.add(UploadFileHeader.x_crm_org, org_id)

        # Call upload_file method that takes FileBodyWrapper instance and header_instance as parameter
        response = bulk_write_operations.upload_file(file_body_wrapper, header_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, SuccessResponse):

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

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):

                    if response_object.get_status() is not None:
                        # Get the Status
                        print("Status: " + response_object.get_status().get_value())

                    if response_object.get_code() is not None:
                        # Get the Code
                        print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    if details is not None:
                        for key, value in details.items():
                            print(key + ' : ' + str(value))

                    if response_object.get_error_message() is not None:
                        # Get the ErrorMessage
                        print("Error Message: " + response_object.get_error_message().get_value())

                    # Get the ErrorCode
                    print('Error Code: ' + str(response_object.get_error_code()))

                    if response_object.get_x_error() is not None:
                        # Get the XError
                        print('XError: ' + response_object.get_x_error().get_value())

                    if response_object.get_info() is not None:
                        # Get the Info
                        print("Info: " + response_object.get_info().get_value())

                    if response_object.get_x_info() is not None:
                        # Get the XInfo
                        print("XInfo: " + response_object.get_x_info().get_value())

                    if response_object.get_message() is not None:
                        # Get the Message
                        print("Message: " + response_object.get_message().get_value())

                    print('HttpStatus: ' + response_object.get_http_status())

    @staticmethod
    def create_bulk_write_job(module_api_name, file_id):

        """
        This method is used to create bulk write job with the uploaded file ID
        :param module_api_name: The API Name of the module.
        :param file_id: The ID of the uploaded file to create BulkWrite Job.

        example
        module_api_name = 'Leads'
        file_id = 3409643000002212140
        """

        # Get instance of BulkWriteOperations Class
        bulk_write_operations = BulkWriteOperations()

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

        # Set the charset of the uploaded file
        request.set_character_encoding('UTF-8')

        # To set the type of operation you want to perform on the bulk write job.
        request.set_operation(Choice('insert'))

        resources = []

        # Get instance of Resource Class
        resource = Resource()

        # To set the type of module that you want to import. The value is data.
        resource.set_type(Choice('data'))

        # To set API name of the module that you select for bulk write job.
        resource.set_module(module_api_name)

        # To set the fileId obtained from file upload API.
        resource.set_file_id(file_id)

        # True - Ignores the empty values.The default value is false.
        resource.set_ignore_empty(True)

        # To set a field as a unique field or ID of a record.
        # resource.set_find_by('Email')

        field_mappings = []

        # Get instance of FieldMapping Class
        field_mapping = FieldMapping()

        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('Email')

        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(0)

        field_mappings.append(field_mapping)

        field_mapping = FieldMapping()

        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('First_Name')

        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(1)

        field_mappings.append(field_mapping)

        field_mapping = FieldMapping()

        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('Last_Name')

        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(2)

        field_mappings.append(field_mapping)

        field_mapping = FieldMapping()

        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('Phone')

        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(3)

        field_mappings.append(field_mapping)

        field_mapping = FieldMapping()

        field_mapping.set_api_name('Website')

        default_value = dict()

        default_value["value"] = "www.zohoapis.com"

        # To set the default value for an empty column in the uploaded file.
        field_mapping.set_default_value(default_value)

        field_mappings.append(field_mapping)

        resource.set_field_mappings(field_mappings)

        resources.append(resource)

        # Set the list of resources to RequestWrapper instance
        request.set_resource(resources)

        # Call create_bulk_write_job method that takes RequestWrapper instance as parameter
        response = bulk_write_operations.create_bulk_write_job(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected SuccessResponse instance is received.
                if isinstance(response_object, SuccessResponse):

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
    def get_bulk_write_job_details(job_id):

        """
        This method is used to get the details of a bulk write job performed previously.
        :param job_id: The unique ID of the bulk write job.
        """

        """
        example
        job_id = 3477061000005615003
        """

        # Get instance of BulkWriteOperations Class
        bulk_write_operations = BulkWriteOperations()

        # Call get_bulk_write_job_details method that takes job_id as parameter
        response = bulk_write_operations.get_bulk_write_job_details(job_id)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected BulkWriteResponse instance is received
                if isinstance(response_object, BulkWriteResponse):

                    # Get the Job Status of the bulkWriteResponse
                    print("Bulk write Job Status: " + response_object.get_status())

                    # Get the CharacterEncoding of the bulkWriteResponse
                    print("Bulk write CharacterEncoding: " + response_object.get_character_encoding())

                    resources = response_object.get_resource()

                    if resources is not None:
                        for resource in resources:
                            # Get the Status of each Resource
                            print("Bulk write Resource Status: " + resource.get_status().get_value())

                            # Get the Type of each Resource
                            print("Bulk write Resource Type: " + resource.get_type().get_value())

                            # Get the Module of each Resource
                            print("Bulk write Resource Module: " + resource.get_module())

                            # Get the field mappings
                            field_mappings = resource.get_field_mappings()

                            if field_mappings is not None:
                                for field_mapping in field_mappings:
                                    # Get the APIName of each FieldMapping
                                    print("Bulk write Resource FieldMapping Module: " + field_mapping.get_api_name())

                                    if field_mapping.get_index() is not None:
                                        # Get the Index of each FieldMapping
                                        print("Bulk write Resource FieldMapping Index: " + str(field_mapping.get_index()))

                                    if field_mapping.get_format() is not None:
                                        # Get the Format of each FieldMapping
                                        print("Bulk write Resource FieldMapping Format: " + field_mapping.get_format())

                                    if field_mapping.get_find_by() is not None:
                                        # Get the FindBy of each FieldMapping
                                        print("Bulk write Resource FieldMapping FindBy: " + field_mapping.get_find_by())

                                    if field_mapping.get_default_value() is not None:
                                        print('Default values')

                                        for key, value in field_mapping.get_default_value().items():
                                            print(key + ": " + str(value))

                            # Get the file
                            file = resource.get_file()

                            if file is not None:
                                # Get the Status of the File
                                print("Bulk write Resource File Status: " + file.get_status().get_value())

                                # Get the Name of the File
                                print("Bulk write Resource File Name: " + file.get_name())

                                # Get the AddedCount of the File
                                print("Bulk write Resource File AddedCount: " + str(file.get_added_count()))

                                # Get the SkippedCount of the File
                                print("Bulk write Resource File SkippedCount: " + str(file.get_skipped_count()))

                                # Get the UpdatedCount of the File
                                print("Bulk write Resource File UpdatedCount: " + str(file.get_updated_count()))

                                # Get the TotalCount of the File
                                print("Bulk write Resource File TotalCount: " + str(file.get_total_count()))

                    callback = response_object.get_callback()

                    if callback is not None:
                        # Get the CallBack Url
                        print("Bulk write CallBack Url: " + callback.get_url())

                        # Get the CallBack Method
                        print("Bulk write CallBack Method: " + callback.get_method().get_value())

                    # Get the ID of the BulkWriteResponse
                    print("Bulk write ID: " + str(response_object.get_id()))

                    result = response_object.get_result()

                    if result is not None:
                        # Get the DownloadUrl of the Result
                        print("Bulk write DownloadUrl: " + result.get_download_url())

                    # Get the CreatedBy User instance of the BulkWriteResponse
                    created_by = response_object.get_created_by()

                    # Check if created_by is not None
                    if created_by is not None:
                        # Get the Name of the created_by User
                        print("Bulkwrite Created By - Name: " + created_by.get_name())

                        # Get the ID of the created_by User
                        print("Bulkwrite Created By - ID: " + str(created_by.get_id()))

                    # Get the Operation of the BulkWriteResponse
                    print("Bulk write Operation: " + response_object.get_operation())

                    # Get the CreatedTime of the BulkWriteResponse
                    print("Bulk write File CreatedTime: " + str(response_object.get_created_time()))

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
    def download_bulk_write_result(download_url, destination_folder):

        """
        This method is used to download the result of bulk write job.
        :param download_url: The URL present in the download_url key in the response of Get Bulk Write Job Details.
        :param destination_folder: The absolute path where downloaded file has to be stored.
        """

        """
        example
        download_url = "https://download-accl.zoho.com/v2/crm/6735/bulk-write/347706122009/347706122009.zip"
        destination_folder = "/Users/user_name/Documents"
        """

        # Get instance of BulkWriteOperations Class
        bulk_write_operations = BulkWriteOperations()

        # Call download_bulk_write_result method that takes download_url as parameter
        response = bulk_write_operations.download_bulk_write_result(download_url)

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

                    # Construct the file name by joining the destination_folder and the name from StreamWrapper instance
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
