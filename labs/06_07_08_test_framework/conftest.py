import pytest
import os

@pytest.fixture(scope="session")
def base_url():
    """Backend API base URL"""
    return os.environ.get('BACKEND_URL', 'http://app-backend:8000')

@pytest.fixture(scope="session")
def frontend_url():
    """Frontend base URL"""
    return os.environ.get('FRONTEND_URL', 'http://app-frontend:5173')

@pytest.fixture(scope="function")
def admin_credentials():
    """Admin user credentials - using your existing DB_admin user"""
    return {
        'username': 'DB_admin',
        'password': 'admin123'
    }