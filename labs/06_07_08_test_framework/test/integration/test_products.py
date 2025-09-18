import libs.utils
import pytest
from models.api.admin import AdminAPI
from models.api.user import UserAPI


def test_add_product_to_catalog():

    # Given I am an admin user​
    base_url = "http://localhost:8000"
    admin_username = "testuser"
    admin_password = "testpassword"

    user_api = UserAPI(base_url)
    login_response = user_api.login(admin_username, admin_password)
    assert login_response.status_code == 200
    admin_token = user_api.token

    admin_api = AdminAPI(base_url, admin_token)

    # When I add a product to the catalog​
    product_name = libs.utils.generate_string_with_prefix()
    create_response, product_id = admin_api.create_product(product_name)
    assert create_response.status_code == 200
    assert product_id is not None

    # Then The product is available to be used in the app
    response = admin_api.get_current_product_count()
    assert response.status_code == 200
    products = response.json()
    product_names = [p["name"] for p in products]
    assert product_name in product_names


def test_remove_product_from_catalog():
    # Given I am an admin user​
    base_url = "http://localhost:8000"
    admin_username = "testuser"
    admin_password = "testpassword"

    user_api = UserAPI(base_url)
    login_response = user_api.login(admin_username, admin_password)
    assert login_response.status_code == 200
    admin_token = user_api.token

    admin_api = AdminAPI(base_url, admin_token)

    # When I remove a product from the catalog​
    response = admin_api.get_current_product_count()
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0

    last_product = products[-1]
    product_name = last_product["name"]
     # Ensure the product exists before attempting to delete

    delete_response = admin_api.delete_product_by_name(product_name)
    assert delete_response is not None
    assert delete_response.status_code == 200

    # Then The product should not be listed in the app to be used
    response_after_delete = admin_api.get_current_product_count()
    assert response_after_delete.status_code == 200
    products_after_delete = response_after_delete.json()
    product_names_after_delete = [p["name"] for p in products_after_delete]
    assert product_name not in product_names_after_delete
