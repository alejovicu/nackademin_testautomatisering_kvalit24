from playwright.sync_api import Page
import time
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.navigate()

    # create new user
    login_page.navigate_to_signup()
    username = f"user_{int(time.time())}"
    password = "pass1234"
    signup_page.signup(username, password)
    signup_page.navigate_to_login()

    # login
    login_page.login_as_admin(username, password)

    # add product
    product_name = f"Apple_{int(time.time())}"
    home_page.add_product(product_name)

    # assert product is visible
    home_page.assert_product_visible(product_name)

    # logout + close
    home_page.logout()
    page.close()


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.navigate()

    # create new user
    login_page.navigate_to_signup()
    username = f"user_{int(time.time())}"
    password = "pass1234"
    signup_page.signup(username, password)
    signup_page.navigate_to_login()

    # login
    login_page.login_as_admin(username, password)

    # add product
    product_name = f"Banana_{int(time.time())}"
    home_page.add_product(product_name)
    home_page.assert_product_visible(product_name)

    # remove product
    home_page.remove_product(product_name)
    home_page.assert_product_not_visible(product_name)

    # logout + close
    home_page.logout()
    page.close()
