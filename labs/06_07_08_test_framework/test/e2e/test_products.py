import pytest
from playwright.sync_api import Page
from models.ui.admin import AdminPage
from models.ui.home import HomePage
# Given I am an admin user
# When I add a product to the catalog
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    admin_page = AdminPage(page)

    
    home_page.navigate()
    home_page.login("admin", "admin1234")

    initial_count = admin_page.get_current_product_count()

    
    product_name = "keyboard"
    admin_page.create_product(product_name)

    assert admin_page.admin_products.filter(has_text=product_name).count() == 1
    assert admin_page.get_current_product_count() == initial_count + 1    


def test_remove_existing_product(page: Page):
    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login("admin", "admin1234")

    product_name = "keyboard"  
    assert admin_page.admin_products.filter(has_text=product_name).count() > 0

    admin_page.delete_product_by_name(product_name)

    assert admin_page.admin_products.filter(has_text=product_name).count() == 0
