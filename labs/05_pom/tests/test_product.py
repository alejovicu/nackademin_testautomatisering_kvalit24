from playwright.sync_api import Page, expect
from models.home import HomePage
from models.login import LoginPage
from models.product_page import ProductPage


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    
    home_page.navigate()
    login_page.login("admin", "admin1234")

    product_page.add_product("Apple")

    
    assert page.get_by_text("Apple").count() > 0


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    
    home_page.navigate()
    login_page.login("admin", "admin1234")

    
    before_count = page.locator(".product-item").count()

    
    product_page.remove_last_product()

    
    after_count = page.locator(".product-item").count()
    assert after_count == before_count - 1
