from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app


def test_add_product_to_catalog(page: Page):
    # Given I am an admin user
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    before = admin.get_current_product_count()

    # When I add a product to the catalog
    name = libs.utils.generate_string_with_prefix("apple", 4)
    admin.create_product(name)

    # Then The product is available to be used in the app

    assert admin.get_current_product_count() == before + 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used


def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    name = libs.utils.generate_string_with_prefix("apple", 4)
    admin.create_product(name)
    assert page.get_by_txt(name).count() > 0

    admin.delete_product_by_name(name)
    page.wait_for_load_state("networkidle")

    assert admin.get_by_text(name).count() == 0


# jag har skrivit admin_page iställlet för page. >> kolla igenom
