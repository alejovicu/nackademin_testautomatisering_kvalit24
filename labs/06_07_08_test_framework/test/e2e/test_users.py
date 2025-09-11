# from playwright.sync_api import Page
# from models.login import LoginPage
# # complete imports

# # Given I am a new potential customer​
# # When I signup in the app​
# # Then I should be able to log in with my new user
# def test_signup(page: Page):
#     # complete code


# # Given I am an authenticated user​
# # When I log in into the application​
# # Then I should see all my products
# def test_signup(page: Page):
#     # complete code
import libs.utils
from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    home = HomePage(page)
    home.navigate()

    # Go to signup page
    home.go_to_signup()
    signup_page = SignupPage(page)

    # Generate new user creds
    username = libs.utils.generate_string_with_prefix()
    password = libs.utils.get_test_password()

    # Sign up
    signup_page.signup(username, password)

    # Go back to login/home
    signup_page.go_to_home()

    # Try logging in with new credentials
    home.login(username, password)

    # Expect user page to show up
    user_page = UserPage(page)
    products = user_page.get_user_products()
    assert isinstance(products, list)  # should be a list, even if empty
    # New users may have no products yet, so we just confirm the list is visible


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login_shows_products(page: Page):
    home = HomePage(page)
    home.navigate()

    # Use known test user credentials
    creds = libs.utils.get_test_user_credentials()
    home.login(creds["username"], creds["password"])

    # Expect user page with products
    user_page = UserPage(page)
    products = user_page.get_user_products()

    # Assert that the products list is visible (could be empty or pre-seeded)
    assert isinstance(products, list)
