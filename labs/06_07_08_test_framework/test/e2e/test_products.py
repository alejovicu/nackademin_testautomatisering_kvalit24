import pytest
import os
from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.base import BaseAPI
# complete imports

BASE_URL = os.getenv("APP_URL", "http://127.0.0.1:8000")


@pytest.fixture
def admin_page(page: Page):
    
    base_api = BaseAPI(BASE_URL)
    base_api.login("admin", "admin")
    page.add_init_script(
        f"window.localStorage.setItem('token', '{base_api.token}');")
    
    print("Token injected:", base_api.token)
    print("Token in page:", page.evaluate("localStorage.getItem('token')"))
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    home_page.navigate()
    # home_page.admin_login()

    return admin_page

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(admin_page):

    product_to_create = "Apa"

    
    print("\n=== DEBUG HTML START ===")
    print(admin_page.page.content())
    print("=== DEBUG HTML END ===\n")
    

    expect(admin_page.admin_products.first).to_be_visible()
    # Check how many products are in the product list
    num_of_products_before = admin_page.get_current_product_count()
    # Add product
    admin_page.create_product(product_to_create)


    print("\n=== DEBUG HTML START ===")
    print(admin_page.page.content())
    print("=== DEBUG HTML END ===\n")

    # Product has been added (list of products has gotten longer)
    expect(admin_page.admin_products).to_have_count(num_of_products_before + 1)

# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(admin_page):
    
    product_to_delete = "Apa"

    expect(admin_page.admin_products.first).to_be_visible()
    # Check how many products are in the product list
    num_of_products_before = admin_page.get_current_product_count()
    # Remove product the last product in the list
    admin_page.delete_product_by_name(product_to_delete)
    # Product has been removed (list of products has gotten shorter)
    expect(admin_page.admin_products).to_have_count(num_of_products_before - 1)