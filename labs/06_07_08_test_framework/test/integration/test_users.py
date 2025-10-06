from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI(VITE_BACKEND_URL)

    user_api.signup(username, password)
    assert user_api.status_code == 200

    user_api.login(username, password)
    assert user_api.status_code == 200


def test_login():
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI(VITE_BACKEND_URL)
    user_api.signup(username, password)
    assert user_api.status_code == 200

    user_api.login(username, password)
    assert user_api.status_code == 200

    products = user_api.get_user_products()
    assert isinstance(products, list), "Expected products to be a list"
