#from playwright.sync_api import Page
#from models.login import LoginPage
# complete imports

#import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
#def test_signup(page: Page):
    # complete code


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
#def test_signup(page: Page):
    # complete code

#from models.ui.home import HomePage
#import libs.utils
#from models.api.user import UserAPI

#def test_signup(page):
    #username = libs.utils.generate_string_with_prefix()
    #password = "test_1234?"

    #user_api = UserAPI('http://localhost:8000')

    #signup_response = user_api.signup(username, password)
    #assert signup_response.status_code == 200

    #login_response = user_api.login(username, password)
    #assert login_response.status_code == 200


# tests/e2e/test_users.py

from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
import libs.utils

def test_user_signup_and_login(page: Page):
    username = libs.utils.generate_string_with_prefix("user")
    password = "test_1234?"

    # Go to homepage
    page.goto("http://localhost:5173/")

    home = HomePage(page)
    home.go_to_signup()

    signup = SignupPage(page)
    signup.signup(username, password)

    # Wait for navigation to finish after signup
    page.wait_for_load_state("networkidle")
    home.navigate()

    # Wait until the login button is visible using your real locator
    home.login_btn_login.wait_for(state="visible", timeout=10000)
    home.login(username, password)

    user_page = UserPage(page)

    # Assertions
    expect(page.locator(f"text=Welcome, {username}!")).to_be_visible()
    assert isinstance(user_page.get_user_products(), list)
