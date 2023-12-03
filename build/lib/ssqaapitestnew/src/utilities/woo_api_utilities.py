from ssqaapitestnew.src.config.host_config import WOO_API_HOST
from ssqaapitestnew.src.utilities.credential_utilities import CredentialUtility
from woocommerce import API
import logging as logger
import os


class WooApiUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOST[self.env]

        wc_creds = CredentialUtility.get_api_credentials()

        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_api_key'],
            consumer_secret=wc_creds['wc_api_secret'],
            version="wc/v3"
        )

    def assert_status_code(self):

        assert self.res_status_code == self.expected_status_code, \
            f"Bad status code, "\
            f"Expected status code: {self.expected_status_code}, "\
            f"Actual status code: {self.res_status_code}, "\
            f"URL:{self.url}, "\
            f"Response json: {self.api_res_json}"

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        api_res = self.wcapi.get(wc_endpoint, params=params)

        self.res_status_code = api_res.status_code
        self.expected_status_code = expected_status_code
        self.api_res_json = api_res.json()

        self.assert_status_code()

        logger.info(f'GET Api response:{self.api_res_json}')

        return self.api_res_json

if __name__ == '__main__':
    obj = WooApiUtility()
    rs_api = obj.get('products')
    import pdb; pdb.set_trace ()

