# from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI

import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # get a new user
    username = libs.utils.generate_string_with_prefix()
    password = "test1234"

    user_api = UserAPI(BACKEND_URL)
    api_response = user_api.signup(username, password)
    assert api_response.status_code == 200

    api_response = user_api.login(username, password)
    assert api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    username = "mimmi"
    password = "1234"

    user_api = UserAPI(BACKEND_URL)
    api_response = user_api.login(username, password)
    assert api_response.status_code == 200

    user_profile_response = user_api.get_user_profile()
    assert user_profile_response.status_code == 200

    # check so "product" key exists
    user_profile = user_profile_response.json()
    assert "products" in user_profile

    # check so "products" is a list even tho it might be empty
    products = user_profile.get("products")
    assert isinstance(products, list)


# Given I am an authenticated user​
# When I log in into the application​
# Then I can assign a product to my own user
def test_assign_product_to_user():
    username = "mimmi"
    password = "1234"
    product_id = 4

    user_api = UserAPI(BACKEND_URL)
    api_response = user_api.login(username, password)
    assert api_response.status_code == 200

    # the lenght of the productlist before
    before_assigned_product = len(user_api.get_user_profile().json()["products"])

    api_response = user_api.assign_product_to_user(product_id)
    assert api_response.status_code == 200

    # the length after assigning a product

    after_assigned_product = len(user_api.get_user_profile().json()["products"])
    assert after_assigned_product == before_assigned_product + 1

    # check so the product_id exists in the product list by looping
    products = user_api.get_user_profile().json()
    product_ids = [product["id"] for product in products.get("products", [])]
    assert product_id in product_ids


# Given I am an authenticated user​
# When I log in into the application​
# Then I can remove a product from my own user
def test_remove_product_from_user():
    username = "mimmi"
    password = "1234"
    product_id = 4

    user_api = UserAPI(BACKEND_URL)
    api_response = user_api.login(username, password)
    assert api_response.status_code == 200

    # same as the assign product above but reversed
    # the lenght of the productlist before
    before_remove_product = len(user_api.get_user_profile().json()["products"])

    # remove a product
    api_response = user_api.remove_product_from_user(product_id)
    assert api_response.status_code == 200

    # the length after removing a product
    after_remove_product = len(user_api.get_user_profile().json()["products"])
    assert after_remove_product == before_remove_product - 1

    # check so the product_id no longer exists in the product list by looping
    products = user_api.get_user_profile().json()
    product_ids = [product["id"] for product in products.get("products", [])]
    assert product_id not in product_ids
