from ssqaapitest.src.config.host_config import API_HOST
from ssqaapitest.src.utilities.credential_utilities import CredentialUtility
from requests_oauthlib import OAuth1
import requests
import os
import json
import logging as logger
import pdb

class RequestUtilitY(object):

    def __init__(self):
        self.url = None
        self.api_res_json = None
        self.expected_status_code = None
        self.res_status_code = None
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]

        wc_creds = CredentialUtility.get_api_credentials()
        self.auth = OAuth1(wc_creds['wc_api_key'], wc_creds['wc_api_secret'])

    def assert_status_code(self):

        assert self.res_status_code == self.expected_status_code, \
            f"Bad status code, "\
            f"Expected status code: {self.expected_status_code}, "\
            f"Actual status code: {self.res_status_code}, "\
            f"URL:{self.url}, "\
            f"Response json: {self.api_res_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint
        if not headers:
            headers = {'content-type': 'application/json'}
        api_res = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.res_status_code = api_res.status_code
        self.expected_status_code = expected_status_code
        self.api_res_json = api_res.json()

        self.assert_status_code()

        logger.debug(f'POST Api response:{self.api_res_json}')
        return self.api_res_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint
        if not headers:
            headers = {'content-type': 'application/json'}
        api_res = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.res_status_code = api_res.status_code
        self.expected_status_code = expected_status_code
        self.api_res_json = api_res.json()

        self.assert_status_code()

        logger.info(f'GET Api response:{self.api_res_json}')
        return self.api_res_json
