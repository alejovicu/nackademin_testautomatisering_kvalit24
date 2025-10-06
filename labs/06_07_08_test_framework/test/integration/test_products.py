from playwright.sync_api import Page
import requests
import os
import libs.utils
from models.api.admin import AdminAPI

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000/")

def test_add_product_product_in_catalog():
    admin_user = AdminAPI(BACKEND_URL)
    login_resp = admin_user.login("admin", "1234")
    assert login_resp.status_code == 200
    token = login_resp.json().get("access_token")

    # Create product
    product_name = libs.utils.generate_string_with_prefix("product")
    create_resp = admin_user.create_product_by_api(product_name)
    assert create_resp.status_code == 200

    
def test_remove_product_in_catalog():
    admin_user = AdminAPI(BACKEND_URL)
    login_resp = admin_user.login("admin", "1234")
    assert login_resp.status_code == 200
    token = login_resp.json().get("access_token")
    
    product_name = libs.utils.generate_string_with_prefix("product")
    create_resp = admin_user.create_product_by_api(product_name)
    assert create_resp.status_code == 200
    
    # Check product exists
    products = requests.get(
        f"{BACKEND_URL}/products",
        headers={"Authorization": f"Bearer {token}"}
    ).json()
    product_names = [p.get("name") for p in products]
    assert product_name in product_names

    # Delete product
    delete_resp = admin_user.delete_product_by_name(product_name)
    assert delete_resp.status_code == 200

    # Check product removed
    products = requests.get(
        f"{BACKEND_URL}/products",
        headers={"Authorization": f"Bearer {token}"}
    ).json()
    product_names = [p.get("name") for p in products]
    assert product_name not in product_names
