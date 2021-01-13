from datetime import datetime
from zcrmsdk.src.com.zoho.crm.api.notification import *
from zcrmsdk.src.com.zoho.crm.api.notification import Notification as ZCRMNotification
from zcrmsdk.src.com.zoho.crm.api import HeaderMap, ParameterMap


class Notification(object):

    @staticmethod
    def enable_notifications():

        """
        This method is used to Enable Notifications and print the response.
        """

        # Get instance of NotificationOperations Class
        notification_operations = NotificationOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        body_wrapper = BodyWrapper()

        # List to hold Notification instances
        notifications = []

        # Get instance of Notification Class
        notification_1 = ZCRMNotification()

        # Set channel Id of the Notification
        notification_1.set_channel_id(100000006800211)

        # To subscribe based on particular operations on given modules.
        notification_1.set_events(['Deals.all'])

        # To set the expiry time for instant notifications.
        notification_1.set_channel_expiry(datetime.now())

        # By using this value, user can validate the notifications.
        notification_1.set_token("TOKEN_FOR_VERIFICATION_OF_100000006800211")

        # URL to be notified (POST request)
        notification_1.set_notify_url("https://www.zohoapis.com")

        # Add Notification instance to the list
        notifications.append(notification_1)

        # Get instance of Notification Class
        notification_2 = ZCRMNotification()

        # Set channel Id of the Notification
        notification_2.set_channel_id(1000000068002)

        # To subscribe based on particular operations on given modules.
        notification_2.set_events(['Accounts.all'])

        # To set the expiry time for instant notifications.
        notification_2.set_channel_expiry(datetime(2020, 11, 11, 10, 10, 10))

        # By using this value, user can validate the notifications.
        notification_2.set_token("TOKEN_FOR_VERIFICATION_OF_1000000068002")

        # URL to be notified (POST request)
        notification_2.set_notify_url("https://www.zohoapis.com")

        # Add Notification instance to the list
        notifications.append(notification_2)

        # Set the list to notifications in BodyWrapper instance
        body_wrapper.set_watch(notifications)

        # Call enable_notifications method that takes BodyWrapper instance as parameter
        response = notification_operations.enable_notifications(body_wrapper)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_watch()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessResponse):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details: ")

                            if action_response.get_details() is not None:
                                for key, value in action_response.get_details().items():
                                    if isinstance(value, list):
                                        event_list = value

                                        for event in event_list:
                                            # Get the ChannelExpiry of each Notification
                                            print("Notification ChannelExpiry: " + str(event.get_channel_expiry()))

                                            # Get the ResourceUri of each Notification
                                            print("Notification ResourceUri: " + event.get_resource_uri())

                                            # Get the ResourceId of each Notification
                                            print("Notification ResourceId: " + event.get_resource_id())

                                            # Get the ResourceName of each Notification
                                            print("Notification ResourceName: " + event.get_resource_name())

                                            # Get the ChannelId of each Notification
                                            print("Notification ChannelId: " + str(event.get_channel_id()))

                                    else:
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
    def get_notification_details():

        """
        This method is used to get details of the Notification and print the response.
        """

        # Get instance of NotificationOperations Class
        notification_operations = NotificationOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        param_instance.add(GetNotificationDetailsParam.module, 'Deals')

        param_instance.add(GetNotificationDetailsParam.page, 1)

        param_instance.add(GetNotificationDetailsParam.per_page, 20)

        param_instance.add(GetNotificationDetailsParam.channel_id, 100000006800211)

        # Call get_notification_details method that takes param_instance as parameter
        response = notification_operations.get_notification_details(param_instance)

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
                    # Get the list of obtained Notification instances
                    notification_list = response_object.get_watch()

                    for notification in notification_list:

                        # Get the NotifyOnRelatedAction of each Notification
                        print("Notification NotifyOnRelatedAction: " + str(notification.get_notify_on_related_action()))

                        # Get the ChannelExpiry of each Notification
                        print("Notification ChannelExpiry: " + str(notification.get_channel_expiry()))

                        # Get the ResourceUri of each Notification
                        print("Notification ResourceUri: " + notification.get_resource_uri())

                        # Get the ResourceId of each Notification
                        print("Notification ResourceId: " + notification.get_resource_id())

                        # Get the ResourceName of each Notification
                        print("Notification ResourceName: " + notification.get_resource_name())

                        # Get the ChannelId of each Notification
                        print("Notification ChannelId: " + str(notification.get_channel_id()))

                        # Get the NotifyUrl each Notification
                        print("Notification NotifyUrl: " + notification.get_notify_url())

                        # Get the events List of each Notification
                        events = notification.get_events()

                        if events is not None:
                            for event in events:
                                # Get the Events
                                print("Notification Events: " + event)

                        # Get the Token each Notification
                        print("Notification Token: " + notification.get_token())

                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('Notification Info PerPage: ' + str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('Notification Info Page: ' + str(info.get_page()))

                        if info.get_count() is not None:
                            # Get the Count from Info
                            print('Notification Info Count: ' + str(info.get_count()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords from Info
                            print('Notification Info MoreRecords: ' + str(info.get_more_records()))

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
    def update_notifications():

        """
        This method is used to update Notifications and print the response.
        """

        # Get instance of NotificationOperations Class
        notification_operations = NotificationOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        body_wrapper = BodyWrapper()

        # List to hold Notification instances
        notifications = []

        # Get instance of Notification Class
        notification_1 = ZCRMNotification()

        # Set channel Id of the Notification
        notification_1.set_channel_id(100000006800211)

        # To subscribe based on particular operations on given modules.
        notification_1.set_events(['Leads.all'])

        # URL to be notified (POST request)
        notification_1.set_notify_url("https://www.zohoapis.com")

        # Add Notification instance to the list
        notifications.append(notification_1)

        # Get instance of Notification Class
        notification_2 = ZCRMNotification()

        # Set channel Id of the Notification
        notification_2.set_channel_id(1000000068002)

        # To subscribe based on particular operations on given modules.
        notification_2.set_events(['Contacts.create'])

        # By using this value, user can validate the notifications.
        notification_2.set_token("TOKEN_FOR_VERIFICATION_OF_1000000068002")

        # URL to be notified (POST request)
        notification_2.set_notify_url("https://www.zohoapis.com")

        # Add Notification instance to the list
        notifications.append(notification_2)

        # Set the list to notifications in BodyWrapper instance
        body_wrapper.set_watch(notifications)

        # Call update_notifications method that takes BodyWrapper instance as parameter
        response = notification_operations.update_notifications(body_wrapper)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_watch()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessResponse):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details: ")

                            if action_response.get_details() is not None:
                                for key, value in action_response.get_details().items():
                                    if isinstance(value, list):
                                        event_list = value

                                        for event in event_list:
                                            # Get the ChannelExpiry of each Notification
                                            print("Notification ChannelExpiry: " + str(event.get_channel_expiry()))

                                            # Get the ResourceUri of each Notification
                                            print("Notification ResourceUri: " + event.get_resource_uri())

                                            # Get the ResourceId of each Notification
                                            print("Notification ResourceId: " + event.get_resource_id())

                                            # Get the ResourceName of each Notification
                                            print("Notification ResourceName: " + event.get_resource_name())

                                            # Get the ChannelId of each Notification
                                            print("Notification ChannelId: " + str(event.get_channel_id()))

                                    else:
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
    def update_notification():

        """
        This method is used to update single Notification and print the response.
        """

        # Get instance of NotificationOperations Class
        notification_operations = NotificationOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        body_wrapper = BodyWrapper()

        # List to hold Notification instances
        notifications = []

        # Get instance of Notification Class
        notification = ZCRMNotification()

        # Set channel Id of the Notification
        notification.set_channel_id(100000006800211)

        # To subscribe based on particular operations on given modules.
        notification.set_events(['Leads.create'])

        # URL to be notified (POST request)
        notification.set_notify_url("https://www.zohoapis.com")

        # Add Notification instance to the list
        notifications.append(notification)

        # Set the list to notifications in BodyWrapper instance
        body_wrapper.set_watch(notifications)

        # Call update_notification method that takes BodyWrapper instance as parameters
        response = notification_operations.update_notification(body_wrapper)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_watch()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessResponse):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details: ")

                            if action_response.get_details() is not None:
                                for key, value in action_response.get_details().items():
                                    if isinstance(value, list):
                                        event_list = value

                                        for event in event_list:
                                            # Get the ChannelExpiry of each Notification
                                            print("Notification ChannelExpiry: " + str(event.get_channel_expiry()))

                                            # Get the ResourceUri of each Notification
                                            print("Notification ResourceUri: " + event.get_resource_uri())

                                            # Get the ResourceId of each Notification
                                            print("Notification ResourceId: " + event.get_resource_id())

                                            # Get the ResourceName of each Notification
                                            print("Notification ResourceName: " + event.get_resource_name())

                                            # Get the ChannelId of each Notification
                                            print("Notification ChannelId: " + str(event.get_channel_id()))

                                    else:
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
    def disable_notifications(channel_ids):

        """
        To stop all the instant notifications enabled by the user for a channel.
        :param channel_ids: A list containing the unique IDs of the notification channels to be disabled.
        """

        """
        example
        channel_ids = [1000000068002, 1000000068020, 1000000068101]
        """

        # Get instance of NotificationOperations Class
        notification_operations = NotificationOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        for channel_id in channel_ids:
            param_instance.add(DisableNotificationsParam.channel_ids, channel_id)

        # Call disable_notifications method that takes paramInstance as parameter
        response = notification_operations.disable_notifications(param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_watch()

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
    def disable_notification():

        """
        This method is used to disable notifications for the specified events in a channel.
        """

        # Get instance of NotificationOperations Class
        notification_operations = NotificationOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        body_wrapper = BodyWrapper()

        # List to hold Notification instances
        notifications = []

        # Get instance of Notification Class
        notification = ZCRMNotification()

        # Set channel Id of the Notification
        notification.set_channel_id(100000006800211)

        # To subscribe based on particular operations on given modules.
        notification.set_events(['Leads.create'])

        notification.set_deleteevents(True)

        # Add Notification instance to the list
        notifications.append(notification)

        # Set the list to notifications in BodyWrapper instance
        body_wrapper.set_watch(notifications)

        # Call disable_notification which takes BodyWrapper instance as parameter
        response = notification_operations.disable_notification(body_wrapper)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_watch()

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
