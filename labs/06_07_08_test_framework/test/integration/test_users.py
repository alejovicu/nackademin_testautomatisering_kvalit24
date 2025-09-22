from playwright.sync_api import Page
# complete imports
import libs.utils
from models.api.user import UserAPI


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234?"

    user_api = UserAPI('http://localhost:8000')

    # When I signup in the app​
    signup_api_response = user_api.signup(username,password)
    assert signup_api_response.status_code == 200

    # Then I should be able to log in with my new user
    login_api_response = user_api.login(username,password)
    assert login_api_response.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    # Given I am an authenticated user
    facade = UsersFacade(page)
    username, password = facade.login_as_new_user()

    # When I log in into the application
    home_page = HomePage(page)
    home_page.login(username, password)

    # Then I should see all my products
    user_page = UserPage(page)
    products = user_page.get_user_products()
    assert len(products) > 0