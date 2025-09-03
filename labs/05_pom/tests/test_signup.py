from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage

username = "123444"
password = "bandola"


def test_create_account(page: Page, credentials):
    username, password = credentials

    home_page = HomePage(page)
    signup_page = SignupPage(page)
    login_page = LoginPage(page)

    home_page.navigate()
    login_page.navigate_to_signup()
    signup_page.create_account(username, password)


def test_login(page: Page, credentials):
    username, password = credentials

    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate()
    login_page.login(username, password)
    assert page.get_by_text(f"Welcome, {username}!").is_visible()
