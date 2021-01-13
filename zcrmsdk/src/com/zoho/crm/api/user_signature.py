try:
    import re
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants

except Exception:
    import re
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from .util.constants import Constants


class UserSignature(object):

    """
    This class represents the Zoho CRM User.
    """

    def __init__(self, email):

        """
        Creates an UserSignature class instance with the specified user email.

        Parameters:
            email (str) : A string containing the CRM user email
        """

        error = {}

        if re.fullmatch(Constants.EMAIL_REGEX, email) is None:
            error[Constants.FIELD] = Constants.EMAIL
            error[Constants.EXPECTED_TYPE] = Constants.EMAIL

            raise SDKException(Constants.USER_SIGNATURE_ERROR, details=error)

        self.email = email
