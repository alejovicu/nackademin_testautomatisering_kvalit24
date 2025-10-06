import pytest
import libs.utils
import os

from models.api.user import UserAPI


BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def test_user_signup():
    username = libs.utils.generate_string_with_prefix("user")
    password = libs.utils.generate_string_with_prefix("pass")

    user_api = UserAPI(BACKEND_URL)

    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    login_api_response = user_api.login(username, password)

    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products

def test_login():
    username = libs.utils.generate_string_with_prefix("user")
    password = libs.utils.generate_string_with_prefix("pass")
    user_api = UserAPI(BACKEND_URL)
    user_api.signup(username, password)

    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200
    assert user_api.token is not None


