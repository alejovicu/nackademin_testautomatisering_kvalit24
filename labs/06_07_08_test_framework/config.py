import os
from models.api.user import UserAPI

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin_user")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "pass_1234")
USER_USERNAME = os.getenv("USER_USERNAME", "user_1")
USER_PASSWORD = os.getenv("USER_PASSWORD", "pass1234")

try:
    user_api = UserAPI(BACKEND_URL)
    user_api.signup(ADMIN_USERNAME, ADMIN_PASSWORD)
except:
    print("Admin user already exists.")


try:
    user_api = UserAPI(BACKEND_URL)
    user_api.signup(USER_USERNAME, USER_PASSWORD)
except:
    print("Test user already exists.")
