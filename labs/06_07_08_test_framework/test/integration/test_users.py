#from playwright.sync_api import Page
# complete imports
#import libs.utils
#from models.api.user import UserAPI


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
#def test_signup():
    # Given I am a new potential customer​
    #username = libs.utils.generate_string_with_prefix()
    #password = "test_1234?"

    #user_api = UserAPI('http://localhost:8000')

    # When I signup in the app​
    #signup_api_response = user_api.signup(username,password)
    #assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    #login_api_response = user_api.login(username,password)
    #assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
#def test_login():
    # complete code
    #pass

import os
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# tests/integration/test_users.py

import pytest
from models.api.user import UserAPI
import libs.utils

@pytest.mark.usefixtures("user_token")
def test_signup(user_api):
    username = libs.utils.generate_string_with_prefix("user")
    password = "testpass123"
    response = user_api.signup(username, password)
    assert response["username"] == username

@pytest.mark.usefixtures("user_token")
def test_login(user_api):
    username = "user_qa"
    password = "pass_5678"
    response = user_api.login(username, password)
    assert "access_token" in response
    assert response["token_type"] == "bearer"

def test_get_user_info(user_token):
    user_api = UserAPI(base_url=BACKEND_URL)
    user_api.set_token(user_token)
    profile = user_api.get_user()
    assert "username" in profile
