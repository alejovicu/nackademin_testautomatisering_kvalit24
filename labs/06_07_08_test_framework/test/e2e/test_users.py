from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import libs.utils
import pytest
import sys
import os
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(dotenv_path=env_path)


@pytest.mark.order(5)
def test_setup_user():
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL"))
    username_admin = os.getenv("admin_username")
    password_admin = os.getenv("admin_password")
    username = os.getenv("admin_username")
    password = os.getenv("admin_password")
    normal_user = "user83"
    normal_password = "pass83"
    course01 = os.getenv("product01")
    course02 = os.getenv("product02")
    course03 = os.getenv("product03")
    course04 = os.getenv("product04")
    user_api.signup(username, password)
    user_api.signup(normal_user, normal_password)
    admin_token = user_api.login_token(username, password)
    admin_api.set_token(admin_token)
    admin_api.create_product(course01)
    admin_api.create_product(course02)
    admin_api.create_product(course03)
    admin_api.create_product(course04)

    token = user_api.login_token(normal_user, normal_password)
    user_api.add_product_to_user(token, course02)
    user_api.add_product_to_user(token, course03)


@pytest.mark.order(6)
def test_signup(page: Page):
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


@pytest.mark.order(7)
def test_login(page: Page):
    home_page = HomePage(page)
    user_page = UserPage(page)
    course01 = os.getenv("product02")
    course02 = os.getenv("product03")
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


@pytest.mark.order(8)
def test_reset_data_user():
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL"))
    admin_username = os.getenv("admin_username")
    admin_password = os.getenv("admin_password")
    course01 = os.getenv("product01")
    course02 = os.getenv("product02")
    course03 = os.getenv("product03")
    course04 = os.getenv("product04")
    admin_token = user_api.login_token(admin_username, admin_password)
    admin_api.set_token(admin_token)
    username = "user83"
    password = "pass83"
    user_token = user_api.login_token(username, password)
    user_api.remove_product_from_user(user_token, course02)
    user_api.remove_product_from_user(user_token, course03)
    admin_api.delete_product_by_name(course01)
    admin_api.delete_product_by_name(course02)
    admin_api.delete_product_by_name(course03)
    admin_api.delete_product_by_name(course04)
