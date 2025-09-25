from playwright.sync_api import Page
import requests
import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI

import os

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
user_api = UserAPI(BASE_URL)


def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI(BASE_URL)

    # When I signup in the app​
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200


def test_login():
    # Given I am an authenticated user
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI("http://localhost:8000")

    # When I log in into the app​
    user_api.signup(username, password)
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200
    token = login_api_response.json().get("access_token")
    user_api.token = token

    # Create a product as admin
    admin_api = AdminAPI("http://localhost:8000")
    admin_api.login("admin", "1234")
    product_name = libs.utils.generate_string_with_prefix("IT_course")
    admin_api.create_product(product_name)

    # Add product to user
    add_respponse = user_api.add_product_to_user(product_name)
    assert add_respponse is not None
    assert add_respponse.status_code in (200, 201)

    # Then I should see all my products
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get("http://localhost:8000/user", headers=headers)
    assert r.status_code == 200
    data = r.json()
    products = data.get("products", [])
