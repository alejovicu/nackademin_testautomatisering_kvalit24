from playwright.sync_api import Page
import libs.utils
import requests
from models.api.user import UserAPI

import os

BACKEND_URL = os.environ.get("BACKEND_URL" , "http://localhost:8000")





# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = "test1234"
    
    user_api = UserAPI(BACKEND_URL)

    signup_response = user_api.signup(username,password)
    assert signup_response.status_code == 200

    login_response = user_api.login(username,password)
    assert login_response.status_code == 200

    


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    username = "malle"
    password = "1234"
    
    user_api = UserAPI(BACKEND_URL)

    login_response = user_api.login(username,password)
    assert login_response.status_code == 200


def test_add_product_to_user():
    username_user = "malle"
    password_user = "1234"

    user_api = UserAPI(BACKEND_URL)
    login_user = user_api.login(username_user, password_user)
    assert login_user.status_code == 200

    product_id = 1   # ID från produktkatalogen
    add_product_response = user_api.add_product_to_user(product_id)
    assert add_product_response.status_code == 200


def test_remove_product_from_user():
    username_user = "malle"
    password_user = "1234"

    user_api = UserAPI(BACKEND_URL)
    login_user = user_api.login(username_user, password_user)
    assert login_user.status_code == 200

    product_id = 1   
    remove_response = user_api.remove_product_from_user(product_id)
    assert remove_response.status_code == 200


