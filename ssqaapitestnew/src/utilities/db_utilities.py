from ssqaapitestnew.src.config.host_config import DB_HOST
from ssqaapitestnew.src.utilities.credential_utilities import CredentialUtility
import pymysql
import pdb
import os

class DBUtility(object):

    def __init__(self):
        self.db_cred = CredentialUtility.get_db_credentials()

        self.machine = os.environ.get('MACHINE')
        assert self.machine, f"Environment variable 'MACHINE' must be set."

        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, f"Environment variable 'WP_HOST' must be set."

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f"Can't run test in docker if wp_host=local")

        self.env = os.environ.get('ENV', 'test')

        self.host = DB_HOST[self.machine][self.env]['host']
        self.db_port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']

    def create_connection(self):

        db_user = self.db_cred['db_user']
        db_password = self.db_cred['db_password']

        if self.wp_host == 'local':
            connection = pymysql.connect(host=self.host, user=db_user, password=db_password, port=self.db_port)
        else:
            raise Exception(f"Unknown WP_HOST")
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
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass