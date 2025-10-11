from playwright.sync_api import Page
from models.login import LoginPage
from models.add_product import ProductPage


def test_validate_login(page: Page):
    username = "admin"
    password = "admin"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.admin_login(username, password)
    add_product = ProductPage(page)
    add_product.logout()


def test_create_product(page: Page):
    username = "admin"
    password = "admin"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.admin_login(username, password)
    product = "apple"
    add_product = ProductPage(page)
    add_product.create_product(product)
    add_product.logout()


def test_validate_product_in_list(page: Page):
    username = "admin"
    password = "admin"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.admin_login(username, password)
    product = "skit"
    add_product = ProductPage(page)
    add_product.create_product(product)
    add_product.validate_product_in_list(product)
