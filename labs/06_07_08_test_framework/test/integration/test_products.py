# import libs.utils
# import pytest


# # Given I am an admin user​
# # When I add a product to the catalog​
# # Then The product is available to be used in the app
# def test_add_product_to_catalog():
#     # complete code
#     pass


# # Given I am an admin user​
# # When I remove a product from the catalog​
# # Then The product should not be listed in the app to be used
# def test_remove_product_from_catalog():
#     # complete code
#     pass
import libs.utils
import pytest
from api.admin import AdminAPI


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    # Get base URL and admin credentials
    base_url = libs.utils.get_base_url()
    creds = libs.utils.get_admin_credentials()

    # Login as admin to get token
    token = libs.utils.get_token(base_url, creds["username"], creds["password"])

    api = AdminAPI(base_url, token)

    # Count products before
    count_before = api.get_current_product_count()

    # Create product
    product_name = libs.utils.generate_random_product_name()
    created = api.create_product(product_name)

    assert created["name"] == product_name

    # Count should increase
    count_after = api.get_current_product_count()
    assert count_after == count_before + 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    base_url = libs.utils.get_base_url()
    creds = libs.utils.get_admin_credentials()
    token = libs.utils.get_token(base_url, creds["username"], creds["password"])

    api = AdminAPI(base_url, token)

    # Ensure product exists
    product_name = libs.utils.generate_random_product_name()
    created = api.create_product(product_name)
    assert created["name"] == product_name

    # Count before
    count_before = api.get_current_product_count()

    # Delete product
    deleted = api.delete_product_by_name(product_name)
    assert deleted is True

    # Count after
    count_after = api.get_current_product_count()
    assert count_after == count_before - 1
