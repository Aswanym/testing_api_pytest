from ssqaapitestnew.src.utilities.request_utilities import RequestUtilitY
from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.products_helper import ProductHelper
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():

    req_helper = RequestUtilitY()
    rs_info = req_helper.get('products')
    assert rs_info, f"Get products api returned empty list."


@pytest.mark.tcid25
def test_get_product_by_id():

    # Get a product
    product_helper = ProductDAO()
    rand_product = product_helper.get_random_product()
    rand_product_id = rand_product[0]['ID']

    # make the call
    prd_helper = ProductHelper()
    res_api = prd_helper.get_product_by_id(rand_product_id)

    # varify
    assert rand_product[0]['post_title'] == res_api['name'],f"Api returned a different product. " \
                                                            f"expected name: {rand_product[0]['post_title']}" \
                                                            f"actual name: {res_api['name']}"






