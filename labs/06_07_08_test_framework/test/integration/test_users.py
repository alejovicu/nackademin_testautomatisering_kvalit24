from playwright.sync_api import Page
<<<<<<< HEAD
from models.api.user import UserAPI
# INTEGRATIONSTESTNING (BACKEND,API)
import libs.utils
import os

BASE_URL = os.getenv("BACKEND","http://localhost:8000/")
=======
# complete imports
import libs.utils
from models.api.user import UserAPI
>>>>>>> 4007169f48709b48b776125c775acc67d6e7056c

def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"
    
    user_api = UserAPI(BASE_URL)
           
    sign_up_api_response = user_api.signup(username,password)
    assert sign_up_api_response.status_code == 200
    
    api_response = user_api.login(username,password)
    assert api_response.status_code == 200
    

<<<<<<< HEAD
def test_login():
    username = "admin"
    password = "admin1234"
    
    user_api = UserAPI(BASE_URL)
            
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200












    
=======
# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
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
    # complete code
    pass
>>>>>>> 4007169f48709b48b776125c775acc67d6e7056c
