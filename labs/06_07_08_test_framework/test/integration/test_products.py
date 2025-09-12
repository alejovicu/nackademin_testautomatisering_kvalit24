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

    # Add product
    add_product_resp = user_api.add_product_to_user(product, token)
    assert add_product_resp.status_code == 200
    response_json = add_product_resp.json()
    assert response_json.get("name") == product
    
    # get products
    products_resp = user_api.get_products(token)
    assert products_resp.status_code == 200

    # count amount of products, as the delete product requires an ID , not name
    admin_api = AdminAPI(BASE_URL, token)
    delete_resp = admin_api.delete_product_by_name(product)
    assert delete_resp.status_code == 200
    