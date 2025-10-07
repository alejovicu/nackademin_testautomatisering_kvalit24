import pytest
from playwright.sync_api import Page
from models.api.admin import AdminAPI
from models.api.user import UserAPI
import os

BASE_URL = os.getenv("BACKEND_URL","http://localhost:8000/")


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
    product_name = "keyboard"
    delete_response = admin_api.remove_product_by_name(product_name)
    assert delete_response.status_code in [200, 204], f"Delete failed: {delete_response.text}"


