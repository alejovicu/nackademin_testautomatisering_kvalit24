from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.user import UserPage
from models.ui.signup import SignupPage
from models.api.user import UserAPI
from libs.utils import generate_string_with_prefix
import libs.utils
import os

VITE_BACKEND_URL = os.getenv("VITE_BACKEND_URL", "http://localhost:8000")

def test_signup(page: Page):
    username = generate_string_with_prefix()
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

    assert user_page.title_user.inner_text() == f"Welcome,{username}!"


def test_login_auth_user(page: Page):
    username = "testing1"
    password = "1234"

    home_page = HomePage(page)
    user_page = UserPage(username, page)
    user_api = UserAPI(VITE_BACKEND_URL)

    response = user_api.login(username, password)
    assert response.status_code == 200
    token = user_api.token

    page.wait_for_load_state("networkidle")
    home_page.navigate()
    page.wait_for_load_state("networkidle")
    user_products = user_page.get_user_products()
    page.wait_for_load_state("networkidle")

    assert len(user_products) > 0, "Expected at least one product"
