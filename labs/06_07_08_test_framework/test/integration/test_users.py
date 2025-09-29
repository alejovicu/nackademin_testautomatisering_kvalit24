from playwright.sync_api import Page
from models.api.user import UserAPI
# INTEGRATIONSTESTNING (BACKEND,API)
import libs.utils
import os

BASE_URL = os.getenv("BACKEND","http://localhost:8000/")

def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"
    
    user_api = UserAPI(BASE_URL)
           
    sign_up_api_response = user_api.signup(username,password)
    assert sign_up_api_response.status_code == 200
    
    api_response = user_api.login(username,password)
    assert api_response.status_code == 200
    

def test_login():
    username = "admin"
    password = "admin1234"
    
    user_api = UserAPI(BASE_URL)
            
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200












    