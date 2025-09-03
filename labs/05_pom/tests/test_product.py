from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.product import ProductPage


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    product = "Kaffemugg"

    home_page.navigate()
    login_page.login(username="admin", password="1234")
    product_page.add_product(name=product)

    # Making sure the product is available in the app
    assert product_page.check_product(product).inner_text() == product

    # Removing product again just to make test repeatable
    product_page.delete_product(name=product)
    assert product_page.check_product(product).count() == 0

    # Given I am an admin user​
    # When I add a product to the catalog​
    # Then The product is available to be used in the app


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    product = "Vattenpistol"

    home_page.navigate()
    login_page.login(username="admin", password="1234")

    # Adding a product before to make test repeatable
    product_page.add_product(name=product)

    assert product_page.check_product(product).inner_text() == product

    product_page.delete_product(name=product)
    assert product_page.check_product(product).count() == 0

    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
