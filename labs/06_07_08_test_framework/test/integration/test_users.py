from playwright.sync_api import Page
from models.api.user import UserAPI
import libs.utils
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
user_api = UserAPI(BACKEND_URL)
username = "test123"
password = "test_123"


def test_signup():
    # Given I am a new potential customer
    test_username = libs.utils.generate_string_with_prefix()
    test_password = "pass_test"
    print(test_username)

    # When I signup in the app​
    signup_api = user_api.signup(test_username, test_password)
    assert signup_api.status_code == 200

    # Then I should be able to log in with my new user
    login_api = user_api.login(test_username, test_password)
    assert login_api.status_code == 200


    
def test_login():

    # Given I am an authenticated user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    # Token from the user
    user_token = login_api_response.json()["access_token"]
    user_api.user_token(user_token)


def test_add_product_to_user():
    
    # Given I am an authenticated user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    # Token from the user
    token = login_api_response.json()["access_token"]
    user_api.user_token(token)

    
    product_id = 2
    new_product = user_api.add_product_to_user(product_id)
    assert new_product.status_code == 200
    assert new_product is not None


def test_remove_product_from_user():
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    
    token = login_api_response.json()["access_token"]
    user_api.user_token(token)

    product_id = 1
    remove_product = user_api.remove_product_from_user(product_id)
    assert remove_product.status_code == 200
