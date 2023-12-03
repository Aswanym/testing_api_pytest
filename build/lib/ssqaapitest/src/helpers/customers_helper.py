from ssqaapitest.src.utilities.generic_utilities import generate_random_email_and_password
from ssqaapitest.src.utilities.request_utilities import RequestUtilitY
import pdb
import json

class CustomerHelper(object):

    def __init__(self):
        self.request_utility = RequestUtilitY()

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.request_utility.post('customers', payload=payload, expected_status_code=201)
        return create_user_json
