from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.api.user import UserAPI
from models.ui.user import UserPage
from models.api.admin import AdminAPI
from models.ui.signup import SignupPage
import time
import libs.utils
import pytest
import os

API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")



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

    with page.expect_response(lambda r: r.url.endswith("/signup") and r.status == 200):
        signup.signup(username, password)

    home.navigate()
    home.login(username, password)
    time.sleep(2)

    user_page = UserPage(page)
    assert user_page.header_title.is_visible()



# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login_and_view_products(page: Page):
    home = HomePage(page)
    username = "test"
    password = "test123"

    home.navigate()
    home.login(username, password)

    user_page = UserPage(page)
    products = user_page.get_user_products()
    print("Products for user: ", products)


    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()
    expect(page.locator('h3:has-text("Your Products")')).to_be_visible()