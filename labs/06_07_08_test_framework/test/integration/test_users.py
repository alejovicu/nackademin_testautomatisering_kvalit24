from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI("http://localhost:5173")

    # When I signup in the app​
    signup_api_response = user_api.signup = (username, password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login = (username, password)
    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products


def test_login():
    # Given I am an authenticated user​
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI("http://localhost:5173")
    login_api_response = user_api.login(username, password)
    assert login_api_response.status_code == 200

    token = login_api_response.json()["access_token"]
    user_api.set_token(token)

    user_api.login(username, password)
    assert user_api.status_code == 200

    products = user_api.get_user_products()
    assert isinstance(products, list), "Expected products to be a list"


### user_data_api_response = user_api.get_user_data()
##assert user_data_api_response.status_code == 200

##products = user_data_api_response.json()["products"]

##user_list = user_api.display_user_products()


# assert "products" in user_list, " User JSON does not contain key products"
# assert len(user_list["products"]) == 0, "No products assigned"
