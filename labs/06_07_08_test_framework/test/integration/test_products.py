import libs.utils
import pytest
from models.api.admin import AdminAPI
from models.api.user import UserAPI
from playwright.sync_api import Page
import libs.utils

API_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:5173"


@pytest.fixture
def user_api():
    return UserAPI(API_URL)

@pytest.fixture
def admin_api():
    username = "admin"
    password = "admin123"

    user_api = UserAPI(API_URL)
    login_response = user_api.login(username, password)

    if login_response.status_code == 404:  # user not found
        signup_response = user_api.signup(username, password)
        assert signup_response.status_code == 200
        login_response = user_api.login(username, password)

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    assert token
    return AdminAPI(API_URL, token=token)


def test_login_existing_user(page: Page, user_api, admin_api):
    username = "test"
    password = "test123"

    product_name = libs.utils.generate_string_with_prefix("product")
    product = admin_api.create_product(product_name)

    user_api.login(username, password)
    user_api.add_product_to_user(product["id"])

    page.goto(FRONTEND_URL)
    page.locator("text=login").click()
    page.locator("input[placeholder='Username']").fill(username)
    page.locator("input[placeholder='Password']").fill(password)
    page.locator("button:has-text('Login')").click()

    page.wait_for_selector(f"text=Welcome, {username}!")
    assert page.locator(f"text=Welcome, {username}!").is_visible()

    page.wait_for_selector("text=Your Products:")
    product_elements = page.locator("text=Your Products: >> xpath=following-sibling::div/div")
    assert product_elements.count() > 0


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

def test_add_product_to_catalog(admin_api):
    product_name = libs.utils.generate_string_with_prefix("product")
    response = admin_api.create_product(product_name)

    assert response["name"] == product_name
    


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(admin_api):
    product_name = libs.utils.generate_string_with_prefix("product")
    product = admin_api.create_product(product_name)
    print("Created Product:", product)

    delete_status = admin_api.delete_product_by_id(product["id"])
    assert delete_status