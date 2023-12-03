
from ssqaapitestnew.src.utilities.request_utilities import RequestUtilitY
import pytest

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtilitY()
    rs_api = req_helper.get('customers')

    assert rs_api, f"Response of api is empty"
