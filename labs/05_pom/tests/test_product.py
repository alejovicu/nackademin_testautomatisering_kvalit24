from playwright.sync_api import Page, expect
from models.add_product import ProductPage
from models.home import HomePage
from models.login import LoginPage


# def test_add_product_to_catalog(page: Page):
#     home_page = HomePage(page)
#     login_page = LoginPage(page)
#     home_page.navigate()
#     login_page.navigate_to_signup()


# Given I am an admin user​
def test_validate_login(page: Page):
    username = "admin"
    password = "admin"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.admin_login(username, password)
    add_product = ProductPage(page)
    add_product.logout()


# def test_create_product(page: Page):
#     username = "admin"
#     password = "admin"
#     po_login = LoginPage(page)
#     po_login.navigate()
#     po_login.admin_login(username, password)
#     product = "apple"
#     add_product = ProductPage(page)
#     add_product.create_product(product)
#     add_product.logout()


# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_validate_product_in_list(page: Page):
    username = "admin"
    password = "admin"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.admin_login(username, password)
    product = "canon"
    add_product = ProductPage(page)
    add_product.create_product(product)

    expect(add_product.product_lists).to_contain_text(product)

    add_product.logout()


# def test_remove_product_from_catalog(page: Page):
#     # Given I am an admin user​
#     # When I remove a product from the catalog​
#     # Then The product should not be listed in the app to be used
#     pass


# Then The product should not be listed in the app to be used
def test_remove_product(page: Page):
    username = "admin"
    password = "admin"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.admin_login(username, password)
    add_product = ProductPage(page)
    add_product.remove_product()
    expect(add_product.empty_product_message).not_to_be_visible()
