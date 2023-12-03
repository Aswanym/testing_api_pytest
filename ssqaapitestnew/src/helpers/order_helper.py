
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