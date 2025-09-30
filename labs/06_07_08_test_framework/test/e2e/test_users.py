from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import libs.utils
import re


def test_signup(page: Page):
    home = HomePage(page)
    home.navigate()
    home.go_to_signup()

    signup = SignupPage(page)
    username = libs.utils.generate_string_with_prefix("user", 8)
    password = libs.utils.generate_string_with_prefix("pw", 12)
    signup.signup(username, password)
    signup.go_to_home()

    home.login(username, password)

    page.get_by_role("button", name="Logout").wait_for(timeout=5000)
    assert page.get_by_text("Your Products:").count() > 0

    page.evaluate("localStorage.setItem('token', 'expired.jwt')")
    page.reload(wait_until="domcontentloaded")

    assert page.get_by_role("button", name="Logout").count() == 0
    page.get_by_text("Don't have an account?").wait_for(timeout=5000)


def test_login_form_submits_with_enter(page: Page):
    # идём на логин
    page.goto("http://localhost:5173/#/login")
    page.get_by_placeholder(re.compile(r"username|email", re.I)).fill("admin")
    page.get_by_placeholder(re.compile(r"password", re.I)).fill("1234")

    # ключевая проверка: submit через Enter, без клика кнопки
    page.keyboard.press("Enter")

    # успешный вход подтверждаем кнопкой Logout
    page.get_by_role("button", name=re.compile(r"logout", re.I)).wait_for(timeout=5000)
