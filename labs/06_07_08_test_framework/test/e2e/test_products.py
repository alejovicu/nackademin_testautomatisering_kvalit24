from playwright.sync_api import Page
from models.ui.admin import AdminPage
from models.api.admin import AdminAPI
import libs.utils
import pytest
import os

API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")

@pytest.fixture
def admin_token():
    admin_api = AdminAPI(API_URL, token=None)
    response = admin_api.login("admin", "admin123")
    token = response.json()["access_token"]
    return token

@pytest.fixture
def auth_page(page: Page, admin_token):
    page.add_init_script(f"window.localStorage.setItem('token', '{admin_token}');")

    return page

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(auth_page: Page):
    page = auth_page
    admin_ui = AdminPage(page)

    page.goto(FRONTEND_URL)


    product_name = libs.utils.generate_string_with_prefix("product")
    admin_ui.create_product(product_name)
    page.wait_for_selector(f"text={product_name}")

    assert admin_ui.product_exists(product_name)



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(auth_page: Page):
    page = auth_page
    admin_ui = AdminPage(page)

    page.goto(FRONTEND_URL)

    product_name = libs.utils.generate_string_with_prefix("product")
    admin_ui.create_product(product_name)
    page.wait_for_selector(f"text={product_name}")
    assert admin_ui.product_exists(product_name)

    admin_ui.delete_product_by_name(product_name)
    page.wait_for_selector(f"text={product_name}", state="detached")

    assert not admin_ui.product_exists(product_name)