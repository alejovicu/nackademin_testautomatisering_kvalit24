from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.user import UserPage
from models.ui.signup import SignupPage
from models.api.user import UserAPI
from libs.utils import generate_string_with_prefix
import libs.utils
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
USER_USERNAME = ("USER_USERNAME", "user2")
USER_PASSWORD  = os.getenv("USER_PASSWORD", "5678")

def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    home_page = HomePage(page)
    signup_page = SignupPage(page)
    user_page = UserPage(username, page)

    home_page.navigate()
    page.wait_for_load_state("networkidle")

    home_page.go_to_signup()

    page.wait_for_load_state("networkidle")

    with page.expect_event("dialog") as dialog_info:
        signup_page.signup(username, password)
    dialog = dialog_info.value

    dialog.accept()

    page.wait_for_load_state("networkidle")

    signup_page.signup_btn_login.click()

    page.wait_for_load_state("networkidle")

    home_page.login(username, password)
    page.wait_for_load_state("networkidle")

    user_page.title_user.wait_for(state="visible", timeout=5000)

    assert username in user_page.title_user.inner_text()


def test_login_auth_user(page: Page):
    username = "user2"
    password = "5678"

    home_page = HomePage(page)
    user_page = UserPage(username, page)
    user_api = UserAPI(BACKEND_URL)

    home_page.navigate()

    page.wait_for_load_state("networkidle")
    home_page.navigate()
    page.wait_for_load_state("networkidle")
    user_page.get_user_products()
    page.wait_for_load_state("networkidle")

    no_products_locator = page.get_by_text("No products assigned.")
    expect(page.locator(".product-grid .product-item")).to_have_count(0)
  
