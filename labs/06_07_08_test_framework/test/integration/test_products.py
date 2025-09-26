from playwright.sync_api import Page
import libs.utils
import pytest
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import requests

import os

BACKEND_URL = os.environ.get("BACKEND_URL" , "http://localhost:8000")

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    admin_user = UserAPI(BACKEND_URL)

    
    login_response = admin_user.login("admin", "1234")
    assert login_response.status_code == 200

    
    token = login_response.json().get("access_token")
    admin_user.token = token  

    admin_api = AdminAPI(BACKEND_URL, admin_user.token)

    
    product_name = "Test3"

    count_before = admin_api.get_current_product_count()
    response = admin_api.create_product(product_name)
    
    assert response.status_code == 200
    assert response.json().get("name") == product_name

    count_after =admin_api.get_current_product_count()
    assert count_after ==count_before +1

# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():

    admin_user = UserAPI(BACKEND_URL)

    login_response = admin_user.login("admin", "1234")
    assert login_response.status_code == 200

    
    token = login_response.json().get("access_token")
    admin_user.token = token 
    admin_api = AdminAPI(BACKEND_URL, admin_user.token)

    # Ta bort produkt
    product_name = "Test3"
    
    delete_response = admin_api.delete_product_by_name(product_name)
    assert delete_response.status_code == 200

    
    products = requests.get(
        f"{BACKEND_URL}/products",
        headers={"Authorization": f"Bearer {token}"}
        ).json()
    
    product_names = [p.get("name") for p in products]
    assert product_name not in product_names
