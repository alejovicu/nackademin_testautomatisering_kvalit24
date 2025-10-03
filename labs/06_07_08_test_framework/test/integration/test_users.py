from playwright.sync_api import Page
from models.api.user import UserAPI
import libs.utils

def test_signup():
    # Given I am a new potential customer
    username = libs.utils.generate_string_with_prefix("user", 6)
    password = "test_1234?"

    user_api = UserAPI('http://host.docker.internal:8000')

    # When I signup in the app
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

def test_login():
    # Given I am an authenticated user
    username = libs.utils.generate_string_with_prefix("user", 6)
    password = "test_1234?"

    user_api = UserAPI('http://host.docker.internal:8000')

    # When I log in into the application
    user_api.signup(username, password)  # Ensure the user exists
    login_api_response = user_api.login(username, password)

    # Then I should see all my products
    assert login_api_response.status_code == 200