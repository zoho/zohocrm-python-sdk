from zcrmsdk.src.com.zoho.crm.api.related_lists import *


class RelatedList(object):

    @staticmethod
    def get_related_lists(module_api_name):

        """
        This method is used to get the related list data of a particular module and print the response.
        :param module_api_name: The API Name of the module to get related lists
        """

        """
        example
        module_api_name = "Leads";
        """

        # Get instance of RelatedListsOperations Class that takes module_api_name as parameter
        related_lists_operations = RelatedListsOperations(module_api_name)

        # Call get_related_lists method
        response = related_lists_operations.get_related_lists()

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

                    # Get the list of obtained RelatedList instances
                    related_lists = response_object.get_related_lists()

                    for related_list in related_lists:

                        # Get the SequenceNumber of each RelatedList
                        print("RelatedList SequenceNumber: " + str(related_list.get_sequence_number()))

                        # Get the DisplayLabel of each RelatedList
                        print("RelatedList DisplayLabel: " + str(related_list.get_display_label()))

                        # Get the APIName of each RelatedList
                        print("RelatedList APIName: " + str(related_list.get_api_name()))

                        # Get the Module of each RelatedList
                        print("RelatedList Module: " + str(related_list.get_module()))

                        # Get the Name of each RelatedList
                        print("RelatedList Name: " + str(related_list.get_name()))

                        # Get the Action of each RelatedList
                        print("RelatedList Action: " + str(related_list.get_action()))

                        # Get the ID of each RelatedList
                        print("RelatedList ID: " + str(related_list.get_id()))

                        # Get the Href of each RelatedList
                        print("RelatedList Href: " + str(related_list.get_href()))

                        # Get the Type of each RelatedList
                        print("RelatedList Type: " + str(related_list.get_type()))

                        # Get the Connected Module of each RelatedList
                        print("RelatedList Connectedmodule: " + str(related_list.get_connectedmodule()))

                        # Get the Linking Module of each RelatedList
                        print("RelatedList Linkingmodule: " + str(related_list.get_linkingmodule()))

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
    def get_related_list(module_api_name, related_list_id):

        """
        This method is used to get the single related list data of a particular module with relatedListId and print the response.
        :param module_api_name: The API Name of the module to get related list
        :param related_list_id: The ID of the relatedList to be obtained
        """

        """
        example
        module_api_name = "Contacts"
        related_list_id = 3409643000000062003
        """

        # Get instance of RelatedListsOperations Class that takes module_api_name as parameter
        related_lists_operations = RelatedListsOperations(module_api_name)

        # Call get_related_list method which takes related_list_id as parameter
        response = related_lists_operations.get_related_list(related_list_id)

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

                    # Get the list of obtained RelatedList instances
                    related_lists = response_object.get_related_lists()

                    for related_list in related_lists:
                        # Get the SequenceNumber of each RelatedList
                        print("RelatedList SequenceNumber: " + str(related_list.get_sequence_number()))

                        # Get the DisplayLabel of each RelatedList
                        print("RelatedList DisplayLabel: " + str(related_list.get_display_label()))

                        # Get the APIName of each RelatedList
                        print("RelatedList APIName: " + str(related_list.get_api_name()))

                        # Get the Module of each RelatedList
                        print("RelatedList Module: " + str(related_list.get_module()))

                        # Get the Name of each RelatedList
                        print("RelatedList Name: " + str(related_list.get_name()))

                        # Get the Action of each RelatedList
                        print("RelatedList Action: " + str(related_list.get_action()))

                        # Get the ID of each RelatedList
                        print("RelatedList ID: " + str(related_list.get_id()))

                        # Get the Href of each RelatedList
                        print("RelatedList Href: " + str(related_list.get_href()))

                        # Get the Type of each RelatedList
                        print("RelatedList Type: " + str(related_list.get_type()))

                        # Get the Connected Module of each RelatedList
                        print("RelatedList Connectedmodule: " + str(related_list.get_connectedmodule()))

                        # Get the Linking Module of each RelatedList
                        print("RelatedList Linkingmodule: " + str(related_list.get_linkingmodule()))

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