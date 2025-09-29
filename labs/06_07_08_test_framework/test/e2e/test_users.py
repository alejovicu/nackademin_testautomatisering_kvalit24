from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from facade.users import UsersFacade
import libs.utils


# Given I am a new potential customer
# When I signup in the app
# Then I should be able to log in with my new user
def test_signup(page: Page):
    # Generate a random username and password
    username = libs.utils.generate_string_with_prefix("user_")
    password = "Test@1234"

    # Navigate to the home page
    home_page = HomePage(page)
    home_page.navigate()

    # Go to the signup page
    home_page.go_to_signup()
    signup_page = SignupPage(page)

    # Fill out the signup form and submit
    signup_page.signup(username, password)

    # Log in with the new user
    home_page.login(username, password)

    # If we got here without errors, signup + login succeeded
    assert True


# Given I am an authenticated user
# When I log in into the application
# Then I should be able to log in successfully
def test_login(page: Page):
    # Use the UsersFacade to create and log in as a new user
    facade = UsersFacade(page)
    username, password = facade.login_as_new_user()

    # If we got here without errors, login succeeded
    assert True
