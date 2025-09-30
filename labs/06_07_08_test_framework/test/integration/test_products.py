from playwright.sync_api import Page
from models.api.admin import AdminAPI
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
admin_api = AdminAPI(BACKEND_URL)
USERNAME = "test_admin"
PASSWORD = "admin_test321"


def test_add_product_to_catalog():
    
    # Given I am an admin user​
    admin_login_response = admin_api.admin_login(USERNAME, PASSWORD)
    assert admin_login_response.status_code == 200

    # Token
    admin_token = admin_login_response.json()["access_token"]
    admin_api.set_admin_token(admin_token)

    # When I add a product to the catalog​
    product_name = "Bag"
    before_counting = admin_api.get_current_product_count()
    create_product_response = admin_api.create_product(product_name)

    # Then the product is available to be used in the app
    assert create_product_response.status_code == 200
    after_counting = admin_api.get_current_product_count()
    product_id = create_product_response.json()["id"]

    assert product_id is not None
    assert after_counting == before_counting + 1


def test_remove_product_from_catalog():

    # Given I am an admin user​
    admin_login_response = admin_api.admin_login(USERNAME, PASSWORD)
    assert admin_login_response.status_code == 200

    # Token
    admin_token = admin_login_response.json()["access_token"]
    admin_api.set_admin_token(admin_token)

    # When I remove a product from the catalog​
    product_name = "Bag"
    product_id = None

    products = admin_api.get_all_products()

    for product in products:
        if product["name"] == product_name:
            product_id = product["id"]
            break

    assert product_id is not None, f"Product '{product_name}' not found"

    # Then the product should not be listed in the app to be used
    delete_product_response = admin_api.delete_product_by_name(product_id)
    assert delete_product_response.status_code == 200