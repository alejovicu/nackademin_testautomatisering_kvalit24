# tests/e2e/test_users.py
import os, re, time, requests
from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import libs.utils

APP_URL = os.getenv("FRONTEND_URL") or os.getenv("APP_FRONT_URL") or "http://localhost:5173"
BACK_URL = os.getenv("BACKEND_URL") or os.getenv("APP_BACK_URL") or "http://localhost:8000"

def _api_signup(username: str, password: str):
    r = requests.post(f"{BACK_URL}/signup", json={"username": username, "password": password})
    if r.status_code not in (200, 201, 400, 409):
        r.raise_for_status()

def _api_login(username: str, password: str) -> str:
    r = requests.post(f"{BACK_URL}/login", json={"username": username, "password": password})
    r.raise_for_status()
    token = r.json().get("access_token")
    assert token, "No access_token in login response"
    return token

def _open_as_new_user(page: Page) -> tuple[str, str]:
    username = libs.utils.generate_string_with_prefix("user")
    password = "pass123"
    _api_signup(username, password)
    token = _api_login(username, password)
    page.add_init_script(f"window.localStorage.setItem('token', '{token}');")
    page.goto(APP_URL)
    page.wait_for_load_state("networkidle")
    return username, password

def _assert_logged_in(page: Page, timeout_ms=10000):
    expect(page.get_by_role("button", name="Logout")).to_be_visible(timeout=timeout_ms)
    expect(page).not_to_have_url(re.compile(r"/login\b"))

# Given I am a new potential customer
# When I signup in the app
# Then I should be able to log in with my new user
def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix("user")
    password = "pass123"

    home = HomePage(page)
    signup = SignupPage(page)

    home.navigate()
    home.go_to_signup()
    signup.signup(username, password)
    signup.go_to_home()

    # Login via API + inject
    token = _api_login(username, password)
    page.add_init_script(f"window.localStorage.setItem('token', '{token}');")
    page.goto(APP_URL)

    _assert_logged_in(page)
    expect(page.get_by_text("Your Products:")).to_be_visible()

# Given I am an authenticated user
# When I log in into the application
# Then I should see all my products
def test_signup_auth(page: Page):
    _open_as_new_user(page)
    _assert_logged_in(page)
    expect(page.get_by_text("Your Products:")).to_be_visible()