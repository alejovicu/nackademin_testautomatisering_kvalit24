from playwright.sync_api import Page, expect
import pytest

from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os
import time

### RUN 'pytest test_data_admin.py' first to register admin credentials


# Store admin login token
@pytest.fixture(scope="session")
def get_admin_token():
    user_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    credentials = user_api.login("user_admin", "test_1234")
    token = credentials.json().get("access_token")
    return token


# Prepare adding product for removal
@pytest.fixture(scope="session")
def add_product_for_removal(get_admin_token):
    admin_api = AdminAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    product_name = "Bildäck"
    create_product = admin_api.create_product(get_admin_token, product_name)
    product_name = create_product.json().get("name")
    return product_name


#########################################################
# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
##########################################################
def test_add_product_to_catalog(page: Page, get_admin_token):
    ### ARRANGE - Given I am an admin user​
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    product_name = "Cykelstyre"

    # Assign admintoken to browser
    page.add_init_script(
        f"""window.localStorage.setItem("token", "{get_admin_token}")"""
    )
    home_page.navigate()
    # Validate that user has admin privilages by asserting if create product button
    create_product_button = admin_page.button_create_product
    expect(create_product_button).to_be_visible()

    ### ACT - When I add a product to the catalog​
    # Fetch pre-addition stock count
    pre_addition_stock_count = admin_page.product_item_in_list.count()
    # Add product
    admin_page.add_product(product_name)
    # Fetch post-addition stock count
    page.wait_for_load_state("networkidle")
    admin_page.wait_for_product_count_change(pre_addition_stock_count, 1)
    post_addition_stock = admin_page.product_item_in_list.count()

    ### ASSERT - Then The product is available to be used in the app
    # Does product name appear in stock?
    latest_product = admin_page.locate_latest_product_name()
    expect(latest_product).to_have_text(product_name)
    # Has stock count increased by 1?
    assert post_addition_stock == pre_addition_stock_count + 1


#############################################################
# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
##############################################################
def test_remove_product_from_catalog(
    page: Page, get_admin_token, add_product_for_removal
):
    ### ARRANGE - Given I am an admin user​
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    # Fetch added product for removal
    product_name = add_product_for_removal

    # Assign admintoken to browser
    page.add_init_script(
        f"""window.localStorage.setItem("token", "{get_admin_token}")"""
    )
    home_page.navigate()
    ### ACT - When I remove a product from the catalog​
    # Fetch pre-removal stock count
    page.wait_for_load_state("networkidle")
    pre_removal_stock_count = admin_page.product_item_in_list.count()
    # Delete product
    admin_page.delete_latest_product()
    # Fetch post-removal stock count
    page.wait_for_load_state("networkidle")
    admin_page.wait_for_product_count_change(pre_removal_stock_count, -1)
    post_removal_stock_count = admin_page.product_item_in_list.count()

    ### ASSERT - Then The product should not be listed in the app to be used
    # Does the product name no longer appear in stock?
    latest_product = admin_page.locate_latest_product_name()
    expect(latest_product).not_to_contain_text(product_name)
    # Has stock count decreased by 1?
    assert post_removal_stock_count == pre_removal_stock_count - 1
