import libs.utils
import pytest
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app


def test_add_product_to_catalog():
    # Login as admin
    user_api = UserAPI(BACKEND_URL)
    login_response = user_api.login("admin", "admin")
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    admin_api = AdminAPI(BACKEND_URL, token=token)

    # Create a unique product name
    product_name = libs.utils.generate_string_with_prefix("test_product")

    # When I create a product
    create_response = admin_api.create_product(product_name)
    assert create_response.status_code == 200  # typical for creation

    # Then I should see it in the product list
    product_count = admin_api.get_current_product_count()
    assert product_count >= 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used


def test_remove_product_from_catalog():
    # Login as admin
    user_api = UserAPI(BACKEND_URL)
    login_response = user_api.login("admin", "admin")
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    admin_api = AdminAPI(BACKEND_URL, token=token)

    # Create a unique product
    product_name = libs.utils.generate_string_with_prefix("test_product")
    create_resp = admin_api.create_product(product_name)
    # Access JSON from create response
    if hasattr(create_resp, "json"):
        created_json = create_resp.json()
    else:
        created_json = create_resp
    assert created_json["name"] == product_name

    # Get product count before deletion
    count_before = admin_api.get_current_product_count()

    # Delete the product
    delete_resp = admin_api.delete_product_by_name(product_name)
    # delete_resp should be dict (empty if backend returned no content)
    assert isinstance(delete_resp, dict)

    # Get product count after deletion
    count_after = admin_api.get_current_product_count()
    assert count_after == count_before - 1

    # Ensure deleting again raises ValueError
    with pytest.raises(ValueError):
        admin_api.delete_product_by_name(product_name)
