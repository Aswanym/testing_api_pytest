import pytest

pytestmark = pytest.mark.abc


# setting a fixture and setting the scope as module so that it will execute only once even when use this fixture on multiple places.
@pytest.fixture(scope='module')
def setup():
    print("")
    print(">>>> setup done <<<<")
    return {"id":1, "name":"kigini"}

@pytest.mark.abc
def test_login_page_valid_user(setup):  # functions should either start or end with test to consider by pytest as a test. 
    print("User logged in successfully")
    print("Function executed successfully")
    print(setup['name'])

@pytest.mark.regression
def test_login_wrong_password(setup):
    print("User given wrong password")
    print("Functin executed successfully")