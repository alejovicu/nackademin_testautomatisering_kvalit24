from libs.utils import generate_product_string_with_prefix
import requests
import os
from models.api.admin import AdminAPI

BASE_URL_BACKEND = os.getenv("BASE_URL_BACKEND", "http://localhost:8000")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin_user")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "pass_1234")


def _admin_api():
    api = AdminAPI(BASE_URL_BACKEND)
    api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    return api


# Given I am an admin user​
def test_add_product_to_catalog():
    api = _admin_api()

    product_name = generate_product_string_with_prefix("peach", 8)

    # When I Add a product to the catalog
    api.create_product(product_name)

    # Then The product is available
    products = api.list_products()
    names = list(products)
    assert product_name in names


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    api = _admin_api()

    product_name = generate_product_string_with_prefix("peach", 8)

    # Created product name
    api.create_product(product_name)

    # Delete product
    api.delete_product_by_name(product_name)

    # The product is not available
    products = api.list_products()
    names = list(products)
    assert product_name not in names
