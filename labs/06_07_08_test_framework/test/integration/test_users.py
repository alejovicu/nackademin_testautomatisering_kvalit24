# from playwright.sync_api import Page

# # complete imports
# import libs.utils
# from models.api.user import UserAPI


# # Given I am a new potential customer​
# # When I signup in the app​
# # Then I should be able to log in with my new user
# def test_signup():
#     # Given I am a new potential customer​
#     username = libs.utils.generate_string_with_prefix()
#     password = "test_1234?"

#     user_api = UserAPI("http://localhost:8000")

#     # When I signup in the app​
#     signup_api_response = user_api.signup(username, password)
#     assert signup_api_response.status_code == 200

#     # Then I should be able to log in with my new user
#     login_api_response = user_api.login(username, password)
#     assert login_api_response.status_code == 200


# # Given I am an authenticated user​
# # When I log in into the application​
# # Then I should see all my products
# def test_login():
#     # complete code
#     pass
from playwright.sync_api import Page  # Not really needed here, but kept for consistency
import libs.utils
from models.api.user import UserAPI


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI(libs.utils.get_base_url())

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
    # Given I am an authenticated user
    creds = libs.utils.get_test_user_credentials()
    username = creds["username"]
    password = creds["password"]

    user_api = UserAPI(libs.utils.get_base_url())

    # When I log in into the application
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    # Then I should see all my products
    headers = {"Authorization": f"Bearer {user_api.token}"}
    resp = libs.utils.requests.get(f"{user_api.base_url}/user", headers=headers)
    assert resp.status_code == 200

    user_data = resp.json()
    assert "products" in user_data
    assert isinstance(user_data["products"], list)
