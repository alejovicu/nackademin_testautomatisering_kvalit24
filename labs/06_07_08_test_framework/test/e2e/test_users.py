from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from facade.users import UsersFacade
import libs.utils
import re

# Inline helper (no wait_for_response needed)
def _assert_logged_in(page: Page, timeout_ms=10000):
    expect(page.get_by_role("button", name="Logout")).to_be_visible(timeout=timeout_ms)
    expect(page).not_to_have_url(re.compile(r"/login\b"))

def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix(prefix="user")
    password = "pass123"

    home = HomePage(page)
    signup = SignupPage(page)

    home.navigate()
    home.go_to_signup()

    signup.signup(username, password)
    signup.go_to_home()

    home.login(username, password)
    _assert_logged_in(page)

    expect(page.get_by_text("Your Products:")).to_be_visible()

def test_signup_auth(page: Page):
    facade = UsersFacade(page)
    username, password = facade.login_as_new_user()
    _assert_logged_in(page)

    expect(page.get_by_text("Your Products:")).to_be_visible()