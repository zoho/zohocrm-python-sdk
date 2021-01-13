from zcrmsdk.src.com.zoho.crm.api.attachments import *
from zcrmsdk.src.com.zoho.crm.api.util import StreamWrapper
from zcrmsdk.src.com.zoho.crm.api import ParameterMap
import os


class Attachment(object):

    @staticmethod
    def get_attachments(module_api_name, record_id):
        """
        This method is used to get a single record's attachments' details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to get attachments
        """

        """
        example
        module_api_name = 'Leads'
        record_id = 3409643000002267003
        """

        # Get instance of AttachmentsOperations Class that takes module_api_name and record_id as parameters
        attachments_operations = AttachmentsOperations(module_api_name, record_id)

        # Possible parameters for Get Attachments Operation
        param_instance = ParameterMap()

        param_instance.add(GetAttachmentsParam.fields, "id")

        param_instance.add(GetAttachmentsParam.page, 2)

        param_instance.add(GetAttachmentsParam.per_page, 10)

        # Call get_attachments method that takes ParameterMap instance as parameter
        response = attachments_operations.get_attachments(param_instance)

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
                    attachments_list = response_object.get_data()

                    for attachment in attachments_list:
                        # Get the ID of each attachment
                        print('Attachment ID : ' + str(attachment.get_id()))

                        # Get the owner User instance of each attachment
                        owner = attachment.get_owner()

                        # Check if owner is not None
                        if owner is not None:
                            # Get the Name of the Owner
                            print("Attachment Owner - Name: " + owner.get_name())

                            # Get the ID of the Owner
                            print("Attachment Owner - ID: " + str(owner.get_id()))

                            # Get the Email of the Owner
                            print("Attachment Owner - Email: " + owner.get_email())

                        # Get the modified time of each attachment
                        print("Attachment Modified Time: " + str(attachment.get_modified_time()))

                        # Get the name of the File
                        print("Attachment File Name: " + str(attachment.get_file_name()))

                        # Get the created time of each attachment
                        print("Attachment Created Time: " + str(attachment.get_created_time()))

                        # Get the Attachment file size
                        print("Attachment File Size: " + str(attachment.get_size()))

                        # Get the parentId Record instance of each attachment
                        parent_id = attachment.get_parent_id()

                        if parent_id is not None:
                            # Get the parent record Name of each attachment
                            print("Attachment parent record Name: " + parent_id.get_key_value("name"))

                            # Get the parent record ID of each attachment
                            print("Attachment parent record ID: " + str(parent_id.get_id()))

                        # Check if the attachment is Editable
                        print("Attachment is Editable: " + str(attachment.get_editable()))

                        # Get the file ID of each attachment
                        print("Attachment File ID: " + str(attachment.get_file_id()))

                        # Get the type of each attachment
                        print("Attachment File Type: " + str(attachment.get_type()))

                        # Get the seModule of each attachment
                        print("Attachment seModule: " + str(attachment.get_se_module()))

                        # Get the modifiedBy User instance of each attachment
                        modified_by = attachment.get_modified_by()

                        # Check if modifiedBy is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Attachment Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Attachment Modified By - ID: " + str(modified_by.get_id()))

                            # Get the Email of the modifiedBy User
                            print("Attachment Modified By - Email: " + modified_by.get_email())

                        # Get the state of each attachment
                        print("Attachment State: " + str(attachment.get_state()))

                        # Get the modifiedBy User instance of each attachment
                        created_by = attachment.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Attachment Created By - Name: " + created_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Attachment Created By - ID: " + str(created_by.get_id()))

                            # Get the Email of the modifiedBy User
                            print("Attachment Created By - Email: " + created_by.get_email())

                        # Get the linkUrl of each attachment
                        print("Attachment LinkUrl: " + str(attachment.get_link_url()))

                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('Record Info PerPage: ' + str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('Record Info Page: ' + str(info.get_page()))

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

                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def upload_attachments(module_api_name, record_id, absolute_file_path):

        """
        This method is used to upload attachments and print the response
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to upload attachment
        :param absolute_file_path: The absolute file path of the file to be attached
        """

        """
        example
        module_api_name= "Leads"
        record_id = 3409643000002267003
        absolute_file_path = "/Users/user-name/Documents/image.jpg";
        """

        # Get instance of AttachmentsOperations Class that takes module_api_name and record_id as parameters
        attachments_operations = AttachmentsOperations(module_api_name, record_id)

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

        # Call upload_attachment method that takes FileBodyWrapper instance as parameter
        response = attachments_operations.upload_attachment(file_body_wrapper)

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
    def delete_attachments(module_api_name, record_id, attachment_ids):

        """
        This method is used to Delete attachments of a single record with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to delete attachments
        :param attachment_ids: The list of attachment IDs to be deleted
        """

        """
        example
        module_api_name= "Leads"
        record_id = 3409643000002267003
        attachment_ids = [3409643000002267012, 3409643000002267018, 3409643000002267010]
        """

        # Get instance of AttachmentsOperations Class that takes module_api_name and record_id as parameter
        attachments_operations = AttachmentsOperations(module_api_name, record_id)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Add the ids to parameter map instance
        for attachment_id in attachment_ids:
            param_instance.add(DeleteAttachmentsParam.ids, attachment_id)

        # Call delete_attachments method that takes paramInstance as parameter
        response = attachments_operations.delete_attachments(param_instance)

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
    def download_attachment(module_api_name, record_id, attachment_id, destination_folder):

        """
        This method is used to download an attachment of a single record of a module with ID and attachment ID and write the file in the specified destination.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to download attachment
        :param attachment_id: The ID of the attachment to be downloaded
        :param destination_folder: The absolute path of the destination folder to store the attachment
        """

        """
        example
        module_api_name = "Leads";
        record_id = 3409643000002267003
        attachment_id = 3409643000002267024
        destination_folder = "/Users/user-name/Desktop";
        """

        # Get instance of AttachmentsOperations Class that takes module_api_name and record_id as parameter
        attachments_operations = AttachmentsOperations(module_api_name, record_id)

        # Call download_attachment method that takes attachment_id as parameters
        response = attachments_operations.download_attachment(attachment_id)

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
    def delete_attachment(module_api_name, record_id, attachment_id):

        """
        This method is used to delete an attachment of a single record with ID and attachment ID and print the response
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to delete attachment
        :param attachment_id: The ID of the attachment to be deleted
        """

        """
        example
        module_api_name = "Leads";
        record_id = 3409643000002267003
        attachment_id = 3409643000002267024
        """

        # Get instance of AttachmentsOperations Class that takes module_api_name and record_id as parameters
        attachments_operations = AttachmentsOperations(module_api_name, record_id)

        # Call delete_attachment method that takes attachment_id as parameter
        response = attachments_operations.delete_attachment(attachment_id)

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
    def upload_link_attachment(module_api_name, record_id, attachment_url):

        """
        This method is used to upload link attachment and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to upload Link attachment
        :param attachment_url: The attachment url of the doc or image link to be attached
        """

        """
        example
        module_api_name = "Leads";
        record_id = 3409643000002267003
        attachment_url = "https://5.imimg.com/data5/KJ/UP/MY-8655440/zoho-crm-500x500.png";
        """

        # Get instance of AttachmentsOperations Class that takes module_api_name and record_id as parameter
        attachments_operations = AttachmentsOperations(module_api_name, record_id)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Add the attachment_url to parameter Instance
        param_instance.add(UploadLinkAttachmentParam.attachmenturl, attachment_url)

        # Call upload_link_attachment method that takes ParameterMap instance as parameter
        response = attachments_operations.upload_link_attachment(param_instance)

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
