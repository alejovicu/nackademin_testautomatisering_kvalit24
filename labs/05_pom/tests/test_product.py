from playwright.sync_api import Page

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
import time


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.navigate()

    login_page.navigate_to_signup()
    signup_page.signup("monica", "pass_monica")
    signup_page.navigate_to_login()
    login_page.login_as_admin("monica", "pass_monica")

    product_name = f"Apple {int(time.time() * 1000)}"
    home_page.add_product(product_name)

    home_page.assert_product_visible(product_name)


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate()
    login_page.login_as_admin()

    product_name = f"Apple {int(time.time() * 1000)}"
    home_page.add_product(product_name)
    home_page.assert_product_visible(product_name)

    home_page.remove_product(product_name)

    home_page.assert_product_not_visible(product_name)
