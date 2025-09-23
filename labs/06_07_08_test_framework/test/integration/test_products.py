import os
import pytest
from models.api.admin import AdminAPI
import time

BACKEND_URL = os.getenv("APP_BACK_URL", "http://localhost:8000")

def test_add_product_to_catalog():

    # GIVEN I AM AN ADMIN USER
    admin_api = AdminAPI(BACKEND_URL)
    admin_api.get_admin_token() # token is stored in the admin-api instance

    # WHEN I ADD A PRODUCT TO THE CATALOGUE
    product_name = f"product_{int(time.time())}"
    count_before = admin_api.get_current_product_count()
    create_response = admin_api.create_product(product_name)

    # THEN THE PRODUCT IS AVAILABLE TO BE USED IN THE APP
    assert create_response.status_code == 200, "Failed to add product (not 200 status code)"
    count_after = admin_api.get_current_product_count()
    assert count_after == count_before + 1, "List did not increase by one"

    product_list = admin_api.get_product_list()
    last_product = product_list[-1]
    assert last_product["name"] == product_name, "Last added product does not match product name"


def test_remove_product_from_catalog():

    # GIVEN I AM AN ADMIN USER
    admin_api = AdminAPI(BACKEND_URL)
    admin_api.get_admin_token()

    # WHEN I REMOVE A PRODUCT FROM THE CATALOGUE
    # Create product to delete
    product_name = f"delete_product_{int(time.time())}"
    admin_api.create_product(product_name)

    # Delete product
    count_before = admin_api.get_current_product_count()
    delete_response = admin_api.delete_product_by_name(product_name)

    # THEN THE PRODUCT SHOULD NOT BE LISTED IN THE APP TO BE USED
    assert delete_response.status_code == 200, "Product deleted properly (correct status code)"
    count_after = admin_api.get_current_product_count()
    assert count_after == count_before -1, "List did not decrease by one"
    
    product_list = admin_api.get_product_list()
    if len(product_list) > 0:
        last_product = product_list[-1]
        assert last_product["name"] != product_name, "Deleted product still appears"


