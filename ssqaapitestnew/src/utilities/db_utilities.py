from ssqaapitestnew.src.utilities.credential_utilities import CredentialUtility
import pymysql
import pdb

class DBUtility(object):

    def __init__(self):
        self.db_cred = CredentialUtility.get_db_credentials()
        self.host = 'localhost'
        self.db_post = 3306

    def create_connection(self):

        db_user = self.db_cred['db_user']
        db_password = self.db_cred['db_password']

        connection = pymysql.connect(host=self.host, user=db_user, password=db_password, port=self.db_post)

        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} Error: {str(e)}")
            # raise Exception(f"Error: {str (e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass