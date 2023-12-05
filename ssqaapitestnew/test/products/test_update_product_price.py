from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.products_helper import ProductHelper
import pdb
import random
import pytest

@pytest.mark.tcid61
def test_update_product_regular_price():

    # get an existing product
    product_dao = ProductDAO()
    product_helper = ProductHelper()
    rand_products = product_dao.get_random_product(5)

    for prod in rand_products:
        pdb.set_trace()
        product_id = prod['ID']
        product_data = product_helper.call_retrieve_product(product_id)
        if product_data['sale_price']:
            continue
        else:
            break

    else:
        test_product = random.choice(rand_products)
        product_id = test_product[0]['ID']
        product_helper.call_update_product(product_id, {'sale_price': ''})

    # create a random price
    price = f"{str(random.randint (10, 200))}.{str(random.randint(10, 99))}"
    payload = dict()
    payload['regular_price'] = price

    # Update the product price
    updated_rs = product_helper.call_update_product(product_id, payload)

    # varify the price, regular price in the updated response with given price
    assert updated_rs['price'] == price, f"Updating price of product id {product_id} is giving unexpected price" \
                                         f"Expected price: {price}, actual price: {updated_rs['price']}"

    assert updated_rs['regular_price'] == price, f"Updating price of product id {product_id} is giving unexpected regular price" \
                                                 f"Expected regular price: {price}, actual regular price: {updated_rs['regular_price']}"

    # Retrieve the product again and check if the price and regular price have updated.
    product_rs = product_helper.call_retrieve_product(product_id)
    assert product_rs['price'] == price, f"Updating price of product id {product_id} is giving unexpected price" \
                                         f"Expected price: {price}, actual price: {product_rs['price']}"

    assert product_rs['regular_price'] == price, f"Updating price of product id {product_id} is giving unexpected regular price" \
                                                 f"Expected regular price: {price}, actual regular price: {product_rs['regular_price']}"
