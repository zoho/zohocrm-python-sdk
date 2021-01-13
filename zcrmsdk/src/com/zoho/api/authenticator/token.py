from abc import abstractmethod, ABC


class Token(ABC):

    """
    The class to verify and set token to the APIHTTPConnector instance, to authenticate requests.
    """

    @abstractmethod
    def authenticate(self, url_connection):
        
        """
        The method to set token to APIHTTPConnector instance

        Parameters:
            url_connection (APIHTTPConnector) : A APIHTTPConnector class instance.
        """

        pass

    @abstractmethod
    def remove(self):

        """
        The method to remove the token from store.

        Returns:
            bool: A Boolean value representing the removed status.
        """
        pass
