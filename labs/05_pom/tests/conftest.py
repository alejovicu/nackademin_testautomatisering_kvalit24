import pytest
from utils.username_generator import generate_username


@pytest.fixture(scope="session")
def credentials():
    """
    Create a new username and password once per test run.
    All tests that use 'credentials' will get the same ones.
    """
    username = generate_username()
    password = "bandola"
    return username, password
