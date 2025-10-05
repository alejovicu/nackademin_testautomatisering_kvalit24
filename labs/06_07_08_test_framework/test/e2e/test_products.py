from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage

USERNAME = "test_admin"
PASSWORD = "admin_test321"

def test_add_product_to_catalog(page: Page):
    # Given I am an admin user​
    login_page = HomePage(page)
    login_page.navigate()

    login_page.login(USERNAME, PASSWORD)
    expect(login_page.login_header_main_title).to_be_visible()
    expect(page.get_by_text("Logout")).to_be_visible()

    # When I add a product to the catalog​
    product_name = "Banana"
    admin_page = AdminPage(page)

    admin_page.create_product(product_name)
    expect(page.get_by_text(product_name)).to_be_visible()


def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    login_page = HomePage(page)
    login_page.navigate()

    login_page.login(USERNAME, PASSWORD)
    expect(login_page.login_header_main_title).to_be_visible()
    expect(page.get_by_text("Logout")).to_be_visible()

    # When I remove a product from the catalog​
    product_name = "Banana"
    admin_page = AdminPage(page)

    admin_page.delete_product_by_name(product_name)
    expect(page.get_by_text(product_name)).not_to_be_visible()