from playwright.sync_api import Page
from models.ui.home import HomePage
from models.api.user import UserAPI
from models.ui.user import UserPage
from models.api.admin import AdminAPI
from models.ui.signup import SignupPage
import time
import libs.utils
import pytest
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")

@pytest.fixture
def admin_api():
    username = "admin"
    password = "admin123"

    user_api = UserAPI(API_URL)
    login_response = user_api.login(username, password)
    login_response.raise_for_status()
    token = login_response.json()["access_token"]
    return AdminAPI(API_URL, token=token)

# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    home = HomePage(page)
    home.navigate()
    time.sleep(2)

    home.go_to_signup()
    signup = SignupPage(page)

    username = libs.utils.generate_string_with_prefix("user")
    password = "test123"

    
    signup.signup(username, password)

    home.navigate()
    home.login(username, password)
    time.sleep(2)

    user_page = UserPage(page)
    assert user_page.header_title.is_visible()



# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login_and_view_products(page: Page, admin_api):
    home = HomePage(page)
    username = "test"
    password = "test123"

    home.navigate()
    home.login(username, password)

    user_page = UserPage(page)
    products = user_page.get_user_products_swagger()
    print("Products for user: ", products)

    assert isinstance(products, list)
