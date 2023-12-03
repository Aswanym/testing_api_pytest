from ssqaapitestnew.src.helpers.order_helper import OrderHelper
import pdb
import pytest


@pytest.mark.orders
@pytest.mark.regression
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
    params = {"status": new_status}
    order_helper.call_update_order(order_id, params)

    # get order information
    updated_order_info = order_helper.call_retrieve_an_order(order_id)

    # varify order status updated
    assert updated_order_info['status'] == new_status, f"Updated order status to {new_status}, " \
                                                       f"but order status is still {updated_order_info['status']}."
