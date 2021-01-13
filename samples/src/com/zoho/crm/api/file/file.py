import os
from zcrmsdk.src.com.zoho.crm.api.file import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap
from zcrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class File(object):

    @staticmethod
    def upload_files():

        """
        This method is used to upload files and print the response.
        """

        # Get instance of FileOperations Class
        file_operations = FileOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of UploadFile operation
        param_instance.add(UploadFilesParam.type, "inline")

        # Get instance of FileBodyWrapper Class that will contain the request body
        request = BodyWrapper()

        """
        StreamWrapper can be initialized in any of the following ways

        * param 1 -> fileName 
        * param 2 -> Read Stream.
        """
        stream_wrapper1 = StreamWrapper(stream=open("/Users/user_name/Desktop/file1.txt", 'rb'))

        """
        * param 1 -> fileName
        * param 2 -> Read Stream
        * param 3 -> Absolute File Path of the file to be attached
        """

        stream_wrapper2 = StreamWrapper(file_path="/Users/user_name/Desktop/file2.txt")

        stream_wrapper3 = StreamWrapper(file_path="/Users/user_name/Desktop/file3.txt")

        # Set list of files to the BodyWrapper instance
        request.set_file([stream_wrapper1, stream_wrapper2, stream_wrapper3])

        # Call upload_files method that takes BodyWrapper instance and ParameterMap instance as parameter.
        response = file_operations.upload_files(request, param_instance)

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
    def get_file(id, destination_folder):

        """
        This method is used to download the file with ID and write in the destinationFolder
        :param id: The ID of the uploaded File.
        :param destination_folder: The absolute path of the destination folder to store the File
        """

        """
        example
		id = "ae9c7cefa418aec1d6a5cc2d9ab35c3231aae3bfeef7d5e00a54b7563c0dd42b";
        destination_folder = "/Users/user_name/Desktop"
        """

        # Get instance of FileOperations Class
        file_operations = FileOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Add the id to ParameterMap instance
        param_instance.add(GetFileParam.id, id)

        # Call get_file method that takes ParameterMap instance as parameter
        response = file_operations.get_file(param_instance)

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
