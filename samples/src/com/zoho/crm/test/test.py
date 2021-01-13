try:
    from samples.src.com.zoho.crm.api.initializer import SDKInitializer
    from samples.src.com.zoho.crm.api.attachments import Attachment
    from samples.src.com.zoho.crm.api.blue_print import BluePrint
    from samples.src.com.zoho.crm.api.bulk_read import BulkRead
    from samples.src.com.zoho.crm.api.bulk_write import BulkWrite
    from samples.src.com.zoho.crm.api.contact_roles import ContactRole
    from samples.src.com.zoho.crm.api.currencies import Currency
    from samples.src.com.zoho.crm.api.custom_views import CustomView
    from samples.src.com.zoho.crm.api.fields import Field
    from samples.src.com.zoho.crm.api.file import File
    from samples.src.com.zoho.crm.api.layouts import Layout
    from samples.src.com.zoho.crm.api.modules import Module
    from samples.src.com.zoho.crm.api.notes import Note
    from samples.src.com.zoho.crm.api.notification import Notification
    from samples.src.com.zoho.crm.api.organization import Organization
    from samples.src.com.zoho.crm.api.profiles import Profile
    from samples.src.com.zoho.crm.api.query import Query
    from samples.src.com.zoho.crm.api.related_lists import RelatedList
    from samples.src.com.zoho.crm.api.related_records import RelatedRecord
    from samples.src.com.zoho.crm.api.records import Record
    from samples.src.com.zoho.crm.api.roles import Role
    from samples.src.com.zoho.crm.api.share_records import ShareRecord
    from samples.src.com.zoho.crm.api.tags import Tag
    from samples.src.com.zoho.crm.api.taxes import Tax
    from samples.src.com.zoho.crm.api.territories import Territory
    from samples.src.com.zoho.crm.api.users import User
    from samples.src.com.zoho.crm.api.variable_groups import VariableGroup
    from samples.src.com.zoho.crm.api.variables import Variable
    from zcrmsdk.src.com.zoho.crm.api.util import ModuleFieldsHandler
except Exception:
    from ..api.initializer import SDKInitializer
    from ..api.attachments import Attachment
    from ..api.blue_print import BluePrint
    from ..api.bulk_read import BulkRead
    from ..api.bulk_write import BulkWrite
    from ..api.contact_roles import ContactRole
    from ..api.currencies import Currency
    from ..api.custom_views import CustomView
    from ..api.fields import Field
    from ..api.file import File
    from ..api.layouts import Layout
    from ..api.modules import Module
    from ..api.notes import Note
    from ..api.notification import Notification
    from ..api.organization import Organization
    from ..api.profiles import Profile
    from ..api.query import Query
    from ..api.records import Record
    from ..api.related_lists import RelatedList
    from ..api.related_records import RelatedRecord
    from ..api.roles import Role
    from ..api.share_records import ShareRecord
    from ..api.tags import Tag
    from ..api.taxes import Tax
    from ..api.territories import Territory
    from ..api.users import User
    from ..api.variable_groups import VariableGroup
    from ..api.variables import Variable
    from zcrmsdk.src.com.zoho.crm.api.util import ModuleFieldsHandler


