import libs.utils
import pytest
from models.api.admin import AdminAPI
import time

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

#Assert that id==1 here?

def test_add_product_to_catalog():

    # Helper function to login as admin and get token
    token = libs.utils.get_admin_token()
    admin_api = AdminAPI("http://localhost:8000", token)

    # Add product
    product_name = f"product_{int(time.time())}"
    count_before = admin_api.get_current_product_count()
    create_response = admin_api.create_product(product_name)

    # Assert that it worked
    assert create_response.status_code == 200, "Failed to add product (not 200 status code)"
    count_after = admin_api.get_current_product_count()
    assert count_after == count_before + 1, "List did not increase by one"



# Given I am an admin user​
# When I remove a product from the catalog​
# Then the product should not be listed in the app to be used

def test_remove_product_from_catalog():

    # Helper function to login as admin and get token
    token = libs.utils.get_admin_token()
    admin_api = AdminAPI("http://localhost:8000", token)

    # Create product to delete
    product_name = f"product_{int(time.time())}"
    admin_api.create_product(product_name)

    # Delete product
    count_before = admin_api.get_current_product_count()
    delete_response = admin_api.delete_product_by_name(product_name)

    #Assert that it worked
    assert delete_response.status_code == 200, "Product deleted properly (correct status code)"
    count_after = admin_api.get_current_product_count()
    assert count_after == count_before -1, "List did not decrease by one"


