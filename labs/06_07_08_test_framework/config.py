import os

def get_admin_credentials():
    
    # Using 'admin' as default is common for local testing, but should be set in environment variables
    username = os.getenv("ADMIN_USERNAME", "admin")
    password = os.getenv("ADMIN_PASSWORD", "admin")
    return username, password
def is_admin(user_id):
    return user_id == 1

def get_user_credentials():
    username = os.getenv("USER_USERNAME", "user")
    password = os.getenv("USER_PASSWORD", "user")
    return username, password
def is_user(user_id):
    return user_id == "standard"

def get_base_url():
    return os.getenv("BACKEND_URL", "http://localhost:8000")

def get_frontend_url():
    return os.getenv("FRONTEND_URL", "http://localhost")

''''
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")'''
