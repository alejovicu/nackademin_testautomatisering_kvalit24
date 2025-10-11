from playwright.sync_api import Page
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
import time


def test_add_product_to_catalog(page: Page):
    # PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.navigate()

    login_page.navigate_to_signup()
    signup_page.signup("admin_user", "pass_1234")

    signup_page.navigate_to_login()
    login_page.login_as_admin("admin_user", "pass_1234")

    # As admin user add a product to the catalog
    product_name = f"peach {int(time.time() * 1000)}"
    home_page.add_product(product_name)

    # The added product is available to be used in the app
    home_page.assert_product_visible(product_name)


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Given I am an admin user
    home_page.navigate()
    login_page.login_as_admin()

    # Add product to the catalog
    product_name = f"peach {int(time.time() * 1000)}"
    home_page.add_product(product_name)
    home_page.assert_product_visible(product_name)

    # Remove product from the catalog
    home_page.remove_product(product_name)

    # The product should not be listed in the app
    home_page.assert_product_not_visible(product_name)
