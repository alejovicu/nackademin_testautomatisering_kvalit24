from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.admin import AdminPage



def test_add_product_to_catalog(page: Page):
    # Given I am an admin user​
    # When I add a product to the catalog​
    # Then The product is available to be used in the app

    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    product = "Apa"

    home_page.navigate()
    login_page.admin_login()
    # Check how many products are in the product list
    num_of_products_before = admin_page.count_products()
    # Add product
    admin_page.create_product(product)
    # Product has been added (list of products has gotten longer)
    expect(admin_page.products).to_have_count(num_of_products_before + 1)


def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used

    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    login_page.admin_login()
    # Check how many products are in the product list
    num_of_products_before = admin_page.count_products()
    # Remove product the last product in the list
    admin_page.remove_last_product()
    # Product has been removed (list of products has gotten shorter)
    expect(admin_page.products).to_have_count(num_of_products_before - 1)
