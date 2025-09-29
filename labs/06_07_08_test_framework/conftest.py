import pytest
import os
from models.api.user import UserAPI


@pytest.fixture(scope="session", autouse=True)
def setup_admin_user():
    """
    Ensures the first registered user is created before any tests run.
    This fixture runs once per test session.
    """
    username = "user_admin"
    password = "test_1234"
    backend_url = os.getenv("BACKEND_URL_TEST", "http://localhost:8000")

    admin_api = UserAPI(backend_url)

    try:
        admin_api.signup(username, password)
        print(f"[setup_admin_user] Created admin user: {username}")
    except Exception as e:
        print(
            f"[setup_admin_user] Skipping admin user setup (might already exist): {e}"
        )
