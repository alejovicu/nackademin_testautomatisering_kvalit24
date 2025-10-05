'''import libs.utils
from models.api.user import UserAPI
from config import BACKEND_URL, USER_USERNAME, USER_PASSWORD

# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user

def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = USER_PASSWORD

    user_api = UserAPI(BACKEND_URL)
# Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200
    assert login_api_response.json().get("access_token") is not None


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    # complete code
    username = USER_USERNAME
    password = USER_PASSWORD
    user_api = UserAPI(BACKEND_URL)
    
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200

    products = login_api_response.json().get("products", [])
    assert products ==[]'''

from playwright.sync_api import Page
# complete imports
import libs.utils
from models.api.user import UserAPI
from config import get_base_url, get_user_credentials
#user_api = UserAPI('http://localhost:8000')
# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
BASE_URL=get_base_url()
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "123"

    user_api = UserAPI(BASE_URL)

    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200
    assert login_api_response.json().get("access_token") is not None


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    # complete code
    username = libs.utils.generate_string_with_prefix()
    password = "123"

    user_api = UserAPI(BASE_URL)
    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200

    products = login_api_response.json().get("products", [])
    assert products ==[]
    

    







    
    
    
    

    







    
    
    