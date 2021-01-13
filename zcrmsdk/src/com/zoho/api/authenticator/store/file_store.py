
try:
    import os
    import csv
    from zcrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType
    from ....crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException

except Exception as e:
    import os
    import csv
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken, TokenType
    from ....crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException


class FileStore(TokenStore):

    """
    The class to store user token details to the file.
    """

    def __init__(self, file_path):

        """
        Creates an FileStore class instance with the specified parameters.

        Parameters:
            file_path (str) : A string containing the absolute file path of the file to store tokens

        """

        self.file_path = file_path
        self.headers = [Constants.USER_MAIL, Constants.CLIENT_ID, Constants.REFRESH_TOKEN, Constants.ACCESS_TOKEN, Constants.GRANT_TOKEN, Constants.EXPIRY_TIME]

        if (os.path.exists(file_path) and os.stat(file_path).st_size == 0) or not os.path.exists(file_path):
            with open(self.file_path, mode='w') as token_file:
                csv_writer = csv.writer(token_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)

    def get_token(self, user, token):
        try:
            if isinstance(token, OAuthToken):
                with open(self.file_path, mode='r') as f:
                    data = csv.reader(f, delimiter=',')
                    next(data, None)
                    for next_record in data:
                        if len(next_record) == 0:
                            continue
                        if self.check_token_exists(user.email, token, next_record):
                            token.access_token = next_record[3]
                            token.expires_in = next_record[5]
                            token.refresh_token = next_record[2]
                            return token

        except IOError as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_FILE_ERROR, cause=ex)

        return None

    def save_token(self, user, token):
        if isinstance(token, OAuthToken):
            token.user_mail = user.email
            self.delete_token(token)

            try:
                with open(self.file_path, mode='a+') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([user.email, token.client_id, token.refresh_token, token.access_token, token.grant_token, token.expires_in])

            except IOError as ex:
                raise SDKException(code=Constants.TOKEN_STORE, message=Constants.SAVE_TOKEN_FILE_ERROR, cause=ex)

    def delete_token(self, token):
        lines = list()

        if isinstance(token, OAuthToken):
            try:
                with open(self.file_path, mode='r') as f:
                    data = csv.reader(f, delimiter=',')
                    for next_record in data:
                        if len(next_record) == 0:
                            continue
                        lines.append(next_record)
                        if self.check_token_exists(token.user_mail, token, next_record):
                            lines.remove(next_record)

                with open(self.file_path, mode='w') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerows(lines)

            except IOError as ex:
                raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKEN_FILE_ERROR, cause=ex)

    def get_tokens(self):
        tokens = []

        try:
            with open(self.file_path, mode='r') as f:
                data = csv.reader(f, delimiter=',')
                next(data, None)
                for next_record in data:
                    if len(next_record) == 0:
                        continue
                    token_type = TokenType.REFRESH if len(next_record[4]) == 0 else TokenType.GRANT
                    token_value = next_record[4] if token_type == TokenType.GRANT else next_record[2]
                    token = OAuthToken(next_record[1], None, token_value, token_type)
                    token.user_mail = next_record[0]
                    token.expires_in = next_record[5]
                    token.access_token = next_record[3]
                    tokens.append(token)

            return tokens
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKENS_FILE_ERROR, cause=ex)

    def delete_tokens(self):
        try:
            with open(self.file_path, mode='w') as token_file:
                csv_writer = csv.writer(token_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKENS_FILE_ERROR, cause=ex)
    
    def check_token_exists(self, email, token, row):
        if email is None:
            raise SDKException(Constants.USER_MAIL_NULL_ERROR, Constants.USER_MAIL_NULL_ERROR_MESSAGE)

        client_id = token.client_id
        grant_token = token.grant_token
        refresh_token = token.refresh_token
        token_check = grant_token == row[4] if grant_token is not None else refresh_token == row[2]

        if row[0] == email and row[1] == client_id and token_check:
            return True
        
        return False

