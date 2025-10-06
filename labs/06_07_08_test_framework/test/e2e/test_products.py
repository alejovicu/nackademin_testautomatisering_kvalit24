from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils


def test_add_product_to_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")
    page.get_by_text("Product Catalog:", exact=False).wait_for(timeout=7000)

    admin = AdminPage(page)
    before = admin.get_current_product_count()

    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)

    expect(page.locator("div.product-item").filter(has_text=name)).to_be_visible(
        timeout=7000
    )
    assert admin.get_current_product_count() == before + 1


def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)

    expect(page.locator("div.product-item").filter(has_text=name)).to_be_visible(
        timeout=7000
    )

    admin.delete_product_by_name(name)

    expect(page.locator("div.product-item").filter(has_text=name)).to_have_count(
        0, timeout=7000
    )
