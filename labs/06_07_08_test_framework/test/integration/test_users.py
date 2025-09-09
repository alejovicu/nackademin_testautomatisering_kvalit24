from playwright.sync_api import Page
# complete imports
import libs.utils
from models.api.user import UserAPI
import pytest


def test_signup():
    
    # GIVEN I AM A NEW POTENTIAL CUSTOMER
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI('http://localhost:8000')

    # WHEN I SIGNUP IN THE APP
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # THEN I SHOULD BE ABLE TO LOG IN WITH MY NEW USER
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200


def test_login_empty_list():

    # GIVEN I AM AN AUTHENTICATHED USER
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI("http://localhost:8000")
    user_api.signup(username, password)

    # WHEN I LOG INTO THE APPLICATION
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200
    token = login_response.json().get("access_token")

    # THEN I SHOULD SEE ALL MY PRPODUCTS
    products_response = user_api.get_user_products(token)
    assert products_response.status_code == 200
    assert "products" in products_response.json(), "Products key not found in response"


# Extra test for practice
# (Assumes that a product with id==1 exists in the DB)
def test_login_one_item_in_list():

    # Given I am an authenticated user​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI("http://localhost:8000")
    user_api.signup(username, password)

    # When I log in into the application​
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200
    token = login_response.json().get("access_token")

    # Assign product to user, assumes a product with id 1 exists
    product_id = 1
    assigned_product_response = user_api.add_product_to_user_via_id(product_id, token)
    assert assigned_product_response.status_code == 200

    # Then I should see all my products
    products_response = user_api.get_user_products(token)
    assert products_response.status_code == 200

    data = products_response.json()
    assert "products" in data, "Products key not found in response"

    product_ids = [p["id"] for p in data["products"]]
    assert product_id in product_ids, "Added product is not in product list"

    # Clean-up
    id_to_delete = 1
    delete_response = user_api.remove_product_from_user_via_id(id_to_delete, token)
    assert delete_response.status_code == 200
