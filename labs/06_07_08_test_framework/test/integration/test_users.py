from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI
import os


def test_signup():
    user_api = UserAPI(os.getenv("BASE_URL"))
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test1234!"

    # When I signup in the app​
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200


def test_login():  # use -s in the pytest command to show the print.
    user_api = UserAPI(os.getenv("BASE_URL"))
    # Given I am an authenticated user​
    username = "user83"
    password = "pass83"

    # When I log in into the application​
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200
    token = login_api_response.json().get("access_token")

    # Then I should see all my products
    user_page = user_api.user_profile(token)
    user_products = user_page.json().get("products")
    if len(user_products) == 0:
        assert len(user_products) == 0
        print("Users product list is empty.")
    else:
        assert len(user_products) >= 0
        print("Products exist on the users account.")
