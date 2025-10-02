
import pytest
from models.api.user import UserAPI

@pytest.fixture(scope="session")
def user_api():
    return UserAPI(base_url="http://localhost:8000")

@pytest.fixture(scope="session")
def admin_token(user_api):
    username = "admin_qa"
    password = "pass_5678"

    # Try login
    try:
        token = user_api.login(username, password).get("access_token")
    except Exception:
        # If login fails, create user
        user_api.signup(username, password, role="admin")
        token = user_api.login(username, password).get("access_token")

    assert token is not None
    return token

@pytest.fixture(scope="session")
def user_token(user_api):
    username = "user_qa"
    password = "pass_5678"

    try:
        token = user_api.login(username, password).get("access_token")
    except Exception:
        user_api.signup(username, password)
        token = user_api.login(username, password).get("access_token")

    assert token is not None
    return token
