from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils


def test_add_product_to_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    before = admin.get_current_product_count()

    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)

    assert page.get_by_text(name).count() > 0
    assert admin.get_current_product_count() == before + 1


def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)
    assert page.get_by_text(name).count() > 0

    admin.delete_product_by_name(name)

    assert page.get_by_text(name).count() == 0
