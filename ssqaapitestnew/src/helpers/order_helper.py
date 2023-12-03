from ssqaapitestnew.src.dao.orders_dao import OrdersDAO
from ssqaapitestnew.src.utilities.woo_api_utilities import WooApiUtility
import json
import os
import pdb
class OrderHelper(object):

    def __init__(self):
        self.current_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_api_utility = WooApiUtility()

    def create_order(self, additional_args=None):

        payload_template = os.path.join(self.current_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        # if user pass more info to payload, then update it.
        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter 'additional_args' must be a dictionary, " \
                                                      f"but found {type(additional_args)}."
            payload.update(additional_args)

        rs_api = self.woo_api_utility.post('orders', params=payload, expected_status_code=201)

        return rs_api

    @staticmethod
    def varify_order_created(order_json, exp_customer_id, exp_products):

        # verify response
        assert order_json, f"Create order response is empty."
        assert order_json['customer_id'] == exp_customer_id, f"customer id expected : {exp_customer_id}, " \
                                                         f"but got '{order_json['customer_id']}'"
        assert len(order_json['line_items']) == len(exp_products), f"Expected only one item in the order but" \
                                                    f" got '{len (order_json['line_items'])}' " \
                                                    f"order_id '{order_json['id']}' "

        # verify db
        order_dao = OrdersDAO()
        order_id = order_json['id']
        line_info = order_dao.get_order_lines_by_order_id(order_id)
        assert line_info, f"Create order, line item not created in db. order id : {order_id}"

        line_items = [info for info in line_info if info['order_item_type'] == 'line_item']
        assert len(line_items) == 1, f"Expected one line item but found {len (line_items)}. order id {order_id}"

        # get list of product id from the json
        api_product_id = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_product_id, f"Created order doesn't have at least 1" \
                                                            f"expected product in db. product id : {product['product_id']} " \
                                                            f"order_id: {order_id}"
