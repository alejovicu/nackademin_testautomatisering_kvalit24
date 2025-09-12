from playwright.sync_api import Page
import pytest
import libs.utils
import sqlite3
from models.api.user import UserAPI

BASE_URL = 'http://localhost:8000'


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234"

    user_api = UserAPI(BASE_URL)

    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    
    # Given I am an authenticated user​
    username = "test_1234"
    password = "test_1234"

    user_api = UserAPI(BASE_URL)

    # When I log in into the application​
    login_resp = user_api.login(username, password)
    assert login_resp.status_code == 200

    # Then I should see all my products
    # TB E

    



    