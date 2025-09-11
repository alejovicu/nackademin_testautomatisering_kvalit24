import requests
from models.api.admin import AdminAPI
from libs.utils import generate_string_with_prefix

BASE_URL = "http://localhost:8000"


def _admin_api():
    api = AdminAPI(BASE_URL)
    api.login("admin", "1234")
    return api


def test_add_product_to_catalog():
    api = _admin_api()

    product_name = generate_string_with_prefix("IT_course")

    # Add a product to the catalog
    api.create_product(product_name)

    # The product is available
    products = api.list_products()
    names = list(products)
    assert product_name in names


def test_remove_product_from_catalog():
    api = _admin_api()

    product_name = generate_string_with_prefix("IT_course")

    # Created product name
    api.create_product(product_name)

    # Delete product
    api.delete_product_by_name(product_name)

    # The product is not available
    products = api.list_products()
    names = list(products)
    assert product_name not in names
