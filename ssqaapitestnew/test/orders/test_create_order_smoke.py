import pdb
from ssqaapitestnew.src.dao.orders_dao import OrdersDAO
from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.order_helper import OrderHelper

import pytest

@pytest.mark.orders
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

    # verify response
    assert order_json, f"Create order response is empty."
    assert order_json['customer_id'] == 0, f"customer id for order created by guest user expected as 0," \
                                           f"but got '{order_json['customer_id']}'"
    assert len(order_json['line_items']) == 1, f"Expected only one item in the order but" \
                                               f" got '{len(order_json['line_items'])}' " \
                                               f"order_id '{order_json['id']}' " \


    # verify db
    order_dao = OrdersDAO()
    order_id = order_json['id']
    line_info = order_dao.get_order_lines_by_order_id(order_id)
    assert line_info, f"Create order, line item not created in db. order id : {order_id}"

    line_items = [info for info in line_info if info['order_item_type'] == 'line_item']
    assert len(line_items) == 1, f"Expected one line item but found {len(line_items)}. order id {order_id}"

    line_item_id = line_items[0]['order_item_id']
    item_details = order_dao.get_order_items_details(line_item_id)
    db_product_id = item_details['_product_id']

    assert str(db_product_id) == str(product_id), f"Create order order 'product id ' is doesn't match with API. " \
                                        f"API product id {product_id}, db product id {db_product_id}"

