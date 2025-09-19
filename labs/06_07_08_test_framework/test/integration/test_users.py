from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI


def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI("http://localhost:8000")

    resp = user_api.signup(username, password)
    assert resp.status_code in (200, 201), resp.text

    login = user_api.login(username, password)
    assert login.status_code == 200, login.text


def test_login():
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI("http://localhost:8000")
    resp = user_api.login(username, password)
    assert resp.status_code == 200

    token = login_api_response.json()["token"]
    user_api.set_token(token)

    user_api.login(username, password)
    assert user_api.status_code == 200

    products = user_api.get_user_products()
    assert isinstance(products, list), "Expected products to be a list"
