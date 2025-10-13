# complete imports
from playwright.sync_api import Page
from libs.utils import generate_string_with_prefix
from models.api.user import UserAPI
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def test_signup():
    # Given I am a new potential customer​
    username = generate_string_with_prefix()
    password = "test1234"

    print(username, password)

    user_api = UserAPI(BACKEND_URL)
    # When I signup in the app​
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200


def test_login():
    # Given I am an authenticated user​
    username = "test_admin"
    password = "test1234"

    user_api = UserAPI(BACKEND_URL)

    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    # Then I should see all my products
    user_api_response = user_api.get_user_details(user_api.token)
    assert user_api_response.status_code == 200
    data = user_api_response.json()
    assert data["products"] == []