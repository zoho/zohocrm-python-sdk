from zcrmsdk.src.com.zoho.crm.api.org import *
from zcrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class Organization(object):

    @staticmethod
    def get_organization():

        """
        This method is used to get the organization data and print the response.
        """

        # Get instance of OrgOperations Class
        org_operations = OrgOperations()

        # Call get_organization method
        response = org_operations.get_organization()

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

                    # Get the list of obtained Org instances
                    org_list = response_object.get_org()

                    for org in org_list:
                        # Get the Country of each Organization
                        print("Organization Country: " + str(org.get_country()))

                        # Get the PhotoId of each Organization
                        print("Organization PhotoId: " + org.get_photo_id())

                        # Get the City of each Organization
                        print("Organization City: " + str(org.get_city()))

                        # Get the Description of each Organization
                        print("Organization Description: " + str(org.get_description()))

                        # Get the McStatus of each Organization
                        print("Organization McStatus: " + str(org.get_mc_status()))

                        # Get the GappsEnabled of each Organization
                        print("Organization GappsEnabled: " + str(org.get_gapps_enabled()))

                        # Get the DomainName of each Organization
                        print("Organization DomainName: " + str(org.get_domain_name()))

                        # Get the TranslationEnabled of each Organization
                        print("Organization TranslationEnabled: " + str(org.get_translation_enabled()))

                        # Get the Alias of each Organization
                        print("Organization Alias: " + str(org.get_alias()))

                        # Get the Id of each Organization
                        print("Organization Id: " + str(org.get_id()))

                        # Get the State of each Organization
                        print("Organization State: " + str(org.get_state()))

                        # Get the Fax of each Organization
                        print("Organization Fax: " + str(org.get_fax()))

                        # Get the EmployeeCount of each Organization
                        print("Organization EmployeeCount: " + str(org.get_employee_count()))

                        # Get the Zip of each Organization
                        print("Organization Zip: " + str(org.get_zip()))

                        # Get the Website of each Organization
                        print("Organization Website: " + str(org.get_website()))

                        # Get the CurrencySymbol of each Organization
                        print("Organization CurrencySymbol: " + str(org.get_currency_symbol()))

                        # Get the Mobile of each Organization
                        print("Organization Mobile: " + str(org.get_mobile()))

                        # Get the CurrencyLocale of each Organization
                        print("Organization CurrencyLocale: " + str(org.get_currency_locale()))

                        # Get the PrimaryZuid of each Organization
                        print("Organization PrimaryZuid: " + str(org.get_primary_zuid()))

                        # Get the ZiaPortalId of each Organization
                        print("Organization ZiaPortalId: " + str(org.get_zia_portal_id()))

                        # Get the TimeZone of each Organization
                        print("Organization TimeZone: " + str(org.get_time_zone()))

                        # Get the Zgid of each Organization
                        print("Organization Zgid: " + str(org.get_zgid()))

                        # Get the CountryCode of each Organization
                        print("Organization CountryCode: " + str(org.get_country_code()))

                        # Get the obtained LicenseDetails instance
                        license_details = org.get_license_details()

                        if license_details is not None:
                            # Get the PaidExpiry of LicenseDetails
                            print("Organization LicenseDetails PaidExpiry: " + str(license_details.get_paid_expiry()))

                            # Get the UsersLicensePurchased of LicenseDetails
                            print("Organization LicenseDetails UsersLicensePurchased: " + str(
                                license_details.get_users_license_purchased()))

                            # Get the TrialType of LicenseDetails
                            print("Organization LicenseDetails TrialType: " + str(license_details.get_trial_type()))

                            # Get the TrialExpiry of LicenseDetails
                            print("Organization LicenseDetails TrialExpiry: " + str(license_details.get_trial_expiry()))

                            # Get the Paid of LicenseDetails
                            print("Organization LicenseDetails Paid: " + str(license_details.get_paid()))

                            # Get the PaidType of LicenseDetails
                            print("Organization LicenseDetails PaidType: " + str(license_details.get_paid_type()))

                        # Get the Phone of each Organization
                        print("Organization Phone: " + str(org.get_phone()))

                        # Get the CompanyName of each Organization
                        print("Organization CompanyName: " + str(org.get_company_name()))

                        # Get the PrivacySettings of each Organization
                        print("Organization PrivacySettings: " + str(org.get_privacy_settings()))

                        # Get the PrimaryEmail of each Organization
                        print("Organization PrimaryEmail: " + str(org.get_primary_email()))

                        # Get the IsoCode of each Organization
                        print("Organization IsoCode: " + str(org.get_iso_code()))

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
    def upload_organization_photo(absolute_file_path):

        """
        This method is used to upload the brand logo or image of the organization and print the response.
        :param absolute_file_path: The absolute file path of the file to be attached
        """

        """
        example
		absolute_file_path = "/Users/user_name/Desktop/logo.png";
        """

        # Get instance of OrgOperations Class
        org_operations = OrgOperations()

        # Get instance of FileBodyWrapper class that will contain the request file
        request = FileBodyWrapper()

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
        request.set_file(stream_wrapper)

        # Call upload_organization_photo method that takes FileBodyWrapper instance as parameter
        response = org_operations.upload_organization_photo(request)

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
