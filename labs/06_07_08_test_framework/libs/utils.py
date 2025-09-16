# import random
# import string

# def generate_string_with_prefix(prefix: str = "user", length: int = 8) -> str:
#     """
#     Generate a string with a configurable prefix and a random string.

#     Args:
#         prefix (str): The prefix for the username (default: "user").
#         length (int): Length of the random string to append (default: 8).

#     Returns:
#         str: A username like "user_ab12cd34".
#     """
#     random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
#     return f"{prefix}_{random_part}"

import random
import string
import requests


def generate_string_with_prefix(prefix: str = "user", length: int = 8) -> str:
    """
    Generate a string with a configurable prefix and a random string.
    Example: "user_ab12cd34"
    """
    random_part = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )
    return f"{prefix}_{random_part}"


def generate_random_product_name(length: int = 6) -> str:
    """
    Generate a random product name like 'product_xyz123'.
    """
    random_part = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )
    return f"product_{random_part}"


def get_base_url() -> str:
    """
    Return the API base URL for the backend.
    Adjust here if your backend runs on a different port.
    """
    return "http://localhost:8000"


def get_admin_credentials() -> dict:
    """
    Return admin credentials.
    Adjust values if your backend seeds a different admin user.
    """
    return {"username": "admin", "password": "admin123"}


def get_test_user_credentials() -> dict:
    """
    Return test user credentials for login tests.
    Adjust values to match a seeded test user in your DB.
    """
    return {"username": "testuser", "password": "test_1234?"}


def get_test_password() -> str:
    """
    Default password used for newly generated test users.
    """
    return "test_1234?"


def get_token(base_url: str, username: str, password: str) -> str:
    """
    Login to the backend and return a JWT access token.
    """
    body = {"username": username, "password": password}
    resp = requests.post(f"{base_url}/login", json=body)
    resp.raise_for_status()
    data = resp.json()
    token = data.get("access_token")
    if not token:
        raise ValueError("Login did not return access_token")
    return token
