from playwright.sync_api import Page
import libs.utils
import sqlite3
import pytest
import uuid
from models.api.user import UserAPI
from models.api.admin import AdminAPI

BASE_URL = 'http://localhost:8000'


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    # complete code
    username = "admin"
    password = "pass1234"
    product = f"test_course_{uuid.uuid4()}"

    user_api = UserAPI(BASE_URL)

    # Login
    login_resp = user_api.login(username, password)
    assert login_resp.status_code == 200

    token = login_resp.json().get("access_token")
    assert token is not None

    add_product_resp = user_api.add_product_to_user(product, token)
    assert add_product_resp.status_code == 200
    
    response_json = add_product_resp.json()
    assert response_json.get("name") == product



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
### Note !! this removes by ID and just the recently added.
def test_remove_product_from_catalog():
    username = "admin"
    password = "pass1234"
    product = f"test_course_{uuid.uuid4()}"

    user_api = UserAPI(BASE_URL)
    # Login
    login_resp = user_api.login(username, password)
    assert login_resp.status_code == 200

    token = login_resp.json().get("access_token")
    assert token is not None

    admin_api = AdminAPI(BASE_URL, token)

    # this adds product 
    add_product_resp = admin_api.create_product(product)
    assert add_product_resp.status_code == 200
    response_json = add_product_resp.json()
    assert response_json.get("name") == product

    # this delete product
    delete_resp = admin_api.delete_product_by_name(product)
    assert delete_resp.status_code == 200

    # this verify product no longer exists
    products = admin_api.get_products()
    assert product not in [p["name"] for p in products]