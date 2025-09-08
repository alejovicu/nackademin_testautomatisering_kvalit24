from playwright.sync_api import Page
# complete imports
import libs.utils
from models.api.user import UserAPI
import pytest
from facade.users import UsersFacade


def test_signup():
    
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI('http://localhost:8000')

    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200


def test_login():

    # Given I am an authenticated user​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI("http://localhost:8000")
    user_api.signup(username, password)

    # When I log in into the application​
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200
    token = login_response.json().get("access_token")

    # Then I should see all my products
    products_response = user_api.get_user_products(token)
    assert products_response.status_code == 200
