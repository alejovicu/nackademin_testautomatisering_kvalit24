from playwright.sync_api import Page, expect
import pytest

from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os


import libs.utils

### RUN 'pytest test_data_admin.py' first to register admin credentials


# Signup user for test_login_and_get_products
@pytest.fixture(scope="session")
def signup_user():
    user_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    username = libs.utils.generate_string_with_prefix()
    password = "test_4321"
    user_api.signup(username, password)
    return username, password


#####################################################
# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
#####################################################
def test_signup_and_login(page: Page):
    ### ARRANGE - Given I am a new potential customer​
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    user_page = UserPage(page)
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234"

    ### ACT - When I signup in the app​
    home_page.navigate()
    home_page.navigate_to_signup()
    signup_page.signup_user(username, password)

    ### ASSERT - Then I should be able to log in with my new user
    signup_page.navigate_to_login()
    home_page.login_user(username, password)
    # Is the "Welcome, <user>"-message visible?
    user_message = user_page.welcome_message
    expect(user_message).to_be_visible()
    # Is it the logged in user?
    assert username in user_message.inner_text()


#####################################
# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
#####################################
def test_login_and_get_products(page: Page, signup_user):
    ### ARRANGE - Given I am an authenticated user​
    home_page = HomePage(page)
    user_page = UserPage(page)
    username, password = signup_user  # Signup user

    home_page.navigate()

    ### ACT - When I log in into the application​
    home_page.login_user(username, password)

    ### ASSERT - Then I should see all my products
    # Is the product list visible to the customer?
    product_container = user_page.products_container
    expect(product_container).to_be_visible()
