from models.api.user import UserAPI
import os


## Ensures "first account" admin with proper credentials
def test_data_signup_admin():
    username = "user_admin"
    password = "test_1234"
    admin_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    admin_api.signup(username, password)
