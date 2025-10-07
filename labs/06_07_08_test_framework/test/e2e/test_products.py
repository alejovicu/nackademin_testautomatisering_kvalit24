import pytest
from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from libs.utils import generate_string_with_prefix

import os
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page:Page):
    # complete code
    username = "admin"
    password = "pass123"
    product = "bord"

    home_page = HomePage(page)
    admin_page = AdminPage(page)


    home_page.navigate()
    home_page.login(username, password)
    if not admin_page.products.first.is_visible():
        num_of_products_before = admin_page.get_current_product_count()
        admin_page.create_product(product)
        expect(admin_page.products).to_have_count(num_of_products_before + 1)
    
    else:
        expect(admin_page.products.first).to_be_visible()

    
    
    page.wait_for_timeout(2000)
    


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    # complete code
    username = "admin"
    password = "pass123"
    product = "bord"

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI(BACKEND_URL)
    response = user_api.login(username, password)
    token = response.json().get("access_token")

      # Setting token through local storage to avoid logging in through the UI every time
    page.add_init_script(
        f"""
    window.localStorage.setItem("token", "{token}");
    """
    )

    home_page.navigate()
    expect(admin_page.products.first).to_be_visible()
        
    num_of_products_before = admin_page.get_current_product_count()
    
    admin_page.delete_product_by_name(product)
   
    expect(admin_page.products).to_have_count(num_of_products_before - 1)

    page.wait_for_timeout(2000)