import pytest
import os

from models.api.admin import AdminAPI

BASE_URL = os.getenv("APP_URL", "http://127.0.0.1:8000")

# Fixture to handle login
@pytest.fixture
def admin_api():
    admin_api = AdminAPI(BASE_URL)
    login_response = admin_api.login("admin", "admin")
    assert login_response.status_code == 200
    return admin_api


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(admin_api):
    product_to_create = "admin_product"

    num_of_products_before = admin_api.get_current_product_count()
    create_product_response = admin_api.create_product(product_to_create)

    # Check if status code is correct
    assert create_product_response.status_code == 200
    # Check if number of products has increased
    assert admin_api.get_current_product_count() == num_of_products_before + 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(admin_api):
    product_to_remove = "admin_product"

    num_of_products_before = admin_api.get_current_product_count()
    create_product_response = admin_api.delete_product_by_name(product_to_remove)

    # Check if status code is correct
    assert create_product_response.status_code == 200
    # Check if number of products has increased
    assert admin_api.get_current_product_count() == num_of_products_before - 1
