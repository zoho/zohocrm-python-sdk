import os
from datetime import datetime
from zcrmsdk.src.com.zoho.crm.api.related_records import *
from zcrmsdk.src.com.zoho.crm.api.attachments import Attachment
from zcrmsdk.src.com.zoho.crm.api.record import Comment, Consent, Record, FileDetails, Participants, LineTax, InventoryLineItems, RemindAt, Reminder, PricingDetails, RecurringActivity
from zcrmsdk.src.com.zoho.crm.api.tags import Tag
from zcrmsdk.src.com.zoho.crm.api.layouts import Layout
from zcrmsdk.src.com.zoho.crm.api.users import User
from zcrmsdk.src.com.zoho.crm.api import HeaderMap, ParameterMap
from zcrmsdk.src.com.zoho.crm.api.util import Choice


class RelatedRecord(object):

    @staticmethod
    def get_related_records(module_api_name, record_id, related_list_api_name):

        """
        This method is used to get the related list records and print the response.
        :param module_api_name: The API Name of the module to get related records.
        :param record_id: The ID of the record to be obtain related records
        :param related_list_api_name: The API name of the related list
        """

        """
        example
        module_api_name = "Products"
        record_id = 3409643000000798007
        related_list_api_name = "Price_Books"
        """

        # Get instance of RelatedRecordsOperations Class that takes moduleAPIName, recordId and relatedListAPIName as parameter
        related_records_operations = RelatedRecordsOperations(related_list_api_name, record_id, module_api_name)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Related Records operation
        param_instance.add(GetRelatedRecordsParam.page, 1)

        param_instance.add(GetRelatedRecordsParam.per_page, 100)

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Related Records operation
        # header_instance.add(GetRelatedRecordsHeader.if_modified_since, datetime.fromisoformat('2019-10-15T05:00:00+05:30'))

        # Call getRelatedRecords method that takes ParameterMap instance and HeaderMap instance as parameter
        response = related_records_operations.get_related_records(param_instance, header_instance)

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
                        # Get the ID of each RelatedRecord
                        print("RelatedRecord ID: " + str(record.get_id()))

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("RelatedRecord Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("RelatedRecord Created By - ID: " + str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("RelatedRecord Created By - Email: " + created_by.get_email())

                        # Get the CreatedTime of each RelatedRecord
                        print("RelatedRecord CreatedTime: " + str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each RelatedRecord
                            print("RelatedRecord ModifiedTime: " + str(record.get_modified_time()))

                        # Get the modified_by User instance of each RelatedRecord
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("RelatedRecord Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("RelatedRecord Modified By - ID: " + str(modified_by.get_id()))

                            # Get the Email of the modified_by User
                            print("RelatedRecord Modified By - Email: " + modified_by.get_email())

                        # Get the list of obtained Tag instance of each RelatedRecord
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("RelatedRecord Tag Name: " + tag.get_name())

                                # Get the Id of each Tag
                                print("RelatedRecord Tag ID: " + str(tag.get_id()))

                        # To get particular field value
                        print("RelatedRecord Field Value: " + str(record.get_key_value('Last_Name')))

                        print('RelatedRecord KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):

                                if len(value) > 0:

                                    if isinstance(value[0], FileDetails):
                                        file_details = value

                                        for file_detail in file_details:
                                            # Get the Extn of each FileDetails
                                            print("RelatedRecord FileDetails Extn: " + file_detail.get_extn())

                                            # Get the IsPreviewAvailable of each FileDetails
                                            print("RelatedRecord FileDetails IsPreviewAvailable: " + str(file_detail.get_is_preview_available()))

                                            # Get the DownloadUrl of each FileDetails
                                            print("RelatedRecord FileDetails DownloadUrl: " + file_detail.get_download_url())

                                            # Get the DeleteUrl of each FileDetails
                                            print("RelatedRecord FileDetails DeleteUrl: " + file_detail.get_delete_url())

                                            # Get the EntityId of each FileDetails
                                            print("RelatedRecord FileDetails EntityId: " + file_detail.get_entity_id())

                                            # Get the Mode of each FileDetails
                                            print("RelatedRecord FileDetails Mode: " + file_detail.get_mode())

                                            # Get the OriginalSizeByte of each FileDetails
                                            print("RelatedRecord FileDetails OriginalSizeByte: " + file_detail.get_original_size_byte())

                                            # Get the PreviewUrl of each FileDetails
                                            print("RelatedRecord FileDetails PreviewUrl: " + file_detail.get_preview_url())

                                            # Get the FileName of each FileDetails
                                            print("RelatedRecord FileDetails FileName: " + file_detail.get_file_name())

                                            # Get the FileId of each FileDetails
                                            print("RelatedRecord FileDetails FileId: " + file_detail.get_file_id())

                                            # Get the AttachmentId of each FileDetails
                                            print("RelatedRecord FileDetails AttachmentId: " + file_detail.get_attachment_id())

                                            # Get the FileSize of each FileDetails
                                            print("RelatedRecord FileDetails FileSize: " + file_detail.get_file_size())

                                            # Get the CreatorId of each FileDetails
                                            print("RelatedRecord FileDetails CreatorId: " + file_detail.get_creator_id())

                                            # Get the LinkDocs of each FileDetails
                                            print("RelatedRecord FileDetails LinkDocs: " + file_detail.get_link_docs())

                                    elif isinstance(value[0], Reminder):
                                        reminders = value

                                        for reminder in reminders:
                                            # Get the Reminder Period
                                            print("RelatedRecord Reminder Period: " + reminder.get_period())

                                            # Get the Reminder Unit
                                            print("RelatedRecord Reminder Unit: " + reminder.get_unit())

                                    elif isinstance(value[0], Choice):
                                        choice_list = value

                                        print(key_name)

                                        print('Values')

                                        for choice in choice_list:
                                            print(choice.get_value())

                                    elif isinstance(value[0], Participants):
                                        participants = value

                                        for participant in participants:
                                            print("RelatedRecord Participants Name: " + participant.get_name())

                                            print("RelatedRecord Participants Invited: " + str(participant.get_invited()))

                                            print("RelatedRecord Participants Type: " + participant.get_type())

                                            print("RelatedRecord Participants Participant: " + participant.get_participant())

                                            print("RelatedRecord Participants Status: " + participant.get_status())

                                    elif isinstance(value[0], InventoryLineItems):
                                        product_details = value

                                        for product_detail in product_details:
                                            line_item_product = product_detail.get_product()

                                            if line_item_product is not None:
                                                print("RelatedRecord ProductDetails LineItemProduct ProductCode: " + line_item_product.get_product_code())

                                                print("RelatedRecord ProductDetails LineItemProduct Currency: " + line_item_product.get_currency())

                                                print("RelatedRecord ProductDetails LineItemProduct Name: " + line_item_product.get_name())

                                                print("RelatedRecord ProductDetails LineItemProduct Id: " + str(line_item_product.get_id()))

                                            print("RelatedRecord ProductDetails Quantity: " + str(product_detail.get_quantity()))

                                            print("RelatedRecord ProductDetails Discount: " + product_detail.get_discount())

                                            print("RelatedRecord ProductDetails TotalAfterDiscount: " + str(product_detail.get_total_after_discount()))

                                            print("RelatedRecord ProductDetails NetTotal: " + str(product_detail.get_net_total()))

                                            if product_detail.get_book() is not None:
                                                print("RelatedRecord ProductDetails Book: " + str(product_detail.get_book()))

                                            print("RelatedRecord ProductDetails Tax: " + str(product_detail.get_tax()))

                                            print("RelatedRecord ProductDetails ListPrice: " + str(product_detail.get_list_price()))

                                            print("RelatedRecord ProductDetails UnitPrice: " + str(product_detail.get_unit_price()))

                                            print("RelatedRecord ProductDetails QuantityInStock: " + str(product_detail.get_quantity_in_stock()))

                                            print("RelatedRecord ProductDetails Total: " + str(product_detail.get_total()))

                                            print("RelatedRecord ProductDetails ID: " + str(product_detail.get_id()))

                                            print("RelatedRecord ProductDetails ProductDescription: " + product_detail.get_product_description())

                                            line_taxes = product_detail.get_line_tax()

                                            for line_tax in line_taxes:
                                                print("RelatedRecord ProductDetails LineTax Percentage: " + str(line_tax.get_percentage()))

                                                print("RelatedRecord ProductDetails LineTax Name: " + line_tax.get_name())

                                                print("RelatedRecord ProductDetails LineTax Id: " + str(line_tax.get_id()))

                                                print("RelatedRecord ProductDetails LineTax Value: " + str(line_tax.get_value()))

                                    elif isinstance(value[0], Tag):
                                        tags = value

                                        if tags is not None:
                                            for tag in tags:
                                                print("RelatedRecord Tag Name: " + tag.get_name())

                                                print("RelatedRecord Tag ID: " + str(tag.get_id()))

                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value

                                        for pricing_detail in pricing_details:
                                            print("RelatedRecord PricingDetails ToRange: " + str(pricing_detail.get_to_range()))

                                            print("RelatedRecord PricingDetails Discount: " + str(pricing_detail.get_discount()))

                                            print("RelatedRecord PricingDetails ID: " + str(pricing_detail.get_id()))

                                            print("RelatedRecord PricingDetails FromRange: " + str(pricing_detail.get_from_range()))

                                    elif isinstance(value[0], Record):
                                        record_list = value

                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(str(key) + " : " + str(val))

                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value

                                        for line_tax in line_taxes:
                                            print("RelatedRecord LineTax Percentage: " + str(
                                                line_tax.get_percentage()))

                                            print("RelatedRecord LineTax Name: " + line_tax.get_name())

                                            print("RelatedRecord LineTax Id: " + str(line_tax.get_id()))

                                            print("RelatedRecord LineTax Value: " + str(line_tax.get_value()))

                                    elif isinstance(value[0], Comment):
                                        comments = value

                                        for comment in comments:
                                            print("Comment-ID: " + str(comment.get_id()))

                                            print("Comment-Content: " + comment.get_comment_content())

                                            print("Comment-Commented_By: " + comment.get_commented_by())

                                            print("Comment-Commented Time: " + str(comment.get_commented_time()))

                                    elif isinstance(value[0], Attachment):
                                        attachments = value

                                        for attachment in attachments:
                                            # Get the ID of each attachment
                                            print('Record Attachment ID : ' + str(attachment.get_id()))

                                            # Get the owner User instance of each attachment
                                            owner = attachment.get_owner()

                                            # Check if owner is not None
                                            if owner is not None:
                                                # Get the Name of the Owner
                                                print("Record Attachment Owner - Name: " + owner.get_name())

                                                # Get the ID of the Owner
                                                print("Record Attachment Owner - ID: " + str(owner.get_id()))

                                                # Get the Email of the Owner
                                                print("Record Attachment Owner - Email: " + owner.get_email())

                                            # Get the modified time of each attachment
                                            print("Record Attachment Modified Time: " + str(attachment.get_modified_time()))

                                            # Get the name of the File
                                            print("Record Attachment File Name: " + attachment.get_file_name())

                                            # Get the created time of each attachment
                                            print("Record Attachment Created Time: " + str(attachment.get_created_time()))

                                            # Get the Attachment file size
                                            print("Record Attachment File Size: " + str(attachment.get_size()))

                                            # Get the parentId Record instance of each attachment
                                            parent_id = attachment.get_parent_id()

                                            if parent_id is not None:
                                                # Get the parent record Name of each attachment
                                                print(
                                                    "Record Attachment parent record Name: " + parent_id.get_key_value("name"))

                                                # Get the parent record ID of each attachment
                                                print("Record Attachment parent record ID: " + str(parent_id.get_id()))

                                            # Check if the attachment is Editable
                                            print("Record Attachment is Editable: " + str(attachment.get_editable()))

                                            # Get the file ID of each attachment
                                            print("Record Attachment File ID: " + str(attachment.get_file_id()))

                                            # Get the type of each attachment
                                            print("Record Attachment File Type: " + str(attachment.get_type()))

                                            # Get the seModule of each attachment
                                            print("Record Attachment seModule: " + str(attachment.get_se_module()))

                                            # Get the modifiedBy User instance of each attachment
                                            modified_by = attachment.get_modified_by()

                                            # Check if modifiedBy is not None
                                            if modified_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print("Record Attachment Modified By - Name: " + modified_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print("Record Attachment Modified By - ID: " + str(modified_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print("Record Attachment Modified By - Email: " + modified_by.get_email())

                                            # Get the state of each attachment
                                            print("Record Attachment State: " + attachment.get_state())

                                            # Get the created_by User instance of each attachment
                                            created_by = attachment.get_created_by()

                                            # Check if created_by is not None
                                            if created_by is not None:
                                                # Get the Name of the created_by User
                                                print("Record Attachment Created By - Name: " + created_by.get_name())

                                                # Get the ID of the created_by User
                                                print("Record Attachment Created By - ID: " + str(created_by.get_id()))

                                                # Get the Email of the created_by User
                                                print("Record Attachment Created By - Email: " + created_by.get_email())

                                            # Get the linkUrl of each attachment
                                            print("Record Attachment LinkUrl: " + str(attachment.get_link_url()))

                                    else:
                                        print(key_name)

                                        for each_value in value:
                                            print(str(each_value))

                            elif isinstance(value, User):
                                print("RelatedRecord " + key_name + " User-ID: " + str(value.get_id()))

                                print("RelatedRecord " + key_name + " User-Name: " + value.get_name())

                                print("RelatedRecord " + key_name + " User-Email: " + value.get_email())

                            elif isinstance(value, Layout):
                                print(key_name + " ID: " + str(value.get_id()))

                                print(key_name + " Name: " + value.get_name())

                            elif isinstance(value, Record):
                                print(key_name + " Record ID: " + str(value.get_id()))

                                print(key_name + " Record Name: " + value.get_key_value('name'))

                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())

                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())

                            elif isinstance(value, RecurringActivity):
                                print(key_name)

                                print("RRULE: " + value.get_rrule())

                            elif isinstance(value, Consent):
                                print("Record Consent ID: " + str(value.get_id()))

                                # Get the createdBy User instance of each Record
                                created_by = value.get_created_by()

                                # Check if created_by is not None
                                if created_by is not None:
                                    # Get the Name of the created_by User
                                    print("Record Consent Created By - Name: " + created_by.get_name())

                                    # Get the ID of the created_by User
                                    print("Record Consent Created By - ID: " + created_by.get_id())

                                    # Get the Email of the created_by User
                                    print("Record Consent Created By - Email: " + created_by.get_email())

                                # Get the CreatedTime of each Record
                                print("Record Consent CreatedTime: " + str(value.get_created_time()))

                                if value.get_modified_time() is not None:
                                    # Get the ModifiedTime of each Record
                                    print("Record Consent ModifiedTime: " + str(value.get_modified_time()))

                                # Get the Owner User instance of the Consent
                                owner = value.get_owner()

                                if owner is not None:
                                    # Get the Name of the Owner User
                                    print("Record Consent Created By - Name: " + owner.get_name())

                                    # Get the ID of the Owner User
                                    print("Record Consent Created By - ID: " + owner.get_id())

                                    # Get the Email of the Owner User
                                    print("Record Consent Created By - Email: " + owner.get_email())

                                print("Record Consent ContactThroughEmail: " + str(value.get_contact_through_email()))

                                print("Record Consent ContactThroughSocial: " + str(value.get_contact_through_social()))

                                print("Record Consent ContactThroughSurvey: " + str(value.get_contact_through_survey()))

                                print("Record Consent ContactThroughPhone: " + str(value.get_contact_through_phone()))

                                print("Record Consent MailSentTime: " + str(value.get_mail_sent_time()))

                                print("Record Consent ConsentDate: " + str(value.get_consent_date()))

                                print("Record Consent ConsentRemarks: " + value.get_consent_remarks())

                                print("Record Consent ConsentThrough: " + value.get_consent_through())

                                print("Record Consent DataProcessingBasis: " + value.get_data_processing_basis())

                                # To get custom values
                                print("Record Consent Lawful Reason: " + str(value.get_key_value("Lawful_Reason")))

                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))

                            else:
                                print(key_name + " : " + str(value))

                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('RelatedRecord Info PerPage: ' + str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('RelatedRecord Info Page: ' + str(info.get_page()))

                        if info.get_count() is not None:
                            # Get the Count from Info
                            print('RelatedRecord Info Count: ' + str(info.get_count()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords from Info
                            print('RelatedRecord Info MoreRecords: ' + str(info.get_more_records()))

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
    def get_related_record(module_api_name, record_id, related_list_api_name, related_list_id, destination_folder):

        """
        This method is used to get the single related list record and print the response.
        :param module_api_name: The API Name of the module to get related record.
        :param record_id: The ID of the record to be get Related List.
        :param related_list_api_name: The API name of the related list.
        :param related_list_id: The ID of the related record.
        :param destination_folder : The absolute path of the destination folder to store the related record
        """

        """
        example
        module_api_name = "Products"
        record_id = 3409643000000798007
        related_list_api_name = "Price_Books"
        related_list_id = 3409643000002414001
        destination_folder = "/Users/user_name/Desktop"
        """

        # Get instance of RelatedRecordsOperations Class that takes moduleAPIName, recordId and relatedListAPIName as parameter
        related_records_operations = RelatedRecordsOperations(related_list_api_name, record_id, module_api_name)

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Related Records operation
        header_instance.add(GetRelatedRecordHeader.if_modified_since, datetime.fromisoformat('2019-10-15T05:00:00+05:30'))

        # Call getRelatedRecord method that takes header_instance and related_list_id as parameter
        response = related_records_operations.get_related_record(related_list_id, header_instance)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        # Get the ID of each RelatedRecord
                        print("RelatedRecord ID: " + str(record.get_id()))

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("RelatedRecord Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("RelatedRecord Created By - ID: " + str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("RelatedRecord Created By - Email: " + created_by.get_email())

                        # Get the CreatedTime of each RelatedRecord
                        print("RelatedRecord CreatedTime: " + str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each RelatedRecord
                            print("RelatedRecord ModifiedTime: " + str(record.get_modified_time()))

                        # Get the modified_by User instance of each RelatedRecord
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("RelatedRecord Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("RelatedRecord Modified By - ID: " + str(modified_by.get_id()))

                            # Get the Email of the modified_by User
                            print("RelatedRecord Modified By - Email: " + modified_by.get_email())

                        # Get the list of obtained Tag instance of each RelatedRecord
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("RelatedRecord Tag Name: " + tag.get_name())

                                # Get the Id of each Tag
                                print("RelatedRecord Tag ID: " + str(tag.get_id()))

                        # To get particular field value
                        print("RelatedRecord Field Value: " + str(record.get_key_value('Last_Name')))

                        print('RelatedRecord KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):

                                if len(value) > 0:

                                    if isinstance(value[0], FileDetails):
                                        file_details = value

                                        for file_detail in file_details:
                                            # Get the Extn of each FileDetails
                                            print("RelatedRecord FileDetails Extn: " + file_detail.get_extn())

                                            # Get the IsPreviewAvailable of each FileDetails
                                            print("RelatedRecord FileDetails IsPreviewAvailable: " + str(file_detail.get_is_preview_available()))

                                            # Get the DownloadUrl of each FileDetails
                                            print("RelatedRecord FileDetails DownloadUrl: " + file_detail.get_download_url())

                                            # Get the DeleteUrl of each FileDetails
                                            print("RelatedRecord FileDetails DeleteUrl: " + file_detail.get_delete_url())

                                            # Get the EntityId of each FileDetails
                                            print("RelatedRecord FileDetails EntityId: " + file_detail.get_entity_id())

                                            # Get the Mode of each FileDetails
                                            print("RelatedRecord FileDetails Mode: " + file_detail.get_mode())

                                            # Get the OriginalSizeByte of each FileDetails
                                            print("RelatedRecord FileDetails OriginalSizeByte: " + file_detail.get_original_size_byte())

                                            # Get the PreviewUrl of each FileDetails
                                            print("RelatedRecord FileDetails PreviewUrl: " + file_detail.get_preview_url())

                                            # Get the FileName of each FileDetails
                                            print("RelatedRecord FileDetails FileName: " + file_detail.get_file_name())

                                            # Get the FileId of each FileDetails
                                            print("RelatedRecord FileDetails FileId: " + file_detail.get_file_id())

                                            # Get the AttachmentId of each FileDetails
                                            print("RelatedRecord FileDetails AttachmentId: " + file_detail.get_attachment_id())

                                            # Get the FileSize of each FileDetails
                                            print("RelatedRecord FileDetails FileSize: " + file_detail.get_file_size())

                                            # Get the CreatorId of each FileDetails
                                            print("RelatedRecord FileDetails CreatorId: " + file_detail.get_creator_id())

                                            # Get the LinkDocs of each FileDetails
                                            print("RelatedRecord FileDetails LinkDocs: " + file_detail.get_link_docs())

                                    elif isinstance(value[0], Reminder):
                                        reminders = value

                                        for reminder in reminders:
                                            # Get the Reminder Period
                                            print("RelatedRecord Reminder Period: " + reminder.get_period())

                                            # Get the Reminder Unit
                                            print("RelatedRecord Reminder Unit: " + reminder.get_unit())

                                    elif isinstance(value[0], Choice):
                                        choice_list = value

                                        print(key_name)

                                        print('Values')

                                        for choice in choice_list:
                                            print(choice.get_value())

                                    elif isinstance(value[0], Participants):
                                        participants = value

                                        for participant in participants:
                                            print("RelatedRecord Participants Name: " + participant.get_name())

                                            print("RelatedRecord Participants Invited: " + str(participant.get_invited()))

                                            print("RelatedRecord Participants Type: " + participant.get_type())

                                            print("RelatedRecord Participants Participant: " + participant.get_participant())

                                            print("RelatedRecord Participants Status: " + participant.get_status())

                                    elif isinstance(value[0], InventoryLineItems):
                                        product_details = value

                                        for product_detail in product_details:
                                            line_item_product = product_detail.get_product()

                                            if line_item_product is not None:
                                                print("RelatedRecord ProductDetails LineItemProduct ProductCode: " + line_item_product.get_product_code())

                                                print("RelatedRecord ProductDetails LineItemProduct Currency: " + line_item_product.get_currency())

                                                print("RelatedRecord ProductDetails LineItemProduct Name: " + line_item_product.get_name())

                                                print("RelatedRecord ProductDetails LineItemProduct Id: " + str(line_item_product.get_id()))

                                            print("RelatedRecord ProductDetails Quantity: " + str(product_detail.get_quantity()))

                                            print("RelatedRecord ProductDetails Discount: " + product_detail.get_discount())

                                            print("RelatedRecord ProductDetails TotalAfterDiscount: " + str(product_detail.get_total_after_discount()))

                                            print("RelatedRecord ProductDetails NetTotal: " + str(product_detail.get_net_total()))

                                            if product_detail.get_book() is not None:
                                                print("RelatedRecord ProductDetails Book: " + str(product_detail.get_book()))

                                            print("RelatedRecord ProductDetails Tax: " + str(product_detail.get_tax()))

                                            print("RelatedRecord ProductDetails ListPrice: " + str(product_detail.get_list_price()))

                                            print("RelatedRecord ProductDetails UnitPrice: " + str(product_detail.get_unit_price()))

                                            print("RelatedRecord ProductDetails QuantityInStock: " + str(product_detail.get_quantity_in_stock()))

                                            print("RelatedRecord ProductDetails Total: " + str(product_detail.get_total()))

                                            print("RelatedRecord ProductDetails ID: " + str(product_detail.get_id()))

                                            print("RelatedRecord ProductDetails ProductDescription: " + product_detail.get_product_description())

                                            line_taxes = product_detail.get_line_tax()

                                            for line_tax in line_taxes:
                                                print("RelatedRecord ProductDetails LineTax Percentage: " + str(line_tax.get_percentage()))

                                                print("RelatedRecord ProductDetails LineTax Name: " + line_tax.get_name())

                                                print("RelatedRecord ProductDetails LineTax Id: " + str(line_tax.get_id()))

                                                print("RelatedRecord ProductDetails LineTax Value: " + str(line_tax.get_value()))

                                    elif isinstance(value[0], Tag):
                                        tags = value

                                        if tags is not None:
                                            for tag in tags:
                                                print("RelatedRecord Tag Name: " + tag.get_name())

                                                print("RelatedRecord Tag ID: " + str(tag.get_id()))

                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value

                                        for pricing_detail in pricing_details:
                                            print("RelatedRecord PricingDetails ToRange: " + str(pricing_detail.get_to_range()))

                                            print("RelatedRecord PricingDetails Discount: " + str(pricing_detail.get_discount()))

                                            print("RelatedRecord PricingDetails ID: " + str(pricing_detail.get_id()))

                                            print("RelatedRecord PricingDetails FromRange: " + str(pricing_detail.get_from_range()))

                                    elif isinstance(value[0], Record):
                                        record_list = value

                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(str(key) + " : " + str(val))

                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value

                                        for line_tax in line_taxes:
                                            print("RelatedRecord LineTax Percentage: " + str(
                                                line_tax.get_percentage()))

                                            print("RelatedRecord LineTax Name: " + line_tax.get_name())

                                            print("RelatedRecord LineTax Id: " + line_tax.get_id())

                                            print("RelatedRecord LineTax Value: " + str(line_tax.get_value()))

                                    elif isinstance(value[0], Comment):
                                        comments = value

                                        for comment in comments:
                                            print("Comment-ID: " + comment.get_id())

                                            print("Comment-Content: " + comment.get_comment_content())

                                            print("Comment-Commented_By: " + comment.get_commented_by())

                                            print("Comment-Commented Time: " + str(comment.get_commented_time()))

                                    elif isinstance(value[0], Attachment):
                                        attachments = value

                                        for attachment in attachments:
                                            # Get the ID of each attachment
                                            print('Record Attachment ID : ' + str(attachment.get_id()))

                                            # Get the owner User instance of each attachment
                                            owner = attachment.get_owner()

                                            # Check if owner is not None
                                            if owner is not None:
                                                # Get the Name of the Owner
                                                print("Record Attachment Owner - Name: " + owner.get_name())

                                                # Get the ID of the Owner
                                                print("Record Attachment Owner - ID: " + owner.get_id())

                                                # Get the Email of the Owner
                                                print("Record Attachment Owner - Email: " + owner.get_email())

                                            # Get the modified time of each attachment
                                            print("Record Attachment Modified Time: " + str(attachment.get_modified_time()))

                                            # Get the name of the File
                                            print("Record Attachment File Name: " + attachment.get_file_name())

                                            # Get the created time of each attachment
                                            print("Record Attachment Created Time: " + str(attachment.get_created_time()))

                                            # Get the Attachment file size
                                            print("Record Attachment File Size: " + str(attachment.get_size()))

                                            # Get the parentId Record instance of each attachment
                                            parent_id = attachment.get_parent_id()

                                            if parent_id is not None:
                                                # Get the parent record Name of each attachment
                                                print(
                                                    "Record Attachment parent record Name: " + parent_id.get_key_value("name"))

                                                # Get the parent record ID of each attachment
                                                print("Record Attachment parent record ID: " + parent_id.get_id())

                                            # Check if the attachment is Editable
                                            print("Record Attachment is Editable: " + str(attachment.get_editable()))

                                            # Get the file ID of each attachment
                                            print("Record Attachment File ID: " + str(attachment.get_file_id()))

                                            # Get the type of each attachment
                                            print("Record Attachment File Type: " + str(attachment.get_type()))

                                            # Get the seModule of each attachment
                                            print("Record Attachment seModule: " + str(attachment.get_se_module()))

                                            # Get the modifiedBy User instance of each attachment
                                            modified_by = attachment.get_modified_by()

                                            # Check if modifiedBy is not None
                                            if modified_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print("Record Attachment Modified By - Name: " + modified_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print("Record Attachment Modified By - ID: " + modified_by.get_id())

                                                # Get the Email of the modifiedBy User
                                                print("Record Attachment Modified By - Email: " + modified_by.get_email())

                                            # Get the state of each attachment
                                            print("Record Attachment State: " + attachment.get_state())

                                            # Get the created_by User instance of each attachment
                                            created_by = attachment.get_created_by()

                                            # Check if created_by is not None
                                            if created_by is not None:
                                                # Get the Name of the created_by User
                                                print("Record Attachment Created By - Name: " + created_by.get_name())

                                                # Get the ID of the created_by User
                                                print("Record Attachment Created By - ID: " + created_by.get_id())

                                                # Get the Email of the created_by User
                                                print("Record Attachment Created By - Email: " + created_by.get_email())

                                            # Get the linkUrl of each attachment
                                            print("Record Attachment LinkUrl: " + str(attachment.get_link_url()))

                                    else:
                                        print(key_name)

                                        for each_value in value:
                                            print(str(each_value))

                            elif isinstance(value, User):
                                print("RelatedRecord " + key_name + " User-ID: " + str(value.get_id()))

                                print("RelatedRecord " + key_name + " User-Name: " + value.get_name())

                                print("RelatedRecord " + key_name + " User-Email: " + value.get_email())

                            elif isinstance(value, Layout):
                                print(key_name + " ID: " + str(value.get_id()))

                                print(key_name + " Name: " + value.get_name())

                            elif isinstance(value, Record):
                                print(key_name + " Record ID: " + str(value.get_id()))

                                print(key_name + " Record Name: " + value.get_key_value('name'))

                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())

                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())

                            elif isinstance(value, RecurringActivity):
                                print(key_name)

                                print("RRULE: " + value.get_rrule())

                            elif isinstance(value, Consent):
                                print("Record Consent ID: " + str(value.get_id()))

                                # Get the createdBy User instance of each Record
                                created_by = value.get_created_by()

                                # Check if created_by is not None
                                if created_by is not None:
                                    # Get the Name of the created_by User
                                    print("Record Consent Created By - Name: " + created_by.get_name())

                                    # Get the ID of the created_by User
                                    print("Record Consent Created By - ID: " + created_by.get_id())

                                    # Get the Email of the created_by User
                                    print("Record Consent Created By - Email: " + created_by.get_email())

                                # Get the CreatedTime of each Record
                                print("Record Consent CreatedTime: " + str(value.get_created_time()))

                                if value.get_modified_time() is not None:
                                    # Get the ModifiedTime of each Record
                                    print("Record Consent ModifiedTime: " + str(value.get_modified_time()))

                                # Get the Owner User instance of the Consent
                                owner = value.get_owner()

                                if owner is not None:
                                    # Get the Name of the Owner User
                                    print("Record Consent Created By - Name: " + owner.get_name())

                                    # Get the ID of the Owner User
                                    print("Record Consent Created By - ID: " + owner.get_id())

                                    # Get the Email of the Owner User
                                    print("Record Consent Created By - Email: " + owner.get_email())

                                print("Record Consent ContactThroughEmail: " + str(value.get_contact_through_email()))

                                print("Record Consent ContactThroughSocial: " + str(value.get_contact_through_social()))

                                print("Record Consent ContactThroughSurvey: " + str(value.get_contact_through_survey()))

                                print("Record Consent ContactThroughPhone: " + str(value.get_contact_through_phone()))

                                print("Record Consent MailSentTime: " + str(value.get_mail_sent_time()))

                                print("Record Consent ConsentDate: " + str(value.get_consent_date()))

                                print("Record Consent ConsentRemarks: " + value.get_consent_remarks())

                                print("Record Consent ConsentThrough: " + value.get_consent_through())

                                print("Record Consent DataProcessingBasis: " + value.get_data_processing_basis())

                                # To get custom values
                                print("Record Consent Lawful Reason: " + str(value.get_key_value("Lawful_Reason")))

                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))

                            else:
                                print(key_name + " : " + str(value))

                # Check if FileBodyWrapper instance is received.
                elif isinstance(response_object, FileBodyWrapper):
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
    def update_related_records(module_api_name, record_id, related_list_api_name):

        """
        This method is used to update the relation between the records and print the response.
        :param module_api_name: The API Name of the module to update related record.
        :param record_id: The ID of the record to be update Related List.
        :param related_list_api_name: The API name of the related list.
        """

        """
        example
        module_api_name = "Products"
        record_id = 3409643000000798007
        related_list_api_name = "Price_Books"
        """

        # Get instance of RelatedRecordsOperations Class that takes moduleAPIName, recordId and relatedListAPIName as parameter
        related_records_operations = RelatedRecordsOperations(related_list_api_name, record_id, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record_1 = Record()

        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """

        record_1.set_id(3409643000002414001)

        record_1.add_key_value('list_price', 50.56)

        # Add Record instance to the list
        records_list.append(record_1)

        # Get instance of Record Class
        record_2 = Record()

        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """

        record_2.set_id(34096430000024140010)

        record_2.add_key_value('list_price', 100.56)

        # Add Record instance to the list
        records_list.append(record_2)

        # Set the list to Records in BodyWrapper instance
        request.set_data(records_list)

        # Call update_related_records method that takes BodyWrapper instance
        response = related_records_operations.update_related_records(request)

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
    def update_related_record(module_api_name, record_id, related_list_api_name, related_list_id):

        """
        This method is used to update a single related record with ID and print the response.
        :param module_api_name: The API Name of the module to update related record.
        :param record_id: The ID of the record
        :param related_list_api_name: The API name of the related list.
        :param related_list_id: The ID of the related record.
        """

        """
        example
        module_api_name = "Products"
        record_id = 3409643000000798007
        related_list_api_name = "Price_Books"
        related_list_id = 3409643000002414001
        """

        # Get instance of RelatedRecordsOperations Class that takes moduleAPIName, recordId and relatedListAPIName as parameter
        related_records_operations = RelatedRecordsOperations(related_list_api_name, record_id, module_api_name)

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record = Record()

        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        record.add_key_value('list_price', 90.90)

        # Add Record instance to the list
        records_list.append(record)

        # Set the list to Records in BodyWrapper instance
        request.set_data(records_list)

        # Call updateRelatedRecord method that takes BodyWrapper instance, related_list_id as parameter.
        response = related_records_operations.update_related_record(related_list_id, request)

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
    def delink_records(module_api_name, record_id, related_list_api_name, related_list_ids):

        """
        This method is used to delete the association between modules and print the response.
        :param module_api_name: The API Name of the module to delink related records.
        :param record_id: The ID of the record
        :param related_list_api_name: The API name of the related list
        :param related_list_ids: The list of related record IDs.
        """

        """
        example
        module_api_name = "Products"
        record_id = 3409643000000798007
        related_list_api_name = "Price_Books"
        related_list_ids = [3409643000002414001, 3409643000002414002, 3409643000002414020]
        """

        # Get instance of RelatedRecordsOperations Class that takes moduleAPIName, recordId and relatedListAPIName as parameter
        related_records_operations = RelatedRecordsOperations(related_list_api_name, record_id, module_api_name)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        for related_list_id in related_list_ids:
            param_instance.add(DelinkRecordsParam.ids, related_list_id)

        # Call delink_records method that takes ParameterMap instance as parameter.
        response = related_records_operations.delink_records(param_instance)

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
    def delink_record(module_api_name, record_id, related_list_api_name, related_list_id):

        """
        This method is used to delete the association between modules and print the response.
        :param module_api_name: The API Name of the module to delink related record.
        :param record_id: The ID of the record
        :param related_list_api_name: The API name of the related list.
        :param related_list_id: The ID of the related record.
        """

        """
        example
        module_api_name = "Products"
        record_id = 3409643000000798007
        related_list_api_name = "Price_Books"
        related_list_id = 3409643000002414001
        """

        # Get instance of RelatedRecordsOperations Class that takes moduleAPIName, recordId and relatedListAPIName as parameter
        related_records_operations = RelatedRecordsOperations(module_api_name, record_id, related_list_api_name)

        # Call delink_record method that takes related_list_id as parameter.
        response = related_records_operations.delink_record(related_list_id)

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