class Test(object):

    @staticmethod
    def test():
        SDKInitializer.initialize_sdk()

        Test.attachment()

        Test.blue_print()

        Test.bulk_read()

        Test.bulk_write()

        Test.contact_role()

        Test.currency()

        Test.custom_view()

        Test.field()

        Test.file()

        Test.layout()

        Test.module()

        Test.note()

        Test.notification()

        Test.org()

        Test.profile()

        Test.query()

        Test.record()

        Test.related_list()

        Test.related_record()

        Test.role()

        Test.share_record()

        Test.tag()

        Test.tax()

        Test.territory()

        Test.user()

        Test.variable_group()

        Test.variable()

    @staticmethod
    def attachment():
        module_api_name = 'Leads'

        record_id = 3409643000002267003

        attachment_id = 3409643000002267024

        destination_folder = '/Users/user-name/resources'

        absolute_file_path = '/Users/user-name/resources/photo.jpg'

        print("-----Calling get_attachments()-----")
        Attachment.get_attachments(module_api_name, record_id)

        print("-----Calling upload_attachments()-----")
        Attachment.upload_attachments(module_api_name, record_id, absolute_file_path)

        print("-----Calling upload_link_attachment()-----")
        Attachment.upload_link_attachment(module_api_name, record_id, "https://crm.zoho.com")

        print("-----Calling delete_attachments()-----")
        Attachment.delete_attachments(module_api_name, record_id, [3409643000002394001, 3409643000003503007])

        print("-----Calling download_attachment()-----")
        Attachment.download_attachment(module_api_name, record_id, 3409643000003930001, destination_folder)

        print("-----Calling delete_attachment()-----")
        Attachment.delete_attachment(module_api_name, record_id, attachment_id)

    @staticmethod
    def blue_print():
        module_api_name = 'Leads'

        record_id = 3409643000002448001

        transition_id = 3477061000000173093

        print("-----Calling get_blueprint()-----")
        BluePrint.get_blueprint(module_api_name, record_id)

        print("-----Calling update_blueprint()-----")
        BluePrint.update_blueprint(module_api_name, record_id, transition_id)

    @staticmethod
    def bulk_read():
        module_api_name = 'Leads'

        job_id = 3409643000003556004

        destination_folder = '/Users/user_name/Documents/resources'

        print("-----Calling create_bulk_read_job()-----")
        BulkRead.create_bulk_read_job(module_api_name)

        print("-----Calling get_bulk_read_job_details()-----")
        BulkRead.get_bulk_read_job_details(job_id)
        #
        print("-----Calling download_result()-----")
        BulkRead.download_result(job_id, destination_folder)

    @staticmethod
    def bulk_write():
        file_path = "/Users/user_name/Documents/Leads.zip"

        org_id = '673899828'

        file_id = '3409643000003562001'

        job_id = 3409643000003555002

        download_url = 'https://download-accl.zoho.com/v2/crm/673899828/bulk-write/3409643000003555002/3409643000003555002.zip'

        destination_folder = '/Users/user_name/Documents/bulk-write'

        print("-----Calling upload_file()-----")
        BulkWrite.upload_file(org_id, file_path)

        print("-----Calling create_bulk_write_job()-----")
        BulkWrite.create_bulk_write_job('Leads', file_id)

        print("-----Calling get_bulk_write_job_details()-----")
        BulkWrite.get_bulk_write_job_details(job_id)

        print("-----Calling download_bulk_write_result()-----")
        BulkWrite.download_bulk_write_result(download_url, destination_folder)

    @staticmethod
    def contact_role():
        contact_role_id = 3409643000003509001

        contact_role_ids = [3409643000003509001, 3409643000003509002, 3409643000003509003]

        print("-----Calling get_contact_roles()-----")
        ContactRole.get_contact_roles()

        print("-----Calling get_contact_role()-----")
        ContactRole.get_contact_role(contact_role_id)

        print("-----Calling create_contact_roles()-----")
        ContactRole.create_contact_roles()

        print("-----Calling update_contact_roles()-----")
        ContactRole.update_contact_roles()

        print("-----Calling update_contact_role()-----")
        ContactRole.update_contact_role(contact_role_id)

        print("-----Calling delete_contact_role()-----")
        ContactRole.delete_contact_role(contact_role_id)

        print("-----Calling delete_contact_roles()-----")
        ContactRole.delete_contact_roles(contact_role_ids)

    @staticmethod
    def currency():
        currency_id = 3409643000002293037

        print("-----Calling enable_multiple_currencies()-----")
        Currency.enable_multiple_currencies()

        print("-----Calling get_currencies()-----")
        Currency.get_currencies()

        print("-----Calling get_currency()-----")
        Currency.get_currency(currency_id)
        #
        print("-----Calling add_currencies()-----")
        Currency.add_currencies()
        #
        print("-----Calling update_currencies()-----")
        Currency.update_currencies()

        print("-----Calling update_currency()-----")
        Currency.update_currency(currency_id)

        print("-----Calling update_base_currency()-----")
        Currency.update_base_currency()

    @staticmethod
    def custom_view():
        module_api_name = "leads"

        custom_view_id = 3409643000000087601

        print("-----Calling get_custom_views()-----")
        CustomView.get_custom_views(module_api_name)

        print("-----Calling get_custom_view()-----")
        CustomView.get_custom_view(module_api_name, custom_view_id)

    @staticmethod
    def field():
        module_api_name = "Tasks"

        field_id = 3409643000000002269

        print("-----Calling get_fields()-----")
        Field.get_fields(module_api_name)

        print("-----Calling get_field()-----")
        Field.get_field(module_api_name, field_id)

    @staticmethod
    def file():
        destination_folder = '/Users/user_name/Documents'

        file_id = '479f0f5eebf0fb982f99e3832b35d23e29f67c2868ee4c789f22579895383c82'

        print("-----Calling upload_files()-----")
        File.upload_files()

        print("-----Calling get_file()-----")
        File.get_file(file_id, destination_folder)

    @staticmethod
    def layout():
        module_api_name = "contacts"

        layout_id = 3409643000000091055

        print("-----Calling get_layouts()-----")
        Layout.get_layouts(module_api_name)

        print("-----Calling get_layout()-----")
        Layout.get_layout(module_api_name, layout_id)

    @staticmethod
    def module():
        module_api_name = "Leads"

        module_id = 3409643000000252001

        print("-----Calling get_modules()-----")
        Module.get_modules()

        print("-----Calling get_module()-----")
        Module.get_module(module_api_name)

        print("-----Calling update_module_by_api_name()-----")
        Module.update_module_by_api_name(module_api_name)

        print("-----Calling update_module_by_id()-----")
        Module.update_module_by_id(module_id)

    @staticmethod
    def note():
        note_id = 3409643000003368008

        note_ids = [3409643000000648001, 3409643000000648005]

        print("-----Calling get_notes()-----")
        Note.get_notes()

        print("-----Calling get_note()-----")
        Note.get_note(note_id)

        print("-----Calling create_notes()-----")
        Note.create_notes()

        print("-----Calling update_notes()-----")
        Note.update_notes()

        print("-----Calling update_note()-----")
        Note.update_note(note_id)

        print("-----Calling delete_notes()-----")
        Note.delete_notes(note_ids)

        print("-----Calling delete_note()-----")
        Note.delete_note(note_id)

    @staticmethod
    def notification():
        channel_ids = [100000006800212]

        print("-----Calling enable_notifications()-----")
        Notification.enable_notifications()

        print("-----Calling get_notification_details()-----")
        Notification.get_notification_details()

        print("-----Calling update_notifications()-----")
        Notification.update_notifications()

        print("-----Calling update_notification()-----")
        Notification.update_notification()

        print("-----Calling disable_notifications()-----")
        Notification.disable_notifications(channel_ids)

        print("-----Calling disable_notification()-----")
        Notification.disable_notification()

    @staticmethod
    def org():
        file_path = '/Users/user_name/Documents/org_picture.png'

        print("-----Calling get_organization()-----")
        Organization.get_organization()

        print("-----Calling upload_organization_photo()-----")
        Organization.upload_organization_photo(file_path)

    @staticmethod
    def profile():
        profile_id = 3409643000000026014

        print("-----Calling get_profiles()-----")
        Profile.get_profiles()

        print("-----Calling get_profile()-----")
        Profile.get_profile(profile_id)

    @staticmethod
    def query():
        print("-----Calling get_records()-----")
        Query.get_records()

    @staticmethod
    def record():
        module_api_name = 'Products'

        # print("-----Calling get_records()-----")
        Record.get_records(module_api_name)

        Record.create_records(module_api_name)

        Record.mass_update_records('Contacts')

        Record.convert_lead(3409643000002730065)

        Record.upsert_records('leads')

        Record.search_records('leads')

        Record.get_deleted_records('leads')

        Record.update_records('leads')

        Record.update_record('events', 3409643000003543002)

        Record.delete_record('Calls', 3409643000003543002)

        Record.delete_records('Calls', [3409643000003543002, 3409643000003543003, 3409643000003543004])

        Record.upload_photo('leads', 3409643000003554001, '/Users/user_name/Documents/sample.jpg')

        Record.get_photo('leads', 3409643000003554001, '/Users/user_name/Documents/resources')

        Record.delete_photo('leads', 3409643000003554001)

        Record.get_record('Calls', 3409643000003543002, None)

        Record.create_records('price_books')

    @staticmethod
    def related_list():
        module_api_name = "leads"

        related_list_id = 3409643000000062003

        print("-----Calling get_related_lists()-----")
        RelatedList.get_related_lists(module_api_name)

        print("-----Calling get_related_list()-----")
        RelatedList.get_related_list(module_api_name, related_list_id)

    @staticmethod
    def related_record():
        module_api_name = "products"

        record_id = 3409643000000231007

        related_module_api_name = "price_books"

        related_id = 3409643000000231007

        related_ids = [3409643000002414001, 3409643000002414010]

        destination_folder = '/Users/user_name/Desktop'

        print("-----Calling get_related_records()-----")
        RelatedRecord.get_related_records(module_api_name, record_id, related_module_api_name)

        print("-----Calling get_related_record()-----")
        RelatedRecord.get_related_record(module_api_name, record_id, related_module_api_name, related_id, destination_folder)

        print("-----Calling update_related_record()-----")
        RelatedRecord.update_related_record(module_api_name, record_id, related_module_api_name, related_id)

        print("-----Calling update_related_records()-----")
        RelatedRecord.update_related_records(module_api_name, record_id, related_module_api_name)

        print("-----Calling delink_record()-----")
        RelatedRecord.delink_record(module_api_name, record_id, related_module_api_name, related_id)

        print("-----Calling delink_records()-----")
        RelatedRecord.delink_records(module_api_name, record_id, related_module_api_name, related_ids)

    @staticmethod
    def role():
        role_id = 3409643000000026005

        print("-----Calling get_roles()-----")
        Role.get_roles()

        print("-----Calling get_role()-----")
        Role.get_role(role_id)

    @staticmethod
    def share_record():
        module_api_name = 'Contacts'

        record_id = 3409643000002112011

        print("-----Calling share_record()-----")
        ShareRecord.share_record(module_api_name, record_id)

        print("-----Calling update_share_permissions()-----")
        ShareRecord.update_share_permissions(module_api_name, record_id)

        print("-----Calling get_shared_record_details()-----")
        ShareRecord.get_shared_record_details(module_api_name, record_id)

        print("-----Calling revoke_shared_record()-----")
        ShareRecord.revoke_shared_record(module_api_name, record_id)

    @staticmethod
    def tag():
        module_api_name = 'Leads'

        tag_id = 3409643000003388001

        record_id = 3409643000002157023

        tag_names = ["python-tags1", "python-tags2"]

        record_ids = [3409643000000723026, 3409643000000527003, 3409643000000394028]

        conflict_id = '3409643000000661027'

        print("-----Calling get_tags()-----")
        Tag.get_tags(module_api_name)

        print("-----Calling create_tags()-----")
        Tag.create_tags(module_api_name)

        print("-----Calling update_tags()-----")
        Tag.update_tags(module_api_name)

        print("-----Calling update_tag()-----")
        Tag.update_tag(module_api_name, tag_id)
        #
        print("-----Calling merge_tags()-----")
        Tag.merge_tags(tag_id, conflict_id)

        print("-----Calling add_tags_to_record()-----")
        Tag.add_tags_to_record(module_api_name, record_id, tag_names)

        print("-----Calling remove_tags_from_record()-----")
        Tag.remove_tags_from_record(module_api_name, record_id, tag_names)

        print("-----Calling add_tags_to_multiple_records()-----")
        Tag.add_tags_to_multiple_records(module_api_name, record_ids, tag_names)

        print("-----Calling remove_tags_from_multiple_records()-----")
        Tag.remove_tags_from_multiple_records(module_api_name, record_ids, tag_names)

        print("-----Calling get_record_count_for_tag()-----")
        Tag.get_record_count_for_tag(module_api_name, tag_id)

        print("-----Calling delete_tag()-----")
        Tag.delete_tag(tag_id)

    @staticmethod
    def tax():
        tax_id = 3409643000002540014

        tax_ids = [3409643000003510005, 3409643000003510006]

        print("-----Calling get_taxes()-----")
        Tax.get_taxes()

        print("-----Calling get_tax()-----")
        Tax.get_tax(tax_id)

        print("-----Calling create_taxes()-----")
        Tax.create_taxes()

        print("-----Calling update_taxes()-----")
        Tax.update_taxes()

        print("-----Calling delete_taxes()-----")
        Tax.delete_taxes(tax_ids)

        print("-----Calling delete_tax()-----")
        Tax.delete_tax(tax_id)

    @staticmethod
    def territory():
        territory_id = 3409643000000505385

        print("-----Calling get_territories()-----")
        Territory.get_territories()

        print("-----Calling get_territory()-----")
        Territory.get_territory(territory_id)

    @staticmethod
    def user():
        user_id = 3409643000002716031

        print("-----Calling create_user()-----")
        User.create_user()

        print("-----Calling get_users()-----")
        User.get_users()

        print("-----Calling get_user()-----")
        User.get_user(user_id)

        print("-----Calling update_users()-----")
        User.update_users()

        print("-----Calling update_user()-----")
        User.update_user(user_id)

        print("-----Calling delete_user()-----")
        User.delete_user(user_id)


    @staticmethod
    def variable_group():
        variable_group_id = 3409643000002275023

        variable_group_api_name = 'new_group'

        print("-----Calling get_variable_groups()-----")
        VariableGroup.get_variable_groups()

        print("-----Calling get_variable_group_by_id()-----")
        VariableGroup.get_variable_group_by_id(variable_group_id)

        print("-----Calling get_variable_group_by_api_name()-----")
        VariableGroup.get_variable_group_by_api_name(variable_group_api_name)

    @staticmethod
    def variable():
        variable_id = 3409643000002275025

        variable_ids = [3409643000003532006, 3409643000003480005]

        variable_api_name = 'First'

        print("-----Calling create_variables()-----")
        Variable.create_variables()

        print("-----Calling get_variables()-----")
        Variable.get_variables()

        print("-----Calling get_variable_by_id()-----")
        Variable.get_variable_by_id(variable_id)

        print("-----Calling get_variable_for_api_name()-----")
        Variable.get_variable_for_api_name(variable_api_name)

        print("-----Calling update_variables()-----")
        Variable.update_variables()

        print("-----Calling update_variable_by_api_name()-----")
        Variable.update_variable_by_api_name(variable_api_name)

        print("-----Calling update_variable_by_id()-----")
        Variable.update_variable_by_id(variable_id)

        print("-----Calling delete_variables()-----")
        Variable.delete_variables(variable_ids)

        print("-----Calling delete_variable()-----")
        Variable.delete_variable(variable_id)


# Test.test()
