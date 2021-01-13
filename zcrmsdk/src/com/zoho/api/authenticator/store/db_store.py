
try:
    import mysql.connector
    from mysql.connector import Error
    from zcrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken, TokenType
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException

except Exception as e:
    import mysql.connector
    from mysql.connector import Error
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken, TokenType
    from ....crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException


class DBStore(TokenStore):

    """
    This class to store user token details to the MySQL DataBase.
    """

    def __init__(self, host=None, database_name=None, user_name=None, password=None, port_number=None):

        """
        Creates a DBStore class instance with the specified parameters.

        Parameters:
            host (str) : A string containing the DataBase host name. Default value is localhost
            database_name (str) : A string containing the DataBase name. Default value is zohooauth
            user_name (str) : A string containing the DataBase user name. Default value is root
            password (str) : A string containing the DataBase password. Default value is an empty string
            port_number (str) : A string containing the DataBase port number. Default value is 3306
        """

        self.host = host if host is not None else Constants.MYSQL_HOST
        self.database_name = database_name if database_name is not None else Constants.MYSQL_DATABASE_NAME
        self.user_name = user_name if user_name is not None else Constants.MYSQL_USER_NAME
        self.password = password if password is not None else ""
        self.port_number = port_number if port_number is not None else Constants.MYSQL_PORT_NUMBER

    def get_token(self, user, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database_name, user=self.user_name, password=self.password, port=self.port_number)
            try:
                if isinstance(token, OAuthToken):
                    cursor = connection.cursor()
                    query = self.construct_dbquery(user.email, token, False)
                    cursor.execute(query)
                    result = cursor.fetchone()

                    if result is not None:
                        token.access_token = result[4]
                        token.expires_in = result[6]
                        token.refresh_token = result[3]

                        return token

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_DB_ERROR, cause=ex)

    def save_token(self, user, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database_name, user=self.user_name, password=self.password, port=self.port_number)

            try:
                if isinstance(token, OAuthToken):
                    token.user_mail = user.email
                    self.delete_token(token)
                    cursor = connection.cursor()
                    query = "insert into oauthtoken (user_mail,client_id,refresh_token,access_token,grant_token,expiry_time) values (%s,%s,%s,%s,%s,%s);"
                    val = (user.email, token.client_id, token.refresh_token, token.access_token, token.grant_token, token.expires_in)
                    cursor.execute(query, val)
                    connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.SAVE_TOKEN_DB_ERROR, cause=ex)

    def delete_token(self, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database_name, user=self.user_name, password=self.password, port=self.port_number)

            try:
                if isinstance(token, OAuthToken):
                    cursor = connection.cursor()
                    query = self.construct_dbquery(token.user_mail, token, True)
                    cursor.execute(query)
                    connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKEN_DB_ERROR, cause=ex)

    def get_tokens(self):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database_name, user=self.user_name, password=self.password, port=self.port_number)
            tokens = []

            try:
                cursor = connection.cursor()
                query = 'select * from oauthtoken;'
                cursor.execute(query)
                results = cursor.fetchall()

                for result in results:
                    token_type = TokenType.REFRESH if (result[5] is None or result[5] == 'null') else TokenType.GRANT
                    token_value = result[5] if token_type == TokenType.GRANT else result[3]
                    token = OAuthToken(result[2], None, token_value, token_type)
                    token.id = result[0]
                    token.expires_in = result[6]
                    token.user_mail = result[1]
                    token.access_token = result[4]
                    tokens.append(token)

                return tokens

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKENS_DB_ERROR, None, ex)

    def delete_tokens(self):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.host, database=self.database_name, user=self.user_name, password=self.password, port=self.port_number)

            try:
                cursor = connection.cursor()
                query = 'delete from oauthtokens;'
                cursor.execute(query)
                connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None
        except Error as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.DELETE_TOKENS_DB_ERROR, None, ex)

    def construct_dbquery(self, email, token, is_delete):
        if email is None:
            raise SDKException(Constants.USER_MAIL_NULL_ERROR, Constants.USER_MAIL_NULL_ERROR_MESSAGE)

        query = "delete from " if is_delete is True else "select * from "
        query += "oauthtoken " + "where user_mail ='" + email + "' and client_id='" + token.client_id + "' and "

        if token.grant_token is not None:
            query += "grant_token='" + token.grant_token + "'"

        else:
            query += "refresh_token='" + token.refresh_token + "'"

        return query
