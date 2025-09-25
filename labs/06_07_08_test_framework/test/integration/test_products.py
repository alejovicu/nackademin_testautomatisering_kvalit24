

from playwright.sync_api import Page
from models.api.admin import AdminAPI



def test_add_product_to_catalog():
    api = AdminAPI("http://127.0.0.1:8000")
    username = "nermin123"
    password = "nermin_123"
    product_name = "Jacket"


    admin_login = api.admin_login(username, password)
    assert admin_login.status_code == 200

    save_token = admin_login.json()["access_token"]
    api.auth_token(save_token)

    before_count = api.product_count()
    create_new_product = api.create_product(product_name)
    assert create_new_product.status_code == 200

    after_count = api.product_count()
    assert after_count == before_count +1





def test_remove_product_from_catalog():
    api = AdminAPI("http://127.0.0.1:8000")
    username = "nermin123"
    password = "nermin_123"
    product_name = "Jacket"
    product_id = None


    admin_login = api.admin_login(username, password)
    assert admin_login.status_code == 200

    save_token = admin_login.json()["access_token"]
    api.auth_token(save_token)

    product_list = api.get_all_products()
    for p in product_list:
        if p["name"] == product_name:
            product_id = p["id"]
            break
    assert product_id is not None, f"The product: {product_name} was not found"

    delete_product = api.delete_product_by_name(product_id)
    assert delete_product.status_code == 200 



import libs.utils
import pytest


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    # complete code
    pass



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    # complete code
    pass