import os
import libs.utils
from models.api.user import UserAPI
import pytest

BACKEND_URL = os.getenv("APP_BACK_URL", "http://localhost:8000")

def test_signup():
    
    # GIVEN I AM A NEW POTENTIAL CUSTOMER
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI(BACKEND_URL)

    # WHEN I SIGNUP IN THE APP
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # THEN I SHOULD BE ABLE TO LOG IN WITH MY NEW USER
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    login_data = login_api_response.json()
    assert "access_token" in login_data, "API response did not include a token"
    assert login_data["access_token"], "Access token is empty"


def test_login():

    # GIVEN I AM AN AUTHENTICATHED USER
    # (Assumes this user already exists in the DB)
    username = "user_1"
    password = "pass_1"

    user_api = UserAPI(BACKEND_URL)

    # WHEN I LOG INTO THE APPLICATION
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200
    assert user_api.token is not None, "No token stored after login"

    # THEN I SHOULD SEE ALL MY PRODUCTS
    products_response = user_api.get_user_products()
    assert products_response.status_code == 200
    assert "products" in products_response.json(), "Products key not found in response"
