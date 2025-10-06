#import libs.utils
#import pytest


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
#def test_add_product_to_catalog():
    # complete code
    #pass


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
#def test_remove_product_from_catalog():
    # complete code
    #pass


# tests/integration/test_products.py

import pytest
from models.api.products import ProductAPI
from models.api.admin import AdminAPI
import os
import libs.utils

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

@pytest.mark.usefixtures("admin_token")
def test_create_product(admin_token):
    product_api = AdminAPI (base_url=BACKEND_URL, token=admin_token)
    random_product=libs.utils.generate_string_with_prefix("product")
    response = product_api.create_product(random_product)
    assert response["name"] == random_product

@pytest.mark.usefixtures("admin_token")
def test_get_current_product_count(admin_token):
    product_api = ProductAPI(BACKEND_URL, token=admin_token)
    products = product_api.list_products()
    assert isinstance(products, list)


@pytest.mark.usefixtures("admin_token")
def test_delete_product_by_name(admin_token):
    product_api = ProductAPI(BACKEND_URL, token=admin_token)
    products = product_api.list_products()
    if products:
        product_api.delete_product(products[0]["id"])