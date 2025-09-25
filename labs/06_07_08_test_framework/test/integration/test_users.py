from playwright.sync_api import Page
# complete imports
import libs.utils
from playwright.sync_api import Page
from libs.utils import generate_string_with_prefix
from models.api.user import UserAPI


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = generate_string_with_prefix()
    password = "testare_123?"

    print(username, password)


    user_api = UserAPI('http://localhost:8000')

    # When I signup in the app​
    signup_api_response = user_api.signup(username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    # complete code
    pass 
    # Given I am an authenticated user​
    username = "testare_arre"
    password = "testare_123"

    user_api = UserAPI('http://localhost:8000')

    # When I log in into the application​
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    # Then I should see all my products
    user_api_response = user_api.get_user_details(user_api.token)
    assert user_api_response.status_code == 200
    data = user_api_response.json()
    assert data["products"] == []