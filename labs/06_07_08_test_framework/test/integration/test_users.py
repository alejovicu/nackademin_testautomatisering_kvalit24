import libs.utils
import requests
from models.api.user import UserAPI
from models.api.admin import AdminAPI

BASE_URL = "http://127.0.0.1:8000/"

def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = "test1234"

    user_api = UserAPI(BASE_URL)
    signup_response = user_api.signup(username, password)
    assert signup_response.status_code == 200

    login_response = user_api.login(username, password)
    assert login_response.status_code == 200

def test_login():
    username = "admin"
    password = "1234"

    user_api = UserAPI(BASE_URL)
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200

def test_add_product_to_user():
    admin_user = UserAPI(BASE_URL)
    admin_login = admin_user.login("admin", "1234")
    assert admin_login.status_code == 200
    admin_token = admin_login.json().get("access_token")

    admin_api = AdminAPI(BASE_URL, admin_token)
    product_name = libs.utils.generate_string_with_prefix("product")
    create_response = admin_api.create_product_by_api(product_name)
    assert create_response.status_code == 200
    product_id = create_response.json()["id"]

    username_user = "user"
    password_user = "user"
    user_api = UserAPI(BASE_URL)
    login_user = user_api.login(username_user, password_user)
    assert login_user.status_code == 200

    add_product_response = user_api.add_product_to_user(product_id)
    assert add_product_response.status_code == 200

def test_remove_product_from_user():
    admin_user = UserAPI(BASE_URL)
    admin_login = admin_user.login("admin", "1234")
    assert admin_login.status_code == 200
    admin_token = admin_login.json().get("access_token")

    admin_api = AdminAPI(BASE_URL, admin_token)
    product_name = libs.utils.generate_string_with_prefix("product")
    create_response = admin_api.create_product_by_api(product_name)
    assert create_response.status_code == 200
    product_id = create_response.json()["id"]

    username_user = "user"
    password_user = "user"
    user_api = UserAPI(BASE_URL)
    login_user = user_api.login(username_user, password_user)
    assert login_user.status_code == 200

    add_product_response = user_api.add_product_to_user(product_id)
    assert add_product_response.status_code == 200

    remove_response = user_api.remove_product_from_user(product_id)
    assert remove_response.status_code == 200
