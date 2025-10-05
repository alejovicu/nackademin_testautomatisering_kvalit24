import libs.utils
from models.api.user import UserAPI

def test_signup(base_url):
    """Test user signup and login"""
    username = libs.utils.generate_string_with_prefix("intuser")
    password = "Test123!@#"
    
    user_api = UserAPI(base_url)
    signup_response = user_api.signup(username, password)
    assert signup_response.status_code == 200
    
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200
    assert 'access_token' in login_response.json()

def test_login(base_url):
    """Test that logged in user can see their products"""
    username = libs.utils.generate_string_with_prefix("intuser")
    password = "Test123!@#"
    
    user_api = UserAPI(base_url)
    user_api.signup(username, password)
    
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200
    
    user_info_response = user_api.get_user_info()
    assert user_info_response.status_code == 200
    user_data = user_info_response.json()
    assert 'products' in user_data
    assert isinstance(user_data['products'], list)