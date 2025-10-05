import libs.utils
import config 
import pytest
from models.api.admin import AdminAPI


# Define a fixture to set up the authenticated AdminAPI client once per test function
@pytest.fixture
def admin_api_client():
    """
    Fixture that initializes, logs in, and returns an authenticated AdminAPI instance.
    """
    
    BACKEND_URL = config.get_base_url()
    # Initialize the client
    api = AdminAPI(BACKEND_URL)
    
    # Login and verify success
    login_response = api.login()
    
    # Check for successful login and token
    if login_response.status_code != 200 or not api.token:
         # Log the error for better debugging 
         print(f"Login failed: Status {login_response.status_code}, Response: {login_response.text}")
         raise Exception("Admin login failed during test setup.")

    print(f"\n--- Admin logged in successfully with token: {api.token[:10]}... ---")
    return api


# Given I am an admin user
# When I add a product to the catalog
# Then The product is available to be used in the app
def test_add_product_to_catalog(admin_api_client):
    ## Given I am an admin user (Handled by the fixture)
    
    # 1. Setup unique product name
    product_name = libs.utils.generate_product_with_prefix("product")
    
    # 2. When I add a product to the catalog
    create_response = admin_api_client.create_product(product_name)
    assert create_response.status_code in [201, 200], f"Failed to create product: {create_response.text}"
    
    print(f" Created product name: {product_name}")
    
    # 3. Then The product is available
    products = admin_api_client.get_all_products()
    names = [product.get("name") for product in products]
    
    print(f" All product names: {names}")
    assert product_name in names, f"Product {product_name} not found in catalog after creation."
    
    
   
def test_remove_product_from_catalog(admin_api_client):
    ## Given I am an admin user (Handled by the fixture)
    
    # 1. Setup unique product name and create it first
    product_name = libs.utils.generate_product_with_prefix("product")
    create_response = admin_api_client.create_product(product_name)
    assert create_response.status_code in [201, 200], f"Setup failed: Could not create product {product_name}"
    
    # Sanity check: verify creation
    products_before = admin_api_client.get_all_products()
    assert product_name in [p.get("name") for p in products_before]
    
    # 2. When I remove a product from the catalog
    delete_response = admin_api_client.delete_product_by_name(product_name)
    
    # Assuming successful deletion returns 204 No Content
    # We allow 200/202/204 as common successful deletion codes
    assert delete_response and delete_response.status_code in [200, 202, 204], f"Failed to delete product: {delete_response.text if delete_response else 'No response'}"
    
    # 3. Then The product should not be listed
    products_after = admin_api_client.get_all_products()
    names_after = [product.get("name") for product in products_after]
    
    print(f" All product names after deletion: {names_after}")
    assert product_name not in names_after, f"Product {product_name}"
   



   



