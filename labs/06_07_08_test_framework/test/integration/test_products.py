import pytest
import requests
import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI

BASE_URL = "http://127.0.0.1:8000/"

def test_add_product_to_catalog():
    admin_user = UserAPI(BASE_URL)
    login_response = admin_user.login("admin", "1234")
    assert login_response.status_code == 200

    token = login_response.json().get("access_token")
    admin_user.token = token
    admin_api = AdminAPI(BASE_URL, admin_user.token)

    product_name = libs.utils.generate_string_with_prefix("product")
    response = admin_api.create_product_by_api(product_name)
    assert response.status_code == 200
    assert response.json().get("name") == product_name

    products = requests.get(
        f"{BASE_URL}/products",
        headers={"Authorization": f"Bearer {token}"}
    ).json()

    product_names = [p.get("name") for p in products]
    assert product_name in product_names

def test_remove_product_from_catalog():
    admin_user = UserAPI(BASE_URL)
    login_response = admin_user.login("admin", "1234")
    assert login_response.status_code == 200

    token = login_response.json().get("access_token")
    admin_user.token = token
    admin_api = AdminAPI(BASE_URL, admin_user.token)

    product_name = libs.utils.generate_string_with_prefix("product")
    create_response = admin_api.create_product_by_api(product_name)
    assert create_response.status_code == 200

    delete_response = admin_api.delete_product_by_name(product_name)
    assert delete_response is not None
    assert delete_response.status_code == 200

    products = requests.get(
        f"{BASE_URL}/products",
        headers={"Authorization": f"Bearer {token}"}
    ).json()
    product_names = [p.get("name") for p in products]
    assert product_name not in product_names
