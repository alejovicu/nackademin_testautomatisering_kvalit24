from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI
import os

BACKEND_URL = os.environ.get("BACKEND_URL","http://127.0.0.1:8000")
base_url = UserAPI (BACKEND_URL)
username = "användare"
password = "Flagga_123"

# complete imports
import libs.utils
from models.api.user import UserAPI

def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = "Tomat_123"
    print(username)

    signup_page = base_url.signup(username,password)
    assert signup_page.status_code == 200

    login_page = base_url.login(username,password)
    assert login_page.status_code == 200
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI('http://localhost:8000')

    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
   
   
    login_page = base_url.login(username,password)
    assert login_page.status_code == 200

    token_user = login_page.json()["access_token"]
    base_url.set_token(token_user)

def test_add_product_to_user():
    username = "användare"
    password = "Flagga_123"
   
    login_page = base_url.login(username,password)
    assert login_page.status_code == 200

    token_user = login_page.json()["access_token"]
    base_url.set_token(token_user)

    product_id = 5
    add_product = base_url.add_product_to_user(product_id)
    assert add_product.status_code == 200

def test_remove_product_from_user():
    username = "användare"
    password = "Flagga_123"
   
    login_page = base_url.login(username,password)
    assert login_page.status_code == 200

    token_user = login_page.json()["access_token"]
    base_url.set_token(token_user)

    product_id = 4
    remove_product = base_url.remove_product_from_user(product_id)
    assert remove_product.status_code == 200