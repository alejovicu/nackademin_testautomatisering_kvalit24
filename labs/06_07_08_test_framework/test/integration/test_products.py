import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os

VITE_BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    # Given I am an admin user​
    username = "admin"
    password = "1234"
    product_name = libs.utils.generate_product_string_with_prefix()

    user_api = UserAPI(VITE_BACKEND_URL)

    user_api.login(username, password)  # Login as admin
    assert user_api.status_code == 200

    admin_api = AdminAPI(
        VITE_BACKEND_URL, token=user_api.token
    )  # Passing the token to the admin api

    count_before = (
        admin_api.get_current_product_count()
    )  # Fetching product count before adding

    # When I add a product to the catalog​
    admin_api.create_product(product_name)
    assert admin_api.status_code == 200

    count_after = (
        admin_api.get_current_product_count()
    )  # Fetching product count after adding

    # Then The product is available to be used in the app
    assert count_after == count_before + 1, "Product count did not increase by 1"

    product_names = []
    for product in admin_api.get_product_list():
        product_names.append(product.get("name"))
    assert product_name in product_names, "The added product is not in the list"


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    # Given I am an admin user​
    username = "admin"
    password = "1234"
    product_name = libs.utils.generate_product_string_with_prefix()

    user_api = UserAPI(VITE_BACKEND_URL)

    user_api.login(username, password)  # Login as admin
    assert user_api.status_code == 200

    admin_api = AdminAPI(
        VITE_BACKEND_URL, token=user_api.token
    )  # Passing the token to the admin api

    admin_api.create_product(product_name)
    assert admin_api.status_code == 200

    # When I remove a product from the catalog​
    count_before = (
        admin_api.get_current_product_count()
    )  # Fetching product count before removing
    admin_api.delete_product_by_name(product_name)
    count_after = (
        admin_api.get_current_product_count()
    )  # Fetching product count after adding

    # Then The product should not be listed in the app to be used
    product_names = []
    for product in admin_api.get_product_list():
        product_names.append(product.get("name"))
    assert product_name not in product_names, (
        "The added product is still in the list after removal"
    )

    assert count_after == count_before - 1, "Product count did not decrease by 1"
