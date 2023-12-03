from ssqaapitestnew.src.utilities.request_utilities import RequestUtilitY
from ssqaapitestnew.src.dao.products_dao import ProductDAO
from ssqaapitestnew.src.helpers.products_helper import ProductHelper
from datetime import datetime, timedelta
import pytest
import pdb

@pytest.mark.regression
class TestGetProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_get_products_with_filter_after(self):

        # create payload

        """how many days of products wanted. get the date with which you have to
        filter products and convert it to isoformat"""
        x_days_from_today = 5
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        payload = dict()
        payload['after'] = after_created_date
        payload['per_page'] = 100

        # make call
        product_rs_api = ProductHelper().call_list_products(payload=payload)

        # varify response is not empty
        assert product_rs_api, f"filter product with after param gives empty list in return." \
                               f"product filter with date {_after_created_date}"

        # check with db
        products_db_rs = ProductDAO().get_products_with_filter(after=after_created_date)

        assert len(products_db_rs) == len(product_rs_api), f"while filtering Number of products returned by api and db are " \
                                                        f"different fora given time. " \
                                                        f"expected number of products: {len(products_db_rs)}, " \
                                                        f"actual: {len(product_rs_api)}"

        ids_in_api = [i['id'] for i in product_rs_api]
        ids_in_db = [i['ID'] for i in products_db_rs]
        id_diff = list(set(ids_in_db)-set(ids_in_api))
        assert not id_diff, f"product ids in api is not match with product ids in database"
