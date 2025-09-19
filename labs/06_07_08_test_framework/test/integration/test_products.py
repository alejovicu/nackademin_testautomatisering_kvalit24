from libs.utils import generate_product_string_with_prefix
from models.api.admin import AdminAPI
import requests
import os


BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1234")


def _admin_api():
    api = AdminAPI(BASE_URL)
    api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    return api


def test_add_product_to_catalog():
    api = _admin_api()

    product_name = generate_product_string_with_prefix("banana", 4)

    api.create_product(product_name)

    products = api.list_products()
    names = list(products)
    assert product_name in names


def test_remove_product_from_catalog():
    api = _admin_api()
    product_name = generate_product_string_with_prefix("banana", 4)

    api.create_product(product_name)

    api.delete_product_by_name(product_name)

    products = api.list_products()
    names = list(products)
    assert product_name not in names
