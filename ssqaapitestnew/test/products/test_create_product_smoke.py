import pdb

from ssqaapitestnew.src.utilities.generic_utilities import generate_random_name
from ssqaapitestnew.src.utilities.request_utilities import RequestUtilitY
from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.products_helper import ProductHelper
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid26
def test_create_product():

    # create payload
    payload = dict()
    payload['name'] = generate_random_name(length=20)
    payload['type'] = 'simple'
    payload['regular_price'] = '100'

    # create product
    prod_helper = ProductHelper()
    rs_api = prod_helper.call_create_product(payload)

    # varify response is not empty
    assert rs_api, f"create product response was empty. payload: {payload}"
    assert rs_api['name'] == payload['name'], f"create product response has unexpected name" \
                                              f"expected name: {payload['name']}, " \
                                              f"actual name : {rs_api['name']}"
    product_id = rs_api['id']
    rs_api_product_name = rs_api['name']

    # check created product exists in db
    prod_rs_api = ProductDAO().get_product_by_id(product_id)

    assert prod_rs_api[0]['post_title'] == rs_api_product_name, f"Database returned a different product title than " \
                                                            f"expected. expected name: {rs_api_product_name}, " \
                                                            f"actual name: {prod_rs_api[0]['post_title']}, " \
                                                            f"product id = {product_id}"


