import pdb

from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.order_helper import OrderHelper

import pytest

@pytest.mark.tcid48
def test_create_order_guest_user():

    # get a product from db
    product_dao = ProductDAO()
    rand_product = product_dao.get_random_product(1)
    product_id = rand_product[0]['ID']

    # make the call
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ]
    }
    order_helper = OrderHelper()
    order_json = order_helper.create_order(additional_args=info)
    pdb.set_trace()

    # verify response
    assert order_json, f"Create order response is empty."
    assert order_json['customer_id'] == 0, f"customer id for order created by guest user expected as 0," \
                                           f"but got '{order_json['customer_id']}'"
    assert len(order_json['line_items']) == 1, f"Expected only one item in the order but" \
                                               f" got '{len(order_json['line_items'])}' " \
                                               f"order_id '{order_json['id']}' " \


    # verify db
    pass