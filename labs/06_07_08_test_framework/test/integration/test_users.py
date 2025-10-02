from playwright.sync_api import Page

# complete imports
import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI(BACKEND_URL)

    # When I signup in the app​
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products


def test_login():
    # Given I am an authenticated user
    username = "admin"
    password = "admin"

    user_api = UserAPI(BACKEND_URL)

    # When I log in into the application
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200

    # Extract token
    token = login_response.json()["access_token"]

    # Then I should see all my products
    admin_api = AdminAPI(BACKEND_URL, token=token)
    product_count = admin_api.get_current_product_count()

    assert product_count >= 0
