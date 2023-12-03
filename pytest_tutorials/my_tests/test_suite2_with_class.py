import pytest

# tags can specify to an entire file as below and also give multiple tags to single class or funtion this way
pytestmark = [pytest.mark.abc, pytest.mark.slow]

@pytest.fixture(scope='module')
def setup():
    print("")
    print(">>>> setup done <<<<")
    return {"id":1, "name":"kigini"}

# tags can given as decretors as below. 
@pytest.mark.smoke
class TestCheckout(object):   # class name of any test should start with Test. 

    
    # functions should either start or end with test to consider by pytest as a test. 
    def test_checkout_as_guest(self, setup):
        print("checkout succesfull")
        
    def test_checkout_as_user(self):
        print("checkout succesfull")
    