
import libs.utils
import pytest
import time
import os
from models.api.admin import AdminAPI

BASE_URL_BACKEND =os.getenv("BASE_URL_BACKEND", "http://localhost:8000")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")

def admin_api():
    api = AdminAPI(BASE_URL_BACKEND, token=None)
    login_response = api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    

    token = login_response.json().get("access_token")
    assert token is not None
    api.token = token
    return api


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():
    ## Given I am an admin user​ 
    api=admin_api()
    product_name=libs.utils.generate_product_with_prefix("product")
    api.create_product(product_name)
    print(" Created product name:", product_name)
    products=api.get_all_products()
    names=[product["name"] for product in products]
    print(" All product names:", names)
    assert product_name in names

   
        
        



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used

    
def test_remove_product_from_catalog():
    api=admin_api()
    product_name=libs.utils.generate_product_with_prefix("product")
    api.create_product(product_name)
    print(" Created product name:", product_name)
    #assert create_products.status_code==200
   

  
    
    api.delete_product_by_name(product_name)
    products=api.get_all_products()
    names=[product["name"] for product in products]
    print(" All product names:", names)
    assert product_name not in names

   



   
