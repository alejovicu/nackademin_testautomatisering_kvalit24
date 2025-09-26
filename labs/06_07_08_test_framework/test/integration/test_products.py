import pytest
import os
from playwright.sync_api import Page
from models.api.admin import AdminAPI
from models.api.user import UserAPI

BASE_URL = os.getenv("BACKEND","http://127.0.0.1:8000")


@pytest.fixture
def admin_api():
    api = AdminAPI(BASE_URL)
    login_response = api.login("admin", "admin1234")
    assert login_response.status_code == 200, f"Admin login failed: {login_response.text}"
    return api

@pytest.fixture
def user_api():
    api = UserAPI(BASE_URL)
    api.signup("testuser", "testpass1234")
    login_response = api.login("testuser", "testpass1234")
    assert login_response.status_code == 200, f"User login failed: {login_response.text}"
    return api


def test_add_product_to_catalog(admin_api: AdminAPI, page: Page):
    product_name = "keyboard"
    response = admin_api.create_product(product_name)
    assert response.status_code == 200, f"Create failed: {response.text}"
    assert response.json().get("name") == product_name


def test_remove_product_from_catalog(admin_api: AdminAPI, page: Page):
    product_name = "test_product_to_delete"
    create_response = admin_api.create_product(product_name)
    assert create_response.status_code == 200, "Failed to create product for deletion"

    delete_response = admin_api.remove_product_by_name(product_name)
    assert delete_response.status_code in [200, 204], f"Delete failed: {delete_response.text}"


def test_add_product_to_user(admin_api: AdminAPI, user_api: UserAPI):
    product_response = admin_api.create_product("test_product_for_user")
    assert product_response.status_code == 200
    product_id = product_response.json().get("id")

    
    response = user_api.add_product_to_user(product_id)
    assert response.status_code == 200, f"Failed to add product: {response.text}"


def test_remove_product_from_user(admin_api: AdminAPI, user_api: UserAPI):
    product_response = admin_api.create_product("test_product_to_remove")
    assert product_response.status_code == 200
    product_id = product_response.json().get("id")

    add_response = user_api.add_product_to_user(product_id)
    assert add_response.status_code == 200, "Failed to add product before removal"

    remove_response = user_api.remove_product_from_user(product_id)
    assert remove_response.status_code in [200, 204], f"Failed to remove product: {remove_response.text}"


def test_get_user_profile(user_api: UserAPI):
    profile_response = user_api.get_profile()
    assert profile_response.status_code == 200
    data = profile_response.json()
    assert "username" in data
    assert data["username"] == "testuser"
