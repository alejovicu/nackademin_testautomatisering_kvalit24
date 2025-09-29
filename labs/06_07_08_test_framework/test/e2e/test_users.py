from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
from models.api.base import BaseAPI

import libs.utils
import os
import pytest

BASE_URL = os.getenv("APP_URL", "http://127.0.0.1:8000")

@pytest.fixture
def user_page(page: Page):

    base_api = BaseAPI(BASE_URL)
    base_api.login("user_account", "user_pass")
    page.add_init_script(
        f"window.localStorage.setItem('token', '{base_api.token}');")
    home_page = HomePage(page)
    user_page = UserPage(page)
    
    home_page.navigate()

    return user_page

# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    # complete code
    username = libs.utils.generate_string_with_prefix("user_")
    password = libs.utils.generate_string_with_prefix("pass_")
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()

    signup_page = SignupPage(page)
    # Wait for the signup request to finish before trying to login
    with page.expect_response(lambda r: r.url.endswith("/signup") and r.status == 200):
        signup_page.signup(username, password)
    signup_page.go_to_home()

    home_page.login(username, password)

    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    username = "user_account"
    password = "user_pass"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()
    expect(page.locator('h3:has-text("Your Products")')).to_be_visible()

# Given I am an authenticated user
# When I assign a product to myself
# Then the product should be assigned to me
def test_assign_product_to_user(user_page):
    user_page.add_product_to_user("Banan")
    expect(user_page.user_products.filter(has_text="Banan")).to_be_visible()

# Given I am an authenticated user
# When I unassign a product from myself
# Then the product should be unassigned from me
def test_unassign_product_from_user(user_page):
    user_page.remove_product_from_user("Banan")
    expect(user_page.user_products.filter(has_text="Banan")).not_to_be_visible()