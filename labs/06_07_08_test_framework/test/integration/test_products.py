from config import BACKEND_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from libs.utils import generate_product_string_with_prefix
from models.api.admin import AdminAPI
from models.api.user import UserAPI
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def _admin_api():
    api = AdminAPI(BACKEND_URL)
    api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    return api


def test_add_product_to_catalog():
    
    api = _admin_api()

    product_name = generate_product_string_with_prefix()

    api.create_product(product_name)

    products = api.list_products()
    names = list(products)
    assert product_name in names


def test_remove_product_from_catalog():
    api = _admin_api()
    product_name = generate_product_string_with_prefix()

    api.create_product(product_name)

    products = api.list_products()
    print('LIST BEFORE')
    print(products)

    api.delete_product_by_name(product_name)

    products = api.list_products()
    print('LIST AFTER')
    print(products)
    names = list(products)
    assert product_name not in names
