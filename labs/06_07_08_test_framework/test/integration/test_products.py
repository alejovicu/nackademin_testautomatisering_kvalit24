from playwright.sync_api import Page, expect
from models.api.admin import AdminAPI
import os

BACKEND_URL = os.environ.get("BACKEND_URL","http://127.0.0.1:8000")
admin_page = AdminAPI(BACKEND_URL)
product_name = "Pasta"
username = "admin"
password = "test123" 

def test_add_product_to_catalog():

    admin_page.admin_login(username, password)

    initial_count = admin_page.get_current_product_count()

    admin_page.create_product_by_api(product_name)

    updated_count = admin_page.get_current_product_count()
    assert updated_count == initial_count + 1

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

def test_remove_product_from_catalog():
    product_name = 2
    username = "admin"
    password = "test123" 
    admin_page = AdminAPI("http://127.0.0.1:8000")

    
    admin_page.admin_login(username, password)
    
    initial_count = admin_page.get_current_product_count()

    admin_page.delete_product_by_id(product_name)
    updated_count = admin_page.get_current_product_count()

    assert updated_count == initial_count - 1, (f"Expected {initial_count - 1} products, but got {updated_count}")
