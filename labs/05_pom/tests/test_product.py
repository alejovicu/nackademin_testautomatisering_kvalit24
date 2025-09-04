import time
from playwright.sync_api import Page
from models.home import HomePage
from models.login import LoginPage

USER = "DB_admin"
PASS = "admin123"


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Given I am an admin user
    login_page.navigate()
    login_page.login(USER, PASS)
    login_page.expect_logged_in_as(USER)

    # When I add a product to the catalog
    product_name = f"Playwright Item {int(time.time())}"
    home_page.navigate()
    home_page.add_product(product_name)

    # Then the product is available to be used in the app
    home_page.expect_product_listed(product_name)


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Given I am an admin user
    login_page.navigate()
    login_page.login(USER, PASS)
    login_page.expect_logged_in_as(USER)

    # First add a product to remove
    product_name = f"Playwright Item {int(time.time())}"
    home_page.navigate()
    home_page.add_product(product_name)
    home_page.expect_product_listed(product_name)

    # When I remove a product from the catalog
    home_page.remove_product(product_name)

    # Then the product should not be listed in the app
    home_page.expect_product_not_listed(product_name)
