from playwright.sync_api import Page
import pytest
import libs.utils
import sqlite3
import os
from models.api.user import UserAPI

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")



def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234"

    user_api = UserAPI(BACKEND_URL)

    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)

    assert login_api_response.status_code == 200
    assert "access_token" in login_api_response.json()
    assert user_api.token == login_api_response.json()["access_token"]


def test_login():
    # Given I am an authenticated user​
    # note !! this user must be added pre-test run
    username = "test_1234"
    password = "test_1234"

    user_api = UserAPI(BACKEND_URL)

    # When I log in into the application​
    login_api_response = user_api.login(username, password)

    assert login_api_response.status_code == 200
    assert "access_token" in login_api_response.json()
    assert user_api.token == login_api_response.json()["access_token"]

    # Then I should see all my products
    # T-B-I

    



    