import pytest
import libs.utils

from models.api.user import UserAPI

BASE_URL = "http://127.0.0.1:8000"

# Fixture to handle login
@pytest.fixture
def user_api():
    user_api = UserAPI(BASE_URL)
    login_response = user_api.login("user_account", "user_pass")
    assert login_response.status_code == 200
    return user_api


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    username = libs.utils.generate_string_with_prefix()
    password = libs.utils.generate_string_with_prefix("pass_")

    user_api = UserAPI(BASE_URL)

    signup_api_response = user_api.signup(username, password)

    assert signup_api_response.status_code == 200
    
    login_api_response = user_api.login(username, password)

    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(user_api):
    user_profile_response = user_api.get_user_profile()
    user_profile = user_profile_response.json()
    products = user_profile.get("products")

    # Check if status code is correct
    assert user_profile_response.status_code == 200
    # Check if the returned json contains correct key
    assert "products" in user_profile
    # Check if the products is in correct format (list)
    assert isinstance(products, list)


def test_assign_product_to_user(user_api):
    product_to_assign = "Banan"

    # Count assigned products before assigning
    num_of_products_before = user_api.num_of_user_products()
    assign_product_response = user_api.assign_product_to_user(product_to_assign)

    # Check if correct status code is returned
    assert assign_product_response.status_code == 200
    # Check if any product in productlist matches product_to_assign 
    assert any(product.get("name") == product_to_assign for product in user_api.user_products())
    # Check if number of products has increased
    assert user_api.num_of_user_products() == num_of_products_before + 1


def test_remove_product_from_user(user_api):
    product_to_unassign = "Banan"

    # Count assigned products before unassigning
    num_of_products_before = user_api.num_of_user_products()
    unassign_product_response = user_api.unassign_product_from_user(product_to_unassign)

    # Check if correct status code is returned
    assert unassign_product_response.status_code == 200
    # Check if any product in productlist matches product_to_unassign 
    assert any(product.get("name") != product_to_unassign for product in user_api.user_products())
    # Check if number of products has dencreased
    assert user_api.num_of_user_products() == num_of_products_before - 1
