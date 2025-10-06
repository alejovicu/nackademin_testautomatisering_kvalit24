import os
from libs.utils import generate_product_string_with_prefix
from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from config import BACKEND_URL, ADMIN_USERNAME, ADMIN_PASSWORD


# Given I am an admin user
# When I add a product to the catalog
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    username = ADMIN_USERNAME
    password = ADMIN_PASSWORD

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI(BACKEND_URL)
    product = generate_product_string_with_prefix("mango", 8)

    # Get token from the API and verify that login is successful
    response = user_api.login(username, password)
    assert response.status_code == 200, f"Admin login failed: {response.text}"
    token = user_api.token

    # Inject the token into localStorage before loading the page
    page.add_init_script(f"""
    window.localStorage.setItem("token", "{token}");
""")

    # Navigate directly to the home page
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # Create a new product using the AdminPage
    admin_page.create_product(product_name=product)
    page.wait_for_load_state("networkidle")

    # Go to the listing page (home) and verify
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    product_locator = admin_page.find_product(product)
    expect(product_locator).to_have_count(1, timeout=5000)
    expect(product_locator.first).to_contain_text(product)


# Given I am an admin user
# When I remove a product from the catalog
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    username = ADMIN_USERNAME
    password = ADMIN_PASSWORD

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI(BACKEND_URL)
    product = generate_product_string_with_prefix("mango", 8)

    # Get token from the API and verify that login is successful
    response = user_api.login(username, password)
    assert response.status_code == 200, f"Admin login failed: {response.text}"
    token = user_api.token

    # Inject the token into localStorage before loading the page
    page.add_init_script(f"""
    window.localStorage.setItem("token", "{token}");
""")

    # Navigate to the home page
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # Add the product (to make the test repeatable)
    admin_page.create_product(product_name=product)
    page.wait_for_load_state("networkidle")

    # Wait until the product name appears visibly
    page.get_by_text(product).wait_for(state="visible")

    # Delete and verify the product is hidden
    admin_page.delete_product_by_name(product_name=product)
    expect(admin_page.find_product(product)).to_be_hidden()
