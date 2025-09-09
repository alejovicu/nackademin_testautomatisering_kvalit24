import random
import string
import requests

# GENERATE USERNAME FOR SIGNUP
def generate_string_with_prefix(prefix: str = "user", length: int = 8) -> str:
    """
    Generate a string with a configurable prefix and a random string.

    Args:
        prefix (str): The prefix for the username (default: "user").
        length (int): Length of the random string to append (default: 8).

    Returns:
        str: A username like "user_ab12cd34".
    """
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}_{random_part}"


# LOG IN AS ADMIN AND RETURN TOKEN
# Works even if database is cleared and no admin exists
# BUT need to run test_products.py BEFORE test_users.py, otherwise a user will have id==1 and be considered admin
def get_admin_token():
    BASE_URL = "http://localhost:8000"
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"

    login_body = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
    login_response = requests.post(f"{BASE_URL}/login", json=login_body)

    if login_response.status_code == 200:
        return login_response.json().get("access_token")

    signup_body = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
    requests.post(f"{BASE_URL}/signup", json=signup_body) 

    login_response = requests.post(f"{BASE_URL}/login", json=login_body)
    token = login_response.json().get("access_token")
    return token