from playwright.sync_api import Page
import pytest
import libs.utils
from models.api.user import UserAPI
from models.ui.user import UserPage
from models.ui.home import HomePage

FRONTEND_URL = "http://localhost"
API_URL = "http://localhost:8000"


@pytest.fixture
def user_api():
    return UserAPI(API_URL)


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup_and_login(page: Page, user_api):

    # Create a new user API
    username = libs.utils.generate_string_with_prefix("user")
    password = "test_1234?"

    sigup_response = user_api.signup(username, password)
    assert sigup_response.status_code == 200

    # Login with new user UI
    page.goto(FRONTEND_URL)
    page.locator("text=login").click()
    page.locator("input[placeholder='Username']").fill (username)
    page.locator("input[placeholder='Password']").fill(password)
    page.locator("button:has-text('Login')").click()

    page.wait_for_selector(f"text=Welcome, {username}!")
    assert page.locator(f"text=Welcome, {username}!").is_visible()


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login_existing_user(page: Page):
    username = "test"
    password = "test123"

    page.goto(FRONTEND_URL)
    page.locator("text=login").click()
    page.locator("input[placeholder='Username']").fill(username)
    page.locator("input[placeholder='Password']").fill(password)
    page.locator("button:has-text('Login')").click()

    page.wait_for_selector(f"text=Welcome, {username}!")
    assert page.locator(f"text=Welcome, {username}!").is_visible()

    page.wait_for_selector("text=Your Products:")
    product_elements = page.locator("text=Your Products: >> xpath=following-sibling::div/div")

    assert product_elements.count() > 0

    