from ssqaapitestnew.src.utilities.db_utilities import DBUtility
import pdb
import logging as logger

class CustomerDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM mysite.wp_users WHERE user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        logger.debug(f"sql: {rs_sql}")
        return rs_sql

    def get_existing_email(self):

        sql = f"SELECT user_email FROM mysite.wp_users ORDER BY ID DESC LIMIT 1;"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql
