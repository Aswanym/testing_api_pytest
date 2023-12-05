from ssqaapitestnew.src.utilities.request_utilities import RequestUtilitY
from ssqaapitestnew.src.utilities.woo_api_utilities import WooApiUtility

class ProductHelper (object):
    def __init__(self):
        self.pdt_helper = RequestUtilitY()
        self.woo_api_utility = WooApiUtility()

    def get_product_by_id(self, product_id):
        res_api = self.pdt_helper.get(f'products/{product_id}')
        return res_api

    def call_create_product(self, payload):
        rs_api = self.pdt_helper.post(endpoint='products', payload=payload, expected_status_code=201)
        return rs_api

    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            if 'per_page' not in payload.keys():
                payload['per_page'] = 100

            # add the current page number to the call
            payload['page'] = i
            rs_api = self.pdt_helper.get('products', payload=payload)

            # if there is no response then stop because there are not more data

            if not rs_api:
                break;
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products

    def call_update_product(self, product_id, payload):
        rs_update = self.woo_api_utility.put(f"products/{product_id}", payload)
        return rs_update

    def call_retrieve_product(self, product_id):
        rs_api = self.woo_api_utility.get(f"products/{product_id}")
        return rs_api

