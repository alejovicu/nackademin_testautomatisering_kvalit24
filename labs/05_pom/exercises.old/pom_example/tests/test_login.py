from playwright.sync_api import Page
from models.login import LoginPage
from models.signup import SignupPage

import libs.utils


def test_valid_login(page: Page):
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.login("admin", "1234")


def test_login_with_new_user(page: Page):
    po_login = LoginPage(page)
    po_signup = SignupPage(page)

    po_login.login_btn_signup.click()
    username = libs.utils.generate_username()
    password = "testtest"
    po_signup.signup(username, password)

    po_signup.signup_btn_login.click()

    po_login.login(username.password)
