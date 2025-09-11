from playwright.sync_api import Page, expect
from models.login import AuthPage
from models.signup import CatalogAdmin


def test_admin_can_add_product(page: Page):
    # Given
    login = AuthPage(page)
    login.open()
    login.login_as_admin("gaffar223", "gaffar_223")

    # When
    admin = CatalogAdmin(page)
    admin.open_catalog()
    admin.create_item("Mango")

    # Then
    expect(page.get_by_text("New product")).to_be_visible()


def test_admin_can_remove_product(page: Page):
    # Given
    login = AuthPage(page)
    login.open()
    login.login_as_admin("gaffar223", "gaffar_223")
    product_name="Mango"

    # When
    admin = CatalogAdmin(page)
    before = admin.total_items()
    admin.remove_item(product_name)

    # Then
    expect(admin.items).to_have_count(before - 1)
    expect(page.get_by_text(product_name)).not_to_be_visible()
