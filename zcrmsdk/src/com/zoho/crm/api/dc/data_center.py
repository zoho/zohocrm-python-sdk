from abc import abstractmethod,  ABC


class DataCenter(ABC):

    """
    This class represents the properties of Zoho CRM DataCenter
    """

    @abstractmethod
    def get_iam_url(self):

        """
        The method to get the accounts URL.
        :return: A str representing the accounts URL.
        """

        pass

    @abstractmethod
    def get_file_upload_url(self):
        """
        The method to get the File Upload URL
        :return: A str representing the File Upload URL
        """

        pass

    class Environment(object):

        def __init__(self, url, accounts_url, file_upload_url):

            """
            Creates an Environment class instance with the specified parameters.
            :param url: A str representing the Zoho CRM API URL.
            :param accounts_url: A str representing the accounts URL.
            :param file_upload_url : A str representing the File Upload URL
            """

            self.url = url
            self.accounts_url = accounts_url
            self.file_upload_url = file_upload_url
            return
