from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.user import UserPage
from models.ui.signup import SignupPage
from models.api.user import UserAPI
from libs.utils import generate_string_with_prefix
import os

VITE_BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    username = generate_string_with_prefix()
    password = "1234"

    home_page = HomePage(page)
    signup_page = SignupPage(page)
    user_page = UserPage(username, page)

    # Navigate to home
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # Go to signup page
    home_page.go_to_signup()
    page.wait_for_load_state("networkidle")

    # Handle alert dialog when signing up
    with page.expect_event("dialog") as dialog_info:
        signup_page.signup(username, password)  # triggers alert
    dialog = dialog_info.value
    dialog.accept()  # accept the alert

    page.wait_for_load_state("networkidle")

    # Click login button after signup
    signup_page.signup_btn_login.click()
    page.wait_for_load_state("networkidle")

    # Log in
    home_page.login(username, password)
    page.wait_for_load_state("networkidle")

    # Wait until the welcome message appears
    user_page.title_user.wait_for(state="visible", timeout=5000)

    # Assertions
    assert username in user_page.title_user.inner_text()
    assert user_page.title_user.is_visible(), "User title is not visible"
    assert user_page.title_user.inner_text() == f"Welcome, {username}!"


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_cart_when_user_have_selected_products(page: Page):
    username = "testuser00"  # User that has products assigned in test data
    password = "1234"

    home_page = HomePage(page)
    user_page = UserPage(username, page)
    user_api = UserAPI(VITE_BACKEND_URL)
    token = user_api.login(username, password)

    # Setting token through local storage to avoid logging in through the UI every time
    page.add_init_script(
        f"""
    window.localStorage.setItem("token", "{token}");
    """
    )
    page.wait_for_load_state("networkidle")
    home_page.navigate()
    page.wait_for_load_state("networkidle")
    user_products = user_page.get_user_products()
    page.wait_for_load_state("networkidle")
    assert len(user_products) > 0, "Expected at least one product"


def test_cart_when_user_has_not_selected_products(page: Page):
    username = "testuser11"  # User that has no products assigned in test data
    password = "1234"

    home_page = HomePage(page)
    user_page = UserPage(username, page)
    user_api = UserAPI(VITE_BACKEND_URL)
    token = user_api.login(username, password)

    # Setting token through local storage to avoid logging in through the UI every time
    page.add_init_script(
        f"""
    window.localStorage.setItem("token", "{token}");
    """
    )
    page.wait_for_load_state("networkidle")
    home_page.navigate()
    page.wait_for_load_state("networkidle")
    user_page.get_user_products()
    page.wait_for_load_state("networkidle")

    no_products_locator = page.get_by_text("No products assigned.")
    assert no_products_locator.is_visible()
