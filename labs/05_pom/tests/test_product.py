from playwright.sync_api import Page, expect
import random
from models.home import HomePage
from models.login import LoginPage
from models.product import ProductPage


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product = ProductPage(page)
    # Given I am an admin user​
    home_page.navigate()
    login_page.login("testuser", "testpassword")
    # When I add a product to the catalog​
    # Then The product is available to be used in the app
    product.create_product("TestProduct" + str(random.randint(1, 1000)))
    product.create_product("TestProduct" + str(random.randint(1, 1000)))



def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product = ProductPage(page)
    home_page.navigate()
    login_page.login("testuser", "testpassword")

    product.delete_product()
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
