import time
from playwright.sync_api import Page
from models.home import HomePage
from models.login import LoginPage


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Login as admin
    home_page.navigate()
    login_page.login_as_admin()

    # Add a product to the catalog
    product_name = f"IT course {int(time.time() * 1000)}"
    home_page.add_product(product_name)

    # Product is available in the app
    home_page.assert_product_visible(product_name)


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Login as admin
    home_page.navigate()
    login_page.login_as_admin()

    # Add a product to the catalog
    product_name = f"IT course {int(time.time() * 1000)}"
    home_page.add_product(product_name)
    home_page.assert_product_visible(product_name)

    # Remove product from the catalog
    home_page.remove_product(product_name)

    # Product is not visible in the app
    home_page.assert_product_not_visible(product_name)
