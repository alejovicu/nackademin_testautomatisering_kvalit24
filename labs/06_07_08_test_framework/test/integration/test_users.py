from playwright.sync_api import Page
from models.api.user import UserAPI
import libs.utils
import os

BASE_URL = os.getenv("BACKEND_URL","http://localhost:8000/")

def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"
    
    user_api = UserAPI(BASE_URL)
           
    sign_up_api_response = user_api.signup(username,password)
    assert sign_up_api_response.status_code == 200
    
    api_response = user_api.login(username,password)
    assert api_response.status_code == 200
    

def test_login():
    username = "user1"
    password = "user1234"
    
    user_api = UserAPI(BASE_URL)
            
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200



def test_assign_product_to_user():
    product_to_assign = 1
    
    username = "user1"
    password = "user1234"
    user_api = UserAPI(BASE_URL)
            
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200

    assign_product_response = user_api.add_product_to_user(product_to_assign)

    # Check if correct status code is returned
    assert assign_product_response.status_code == 200
    
def test_remove_product_from_user():
    product_to_unassign = 1

    username = "user1"
    password = "user1234"
    user_api = UserAPI(BASE_URL)
            
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200

    unassign_product_response = user_api.remove_product_from_user(product_to_unassign)

    # Check if correct status code is returned
    assert unassign_product_response.status_code == 200