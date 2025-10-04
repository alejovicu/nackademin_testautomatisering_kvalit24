from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils
import os


def test_add_product_to_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    before = admin.get_current_product_count()

    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)

    expect(page.locator("div.product-item").filter(has_text=name)).to_be_visible()
    assert admin.get_current_product_count() == before + 1


def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)

    expect(page.locator("div.product-item").filter(has_text=name)).to_be_visible()

    admin.delete_product_by_name(name)

    expect(page.locator("div.product-item").filter(has_text=name)).to_have_count(0)
