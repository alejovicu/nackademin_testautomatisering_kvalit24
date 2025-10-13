from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os, time
from config import BACKEND_URL

def test_signup():
    user_api = UserAPI(BACKEND_URL)
    username = f"user_{int(time.time())}"
    password = "pass123"

    # signup + login
    user_api.session.post(f"{BACKEND_URL}/signup", json={"username": username, "password": password})
    token = user_api.login(username, password)
    assert token and isinstance(token, str)

def test_login():
    user_api = UserAPI(BACKEND_URL)
    username, password = "admin", "admin123"
    user_api.session.post(f"{BACKEND_URL}/signup", json={"username": username, "password": password})
    token = user_api.login(username, password)

    admin_api = AdminAPI(BACKEND_URL, token=token)
    products = admin_api.get_product_list()
    count = admin_api.get_current_product_count()
    assert isinstance(products, list)
    assert count == len(products)