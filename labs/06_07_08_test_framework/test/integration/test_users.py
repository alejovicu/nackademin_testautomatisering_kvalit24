from playwright.sync_api import Page
import pytest
import libs.utils
from models.api.user import UserAPI


import os

API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")



# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = libs.utils.generate_string_with_prefix("pass_")

    user_api = UserAPI(API_URL)

    signup_api_response = user_api.signup(username, password)

    assert signup_api_response.status_code == 200
    
    login_api_response = user_api.login(username, password)

    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    user_api = UserAPI(API_URL)
    login_response = user_api.login("test", "test123")
    assert login_response.status_code == 200