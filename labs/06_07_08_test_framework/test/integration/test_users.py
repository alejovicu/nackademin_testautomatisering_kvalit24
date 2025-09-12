from playwright.sync_api import Page
import pytest
import libs.utils

from models.api.user import UserAPI

### RUN 'pytest test_data_admin.py' first to register admin credentials


# Signup user for test_login_and_get_products
@pytest.fixture(scope="session")
def signup_user():
    user_api = UserAPI("http://localhost:8000")
    username = libs.utils.generate_string_with_prefix()
    password = "test_4321"
    user_api.signup(username, password)
    return username, password


####################################################
# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
####################################################
def test_signup_and_login():
    ### ARRANGE - Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234"
    user_api = UserAPI("http://localhost:8000")

    ### ACT - When I signup in the app​
    # Signup new customer
    signup_api_response = user_api.signup(username, password)
    # Validate signup
    assert signup_api_response.status_code == 200

    ### ASSERT - Then I should be able to log in with my new user
    # Login new user
    login_api_response = user_api.login(username, password)
    # Do we get correct respons code?
    assert login_api_response.status_code == 200
    # Does user bearer token exist?
    assert login_api_response.json().get("access_token")


####################################################
# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
####################################################
def test_login_and_get_products(signup_user):
    ### ARRANGE - Given I am an authenticated user​
    username, password = signup_user  # get new user
    user_api = UserAPI("http://localhost:8000")

    ### ACT - When I log in into the application​
    # login user and store bearer token
    login_user = user_api.login(username, password)
    access_token = login_user.json().get("access_token")

    # get user profile with products
    user_profile = user_api.get_products_from_user(access_token)
    total_products = user_profile.json().get("products")

    ### ASSERT - Then I should see all my products
    # Do we get correct respons code?
    assert user_profile.status_code == 200
    # Does the customer product list exist?
    assert isinstance(total_products, list)
