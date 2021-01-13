from datetime import datetime
from zcrmsdk.src.com.zoho.crm.api.notes import *
from zcrmsdk.src.com.zoho.crm.api.record import Record
from zcrmsdk.src.com.zoho.crm.api import HeaderMap, ParameterMap
from zcrmsdk.src.com.zoho.crm.api.notes.note import Note as ZCRMNote


class Note(object):

    @staticmethod
    def get_notes():

        """
        This method is used to get the list of notes and print the response.
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Notes
        param_instance.add(GetNotesParam.page, 1)

        param_instance.add(GetNotesParam.per_page, 200)

        param_instance.add(GetNotesParam.fields, "id")

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        header_instance.add(GetNotesHeader.if_modified_since, datetime.fromisoformat('2019-06-01T00:00:00+05:30'))

        # Call get_notes method that takes paramInstance and headerInstance as parameters
        response = notes_operations.get_notes(param_instance, header_instance)

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

                    # Get the list of obtained Note instances
                    notes_list = response_object.get_data()

                    for note in notes_list:
                        # Get the Id of each Note
                        print("Note Id: " + str(note.get_id()))

                        # Get the NoteTitle of each Note
                        print("Note NoteTitle: " + str(note.get_note_title()))

                        # Get the NoteContent of each Note
                        print("Note NoteContent: " + str(note.get_note_content()))

                        # Get the owner User instance of each Note
                        owner = note.get_owner()

                        # Check if owner is not None
                        if owner is not None:
                            # Get the Name of the Owner
                            print("Note Owner - Name: " + str(owner.get_name()))

                            # Get the ID of the Owner
                            print("Note Owner - ID: " + str(owner.get_id()))

                            # Get the Email of the Owner
                            print("Note Owner - Email: " + str(owner.get_email()))

                        # Get the ModifiedTime of each Note
                        if note.get_modified_time() is not None:
                            print("Note ModifiedTime: " + str(note.get_modified_time()))

                        # Get the list of Attachment instances of each Note
                        attachments = note.get_attachments()

                        # Check if attachments is not None
                        if attachments is not None:
                            for attachment in attachments:
                                Note.print_attachment(attachment)

                        # Get the CreatedTime of each Note
                        print("Note CreatedTime: " + str(note.get_created_time()))

                        # Get the parentId Record instance of each Note
                        parent_id = note.get_parent_id()

                        # Check if parent_id is not None
                        if parent_id is not None:

                            # Get the parent record Name of each Note
                            if parent_id.get_key_value('name') is not None:
                                print('Note parent record Name: ' + str(parent_id.get_key_value('name')))

                            # Get the parent record ID of each Note
                            print('Note parent record ID: ' + str(parent_id.get_id()))

                        # Get the Editable of each Note
                        print("Note Editable: " + str(note.get_editable()))

                        # Get the SeModule of each Note
                        print("Note SeModule: " + str(note.get_se_module()))

                        # Get the IsSharedToClient of each Note
                        print("Note IsSharedToClient: " + str(note.get_is_shared_to_client()))

                        # Get the modifiedBy User instance of each Note
                        modified_by = note.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Note Modified By - Name: " + str(modified_by.get_name()))

                            # Get the ID of the modifiedBy User
                            print("Note Modified By - ID: " + str(modified_by.get_id()))

                            # Get the Email of the modifiedBy User
                            print("Note Modified By - Email: " + str(modified_by.get_email()))

                        # Get the Size of each Note
                        print("Note Size: " + str(note.get_size()))

                        # Get the State of each Note
                        print("Note State: " + str(note.get_state()))

                        # Get the VoiceNote of each Note
                        print("Note VoiceNote: " + str(note.get_voice_note()))

                        # Get the createdBy User instance of each Note
                        created_by = note.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Note Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Note Created By - ID: " + str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("Note Created By - Email: " + created_by.get_email())

                    # Get the Info object from obtained response
                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage of the Info
                            print('Note Info PerPage: ' + str(info.get_per_page()))

                        if info.get_count() is not None:
                            # Get the Count of the Info
                            print('Note Info Count: ' + str(info.get_count()))

                        if info.get_page() is not None:
                            # Get the Page of the Info
                            print('Note Info Page: ' + str(info.get_page()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords of the Info
                            print('Note Info MoreRecords: ' + str(info.get_more_records()))

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
    def get_note(note_id):

        """
        This method is used to get the note with id and print the response.
        :param note_id: The ID of the Note to be obtained
        """

        """
        example
        note_id = 3409643000000549003
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters of Get Note Operation
        param_instance.add(GetNoteParam.fields, "id,Note_Content")

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers of Get Note Operation
        header_instance.add(GetNoteHeader.if_modified_since, datetime(2020, 6, 6, 10, 11, 12))

        # Call get_note method that takes note_id, ParameterMap instance, HeaderMap instance as parameter
        response = notes_operations.get_note(note_id, param_instance, header_instance)

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

                    # Get the list of obtained Note instances
                    notes_list = response_object.get_data()

                    for note in notes_list:
                        # Get the Id of each Note
                        print("Note Id: " + str(note.get_id()))

                        # Get the NoteTitle of each Note
                        print("Note NoteTitle: " + str(note.get_note_title()))

                        # Get the NoteContent of each Note
                        print("Note NoteContent: " + str(note.get_note_content()))

                        # Get the owner User instance of each Note
                        owner = note.get_owner()

                        # Check if owner is not None
                        if owner is not None:
                            # Get the Name of the Owner
                            print("Note Owner - Name: " + str(owner.get_name()))

                            # Get the ID of the Owner
                            print("Note Owner - ID: " + str(owner.get_id()))

                            # Get the Email of the Owner
                            print("Note Owner - Email: " + str(owner.get_email()))

                        # Get the ModifiedTime of each Note
                        if note.get_modified_time() is not None:
                            print("Note ModifiedTime: " + str(note.get_modified_time()))

                        # Get the list of Attachment instances of each Note
                        attachments = note.get_attachments()

                        # Check if attachments is not None
                        if attachments is not None:
                            for attachment in attachments:
                                Note.print_attachment(attachment)

                        # Get the CreatedTime of each Note
                        print("Note CreatedTime: " + str(note.get_created_time()))

                        # Get the parentId Record instance of each Note
                        parent_id = note.get_parent_id()

                        # Check if parent_id is not None
                        if parent_id is not None:

                            # Get the parent record Name of each Note
                            if parent_id.get_key_value('name') is not None:
                                print('Note parent record Name: ' + str(parent_id.get_key_value('name')))

                            # Get the parent record ID of each Note
                            print('Note parent record ID: ' + str(parent_id.get_id()))

                        # Get the Editable of each Note
                        print("Note Editable: " + str(note.get_editable()))

                        # Get the SeModule of each Note
                        print("Note SeModule: " + str(note.get_se_module()))

                        # Get the IsSharedToClient of each Note
                        print("Note IsSharedToClient: " + str(note.get_is_shared_to_client()))

                        # Get the modifiedBy User instance of each Note
                        modified_by = note.get_modified_by()

                        # Check if owner is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Note Modified By - Name: " + str(modified_by.get_name()))

                            # Get the ID of the modifiedBy User
                            print("Note Modified By - ID: " + str(modified_by.get_id()))

                            # Get the Email of the modifiedBy User
                            print("Note Modified By - Email: " + str(modified_by.get_email()))

                        # Get the Size of each Note
                        print("Note Size: " + str(note.get_size()))

                        # Get the State of each Note
                        print("Note State: " + str(note.get_state()))

                        # Get the VoiceNote of each Note
                        print("Note VoiceNote: " + str(note.get_voice_note()))

                        # Get the createdBy User instance of each Note
                        created_by = note.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Note Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Note Created By - ID: " + created_by.get_id())

                            # Get the Email of the created_by User
                            print("Note Created By - Email: " + created_by.get_email())

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
    def create_notes():

        """
        This method is used to add new notes and print the response.
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Note instances
        notes_list = []

        for i in range(0, 4):

            # Get instance of Note Class
            note = ZCRMNote()

            # Set Note Content of the Note
            note.set_note_content("Need to do further tracking")

            # Set Note Title of the Note
            note.set_note_title('Contacted python' + str(i))

            # Get instance of Record Class
            parent_record = Record()

            # Set ID of the Record
            parent_record.set_id(3409643000002267003)

            # Set ParentId of the Note
            note.set_parent_id(parent_record)

            # Set SeModule of the Record
            note.set_se_module('Leads')

            notes_list.append(note)

        # Set the list to notes in BodyWrapper instance
        request.set_data(notes_list)

        # Call create_notes method that takes BodyWrapper instance as parameter
        response = notes_operations.create_notes(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
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
    def update_notes():

        """
        This method is used to update existing notes with Ids and print the response.
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Note instances
        notes_list = []

        # Get instance of Note Class
        note_1 = ZCRMNote()

        # Set Note Content of the Note
        note_1.set_note_content("Need to do further tracking 12")

        # Set Note Title of the Note
        note_1.set_note_title('Contacted 12')

        # Set ID to Note
        note_1.set_id(3409643000002193004)

        # Add Note instance to the list
        notes_list.append(note_1)

        # Get instance of Note Class
        note_2 = ZCRMNote()

        # Set Note Content of the Note
        note_2.set_note_content("Need to do further tracking 13")

        # Set Note Title of the Note
        note_2.set_note_title('Contacted 13')

        # Set ID to Note
        note_2.set_id(3409643000001930001)

        # Add Note instance to the list
        notes_list.append(note_2)

        # Set the list to notes in BodyWrapper instance
        request.set_data(notes_list)

        # Call update_notes method that takes BodyWrapper instance as parameter
        response = notes_operations.update_notes(request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
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
    def update_note(note_id):

        """
        This method is used to update an existing note and print the response.
        :param note_id: The ID of the Note to be updated
        """

        """
        example
        note_id = 3409643000002193004
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Note instances
        notes_list = []

        # Get instance of Note Class
        note_1 = ZCRMNote()

        # Set Note Content of the Note
        note_1.set_note_content("Need to do further tracking 12")

        # Set Note Title of the Note
        note_1.set_note_title('Contacted 12')

        # Add Note instance to the list
        notes_list.append(note_1)

        # Set the list to notes in BodyWrapper instance
        request.set_data(notes_list)

        # Call update_note method that takes note_id and BodyWrapper instance as parameter
        response = notes_operations.update_note(note_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
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
    def delete_notes(note_ids):

        """
        This method is used to delete notes in bulk and print the response.
        :param note_ids: The list of Note IDs to be deleted
        """

        """
        example
        note_ids = [3409643000000648001, 3409643000000648005]
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Add the ids to ParameterMap instance
        for note_id in note_ids:
            param_instance.add(DeleteNotesParam.ids, note_id)

        # Call delete_notes method that takes param_instance as parameter
        response = notes_operations.delete_notes(param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
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
    def delete_note(note_id):

        """
        This method is used to delete a single note with ID and print the response.
        :param note_id: The ID of the note to be deleted
        """

        """
        example
        note_id = 3409643000000549003
        """

        # Get instance of NotesOperations Class
        notes_operations = NotesOperations()

        # Call delete_note method that takes note_id as parameter
        response = notes_operations.delete_note(note_id)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
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
    def print_attachment(attachment):
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
            print("Attachment parent record Name: " + str(parent_id.get_key_value("name")))

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
        print("Attachment State: " + attachment.get_state())

        # Get the modifiedBy User instance of each attachment
        created_by = attachment.get_created_by()

        # Check if created_by is not None
        if created_by is not None:
            # Get the Name of the created_by User
            print("Attachment Created By - Name: " + created_by.get_name())

            # Get the ID of the created_by User
            print("Attachment Created By - ID: " + str(created_by.get_id()))

            # Get the Email of the created_by User
            print("Attachment Created By - Email: " + created_by.get_email())

        # Get the linkUrl of each attachment
        print("Attachment LinkUrl: " + str(attachment.get_link_url()))