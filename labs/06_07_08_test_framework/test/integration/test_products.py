from libs.utils import generate_string_with_prefix
import pytest
from models.api.admin import AdminAPI


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():

    admin_api = AdminAPI('http://localhost:8000')
    admin_username = 'test_user'
    admin_password = 'testtest123'

    login_response = admin_api.login(admin_username, admin_password)
    assert login_response.status_code == 200

    product_name = generate_string_with_prefix("Product_", 5)

    add_response = admin_api.create_product(product_name)
    assert add_response.status_code == 200
    assert add_response.json().get("name") == product_name



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    admin_api = AdminAPI('http://localhost:8000')
    admin_username = "test_user"
    admin_password = "testtest123"

    login_response = admin_api.login(admin_username, admin_password)
    assert login_response.status_code == 200

    product_name = generate_string_with_prefix("Product_", 5)

    add_response = admin_api.create_product(product_name)
    assert add_response.status_code == 200
    assert add_response.json().get("name") == product_name

    admin_api.delete_product_by_name(product_name)
    products_response = admin_api.get_products()
    products = products_response.json()
    assert product_name not in [product["name"] for product in products]    
    
