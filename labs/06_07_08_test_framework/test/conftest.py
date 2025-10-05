from models.api.user import UserAPI
from config import BACKEND_URL, ADMIN_USERNAME, ADMIN_PASSWORD

def pytest_sessionstart(session):
    username = ADMIN_USERNAME
    password = ADMIN_PASSWORD
    user_api = UserAPI(BACKEND_URL)
    
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200
