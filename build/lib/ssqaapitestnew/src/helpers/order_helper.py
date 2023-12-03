import json
import os
import pdb;
class OrderHelper(object):

    def __init__(self):
        self.current_file_dir = os.path.dirname(os.path.realpath(__file__))

    def create_order(self, additional_args=None):

        payload_template = os.path.join(self.current_file_dir, '..', 'data', 'create_order_payload.json')

        pdb.set_trace()
        with open(payload_template) as f:
            payload = json.load(f)

        pdb.set_trace()