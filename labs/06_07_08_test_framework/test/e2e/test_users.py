from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import libs.utils
import sys
import os
from test.conftest import setup, reset


def test_signup(page: Page):
    setup()
    home_page = HomePage(page)
    user_page = UserPage(page)
    signup_page = SignupPage(page)
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test1234!"
    home_page.nav()
    home_page.go_to_signup()
    # When I signup in the app​
    signup_page.signup(username, password)
    signup_page.go_to_home()
    # Then I should be able to log in with my new user
    home_page.login(username, password)
    user_page.logout_user()
    reset()


def test_login(page: Page):
    setup()
    home_page = HomePage(page)
    user_page = UserPage(page)
    course01 = os.getenv("product02", "Frontend programering 1")
    course02 = os.getenv("product03", "Backend programering 1")
    # Given I am an authenticated user​
    username = "user83"
    password = "pass83"
    # When I log in into the application​
    home_page.nav()
    home_page.login(username, password)
    # Then I should see all my products
    expect(user_page.page.get_by_text(course01)).to_be_visible()
    expect(user_page.page.get_by_text(course02)).to_be_visible()
    user_page.logout_user()
    reset()
