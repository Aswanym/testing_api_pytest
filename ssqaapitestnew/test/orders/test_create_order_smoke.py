import pdb
from ssqaapitestnew.src.dao.orders_dao import OrdersDAO
from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.order_helper import OrderHelper
from ssqaapitestnew.src.helpers.customers_helper import CustomerHelper
import pytest

@pytest.mark.orders
@pytest.mark.tcid48
def test_create_order_guest_user():

    # get a product from db
    product_dao = ProductDAO()
    rand_product = product_dao.get_random_product(1)
    product_id = rand_product[0]['ID']

    customer_id = 0

    # To update the order creation json give product from our db.
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        "customer_id": customer_id
    }
    order_helper = OrderHelper()
    order_json = order_helper.create_order(additional_args=info)

    product_list = [{'product_id': product_id}]

    # varify order created
    order_helper.varify_order_created (order_json, customer_id, product_list)


@pytest.mark.orders
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer():

    # get a product from db
    product_dao = ProductDAO()
    rand_product = product_dao.get_random_product(1)
    product_id = rand_product[0]['ID']

    # create a customer
    cust_helper = CustomerHelper()
    cust_info = cust_helper.create_customer()
    customer_id = cust_info['id']

    # create additional info to pass to the order json
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }

        ],
        "customer_id": customer_id
    }

    # create order
    order_helper = OrderHelper()
    order_json = order_helper.create_order(additional_args=info)

    product_list = [{'product_id': product_id}]

    # varify order created
    order_helper.varify_order_created(order_json, customer_id, product_list)
