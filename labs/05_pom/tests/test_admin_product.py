from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.product import ProductPage
from libs import utils

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

def test_add_product_to_catalog(page: Page):

    #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    home_page.navigate()
    login_page.login("admin", "admin123")

    product_name = f"Product {utils.generate_username()}"
    product_page.add_product(product_name)


    expect(page.locator(f"text={product_name}")).to_be_visible()


    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used

def test_remove_product_from_catalog(page: Page):

    #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    home_page.navigate()
    login_page.login("admin", "admin123")

    product_name = f"Product {utils.generate_username()}"
    product_page.add_product(product_name)

    product_page.delete_product(product_name)

    expect(page.locator(f"text={product_name}")).not_to_be_visible()
    