import os
from models.api.user import UserAPI
from models.api.admin import AdminAPI

def setup_admin():

    ADMIN_USER  = "nahom_admin"
    ADMIN_PASS = "1234"
    BASE_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
    user_api = UserAPI(BASE_URL)
    signup_response = user_api.signup(ADMIN_USER, ADMIN_PASS)

    if signup_response.status_code == 200:
        print("Admin user created successfully")
    else: 
        print("Admin user already exists")


def setup_user():

    username = "nahom50"
    passowrd = "nahom50"
    BASE_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
    user_api = UserAPI(BASE_URL)
    signup_response = user_api.signup(username, passowrd)

    if signup_response.status_code == 200:
        print("User user created successfully")
    else: 
        print("User user already exists")

