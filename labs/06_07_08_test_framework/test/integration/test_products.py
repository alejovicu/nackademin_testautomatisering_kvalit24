########NOTES:need to understand####################
import libs.utils
import pytest
from models.api.admin import AdminAPI


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    ## Given I am an admin user​ 
    username="admin"
    password="admin"

    admin_api=AdminAPI("http://localhost:8000",token=None)
    login_response=admin_api.login(username, password)
    assert login_response.status_code == 200
    token=login_response.json().get("access_token")
    assert token is not None
    admin_api=AdminAPI("http://localhost:8000",token=token) 
    assert admin_api.token == token
    product_name = libs.utils.generate_product_with_prefix("product")
    initial_product_count = admin_api.get_current_product_count()

    ## When I add a product to the catalog​
    admin_api.create_product(product_name)

    ## Then The product is available to be used in the app
    assert admin_api.get_current_product_count() == initial_product_count + 1
   



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    # complete code
    # Given I am an admin user
    admin_api = AdminAPI("http://localhost:8000", token=None)
    login_response = admin_api.login("admin", "admin")
    assert login_response.status_code == 200

    token = login_response.json().get("access_token")
    assert token is not None
    admin_api = AdminAPI("http://localhost:8000", token=token)

    # Create a product to later delete
    '''product_name = generate_product_with_prefix("testproduct")
    admin_api.create_product(product_name)

    all_products = admin_api.get_all_products()
    assert any(p["name"] == product_name for p in all_products)

    # When I remove the product from the catalog
    admin_api.delete_product_by_name(product_name)

    # Then The product should not be listed
    updated_products = admin_api.get_all_products()
    assert all(p["name"] != product_name for p in updated_products)'''
   
