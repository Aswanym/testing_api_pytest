from ssqaapitestnew.src.helpers.order_helper import OrderHelper
from ssqaapitestnew.src.utilities.woo_api_utilities import WooApiUtility
import pdb
import pytest

pytestmark = [pytest.mark.regression, pytest.mark.orders]

@pytest.mark.parametrize(
    "new_status", [pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
                   pytest.param('completed', marks=pytest.mark.tcid56),
                   pytest.param('on-hold', marks=pytest.mark.tcid57)]
)
def test_update_order_status(new_status):

    # create order and check the order status
    order_helper = OrderHelper()
    rs_order = order_helper.create_order()
    current_status = rs_order['status']
    order_id = rs_order['id']

    # if the current status and new status is not same, then update the order status

    # assert current_status != new_status, f"Current status of order is already {new_status}, " \
    #                                      f"unable to run the test."
    payload = {"status": new_status}
    order_helper.call_update_order(order_id, payload)

    # get order information
    updated_order_info = order_helper.call_retrieve_an_order(order_id)

    # varify order status updated
    assert updated_order_info['status'] == new_status, f"Updated order status to {new_status}, " \
                                                       f"but order status is still {updated_order_info['status']}."

@pytest.mark.tcid58
def test_update_order_status_to_random_string():

    # create order
    order_helper = OrderHelper()
    rs_order = order_helper.create_order()
    order_id = rs_order['id']

    new_status = "bad_status"

    # update order with new status
    payload = {"status": new_status}
    rs_api = WooApiUtility().put(f"orders/{order_id}", payload, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', f"Updating an order with random string gives unexpected response code. " \
                                                   f"expected code: rest_invalid_param" \
                                                   f"actual code: {rs_api['code']}"
    assert rs_api['message'] == 'Invalid parameter(s): status', f"Updating an order with random string gives unexpected " \
                                                                f"response message. expected message: rest_invalid_param" \
                                                                f"actual message: {rs_api['message']}"


