# complete imports
import os
import libs.utils
from models.api.user import UserAPI


BASE_URL_BACKEND = os.getenv("BASE_URL_BACKEND", "http://localhost:8000")


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix("user", 8)
    password = "pass1234"

    user_api = UserAPI(BASE_URL_BACKEND)

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
    username = "user_1"
    password = "pass1234"
    user_api = UserAPI(BASE_URL_BACKEND)

    # When I log in into the application​
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    token = login_api_response.json()["access_token"]
    user_api.set_token(token)

    # Then I should see all my products
    user_data_api_response = user_api.get_user_data()
    assert user_data_api_response.status_code == 200

    products = user_data_api_response.json()["products"]

    if products:
        print(f"Found {len(products)} product(s): {[p['name'] for p in products]}")
        assert len(products) > 0  # Verify at least 1 product
    else:
        print("No products assigned to this user.")
        assert products == []  # Verify the list is empty
