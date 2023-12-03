
from ssqaapitestnew.src.utilities.generic_utilities import generate_random_email_and_password
from ssqaapitestnew.src.helpers.customers_helper import CustomerHelper
from ssqaapitestnew.src.dao.customers_dao import CustomerDAO
from ssqaapitestnew.src.utilities.request_utilities import RequestUtilitY
import logging as logger
import pdb
import pytest

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("Test: create new customer with email and password")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first_name in the response
    assert cust_api_info['email'] == email, f'Create customer api return wrong email. Email: {email}'
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name, but it should be empty."

    # verify customer is created in database
    cust_dao = CustomerDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_db = cust_info[0]['ID']
    id_in_api = cust_api_info['id']
    assert id_in_api == id_in_db, f"Created customer 'id' is not same as 'ID' in database." \
                                  f"Email: {email}"

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    # Get an existing email from database
    cust_dao = CustomerDAO()
    existing_cust_info = cust_dao.get_existing_email()
    existing_email = existing_cust_info[0]['user_email']

    # call request post method with existing email
    payload = {
        'email': existing_email,
        'password': 'password1'
    }
    request_utility = RequestUtilitY()
    rs_api = request_utility.post('customers', payload=payload, expected_status_code=400)
    assert rs_api['code'] == 'registration-error-email-exists', f"Create customer with existing email error code is not " \
                                                                f"correct. Expected: 'registration-error-email-exists'" \
                                                                f"Actual: {rs_api['code']}"






