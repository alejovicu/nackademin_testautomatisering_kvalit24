from playwright.sync_api import Page, expect
from models.login import LoginPage
from libs import utils
from models.home import HomePage
from models.product import ProductPage

def test_user_can_see_products(page: Page):

    # PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    home_page.navigate()
    login_page.login("test", "test123")

    expect(page.get_by_text("Test Product")).to_be_visible()
    expect(page.get_by_text("Add Product")).to_be_visible()
    expect(page.get_by_text("Sample Product 1")).to_be_visible()
    expect(page.get_by_text("Sample Product 2")).to_be_visible()


def test_user_cannot_see_admin_buttons(page: Page):
    # PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    home_page.navigate()
    login_page.login("test", "test123")

    expect(page.locator("#add-product")).not_to_be_visible()
    expect(page.locator(".delete-product")).not_to_be_visible()