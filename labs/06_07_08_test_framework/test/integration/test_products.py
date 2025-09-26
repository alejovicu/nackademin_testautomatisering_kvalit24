import libs.utils
import pytest
from models.api.admin import AdminAPI
from models.api.user import UserAPI

import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    username = "admin1"
    password = "1234"
    product_name = "Testprodukt_2"

    # logg in via user login
    user_api = UserAPI(BACKEND_URL)
    api_response = user_api.login(username, password)
    assert api_response.status_code == 200
    # get the access token and check its there
    token = api_response.json().get("access_token")
    assert token is not None
    # go to admin with access token
    admin_api = AdminAPI(BACKEND_URL, token)

    # check amount of products before add
    api_response = admin_api.get_current_product_count()
    count_before_add = len(api_response.json())

    # add a product to the catalog
    api_response = admin_api.create_product(product_name)
    # count the products after the added one
    api_response = admin_api.get_current_product_count()
    count_after_add = len(api_response.json())
    assert api_response.status_code == 200
    assert count_before_add == count_after_add - 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    username = "admin1"
    password = "1234"
    product_delete_id = 2

    # logg in via user login
    user_api = UserAPI(BACKEND_URL)
    api_response = user_api.login(username, password)
    assert api_response.status_code == 200
    # get the access token and check its there
    token = api_response.json().get("access_token")
    assert token is not None
    # go to admin with access token
    admin_api = AdminAPI(BACKEND_URL, token)

    # check the length of the list before and after the product is deleted.
    api_response = admin_api.get_current_product_count()
    count_before_delete = len(api_response.json())

    # delete by id and check if the delete happens or not
    delete_response = admin_api.delete_product_by_id(product_delete_id)
    assert delete_response.status_code in (200, 204)

    # check and compare len after delete
    api_response = admin_api.get_current_product_count()
    count_after_delete = len(api_response.json())
    assert count_before_delete == count_after_delete + 1
