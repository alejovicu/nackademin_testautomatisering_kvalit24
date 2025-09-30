from playwright.sync_api import Page
from models.api.user import UserAPI
import libs.utils
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
user_api = UserAPI(BACKEND_URL)
USERNAME = "test_user"
PASSWORD = "user_test321"

def test_signup():

    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234"
    print(username)

    # When I signup in the app​
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200
    

def test_login():

    # Given I am an authenticated user​
    login_api_response = user_api.login(USERNAME, PASSWORD)
    assert login_api_response.status_code == 200

    # Token from the user
    user_token = login_api_response.json()["access_token"]
    user_api.set_token(user_token)


def test_add_product_to_user():
    
    # Given I am an authenticated user​
    login_api_response = user_api.login(USERNAME, PASSWORD)
    assert login_api_response.status_code == 200

    # Token from the user
    user_token = login_api_response.json()["access_token"]
    user_api.set_token(user_token)

    # User adds the product to their own account
    product_id = 5
    add_product_response = user_api.add_product_to_user(product_id)
    assert add_product_response.status_code == 200
    assert add_product_response is not None


def test_remove_product_from_user():

    # Given I am an authenticated user​
    login_api_response = user_api.login(USERNAME, PASSWORD)
    assert login_api_response.status_code == 200

    # Token from the user
    user_token = login_api_response.json()["access_token"]
    user_api.set_token(user_token)

    product_id = 2
    remove_product_response = user_api.remove_product_from_user(product_id)
    assert remove_product_response.status_code == 200