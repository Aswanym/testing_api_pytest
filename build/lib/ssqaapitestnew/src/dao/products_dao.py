from ssqaapitestnew.src.utilities.db_utilities import DBUtility
import random

class ProductDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product(self, qty=1):

        sql = "SELECT * FROM new_coolsite.wp_posts WHERE post_type='product' LIMIT 20;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):

        sql = f"SELECT * FROM new_coolsite.wp_posts WHERE post_type='product' AND ID={product_id};"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_products_with_filter(self, after):

        sql = f"SELECT * FROM new_coolsite.wp_posts WHERE post_type='product' AND post_date > '{after}' LIMIT 1000;"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql
