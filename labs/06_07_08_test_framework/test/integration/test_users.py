import libs.utils
import os
from models.api.user import UserAPI
from models.api.admin import AdminAPI

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000/")

def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = "test1234"

    user_api = UserAPI(BACKEND_URL)
    signup_resp = user_api.signup(username, password)
    assert signup_resp.status_code == 200

    login_resp = user_api.login(username, password)
    assert login_resp.status_code == 200

def test_login():
    username = "user"  # Use existing user from your system
    password = "1234"

    user_api = UserAPI(BACKEND_URL)
    login_resp = user_api.login(username, password)
    assert login_resp.status_code == 200

def test_add_product_to_user():
    # Assume product already exists (created by admin in test_admin.py)
    # For testing purposes, we'll use a known product_id or create one via fixture
    product_id = 1  # Or get from a fixture/setup
    
    # Regular user logs in
    user_api = UserAPI(BACKEND_URL)
    login_resp = user_api.login("user", "1234")
    assert login_resp.status_code == 200

    # User adds product to themselves
    add_resp = user_api.add_product_to_user(product_id)
    assert add_resp.status_code == 200

def test_remove_product_from_user():
    # Assume product already exists
    product_id = 1  # Or get from a fixture/setup
    
    # Regular user logs in
    user_api = UserAPI(BACKEND_URL)
    login_resp = user_api.login("user", "1234")
    assert login_resp.status_code == 200

    # User adds product to themselves
    add_resp = user_api.add_product_to_user(product_id)
    assert add_resp.status_code == 200
    
    # User removes product from themselves
    remove_resp = user_api.remove_product_from_user(product_id)
    assert remove_resp.status_code == 200