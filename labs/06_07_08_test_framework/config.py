import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")
USER_USERNAME = os.getenv("USER_USERNAME", "user")
USER_PASSWORD = os.getenv("USER_PASSWORD", "user")


def get_admin_credentials():
    return ADMIN_USERNAME, ADMIN_PASSWORD
def is_admin(user_id):
    return user_id == 1

def get_user_credentials():
    return USER_USERNAME, USER_PASSWORD
def is_user(user_id):
    return user_id == "standard"

def get_base_url():
    return os.getenv("BACKEND_URL", "http://localhost:8000")

def get_frontend_url():
    return os.getenv("FRONTEND_URL", "http://localhost")

