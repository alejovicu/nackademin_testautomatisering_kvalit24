import os
from models.api.user import UserAPI

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1234")
USER_USERNAME = os.getenv("USER_USERNAME", "user2")
USER_PASSWORD  = os.getenv("USER_PASSWORD", "5678")



try:
    user_api = UserAPI(BACKEND_URL)
    user_api.signup(ADMIN_USERNAME, ADMIN_PASSWORD)
except:
    print("Admin already exist.")


try:
    user_api = UserAPI(BACKEND_URL)
    user_api.signup(USER_USERNAME, USER_PASSWORD)
except:
    print("User already exist.")