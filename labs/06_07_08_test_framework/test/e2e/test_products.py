from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage

USERNAME = "admin"
PASSWORD = "1234"


def test_add_product_to_catalog(page: Page):
    product = "Chips"

    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login(USERNAME, PASSWORD)
    
    # Vänta på att admin-element laddas efter login
    expect(admin_page.input_product_name).to_be_visible()
    
    admin_page.create_product_by_api(product)
    expect(admin_page.admin_products.filter(has_text=product)).to_have_count(1)


def test_remove_product_from_catalog(page: Page):
    product = "Chips"

    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login(USERNAME, PASSWORD)
    
    # Vänta på att produktlistan laddas efter login
    expect(admin_page.admin_products.first).to_be_visible()
    
    admin_page.delete_product_by_name_by_api(product)
    expect(admin_page.admin_products.filter(has_text=product)).to_have_count(0)