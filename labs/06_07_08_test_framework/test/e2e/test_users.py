from playwright.sync_api import Playwright, Page
from models.ui.signup import SignupPage
from models.ui.home import HomePage
import pytest
import libs.utils



def test_signup(page: Page):
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_1234"
    
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    login_page = HomePage(page)

    home_page.navigate()
    home_page.go_to_signup()

    # When I signup in the app​
    signup_page.signup(username, password) # <-- this is what is sent into the signup function in the SignupPage class
    
    home_page.navigate()
    assert page.get_by_text('Nackademin Course App').is_visible()

    # Then I should be able to log in with my new user
    login_page.login(username, password)
    assert page.get_by_text("Welcome, "f"{username}").is_visible()
    assert page.get_by_text("Your Products:").is_visible()


def test_login_see_my_products(page: Page):
    # Given I am an authenticated user​
    # note !! this user must be added pre-test run
    username = "test_1234"
    password = "test_1234"
    
    home_page = HomePage(page)
    login_page = HomePage(page)

    home_page.navigate()
    assert page.get_by_text('Nackademin Course App').is_visible()

    # When I log in into the application​
    login_page.login(username, password)
    assert page.get_by_text("Welcome, "f"{username}").is_visible()
    assert page.get_by_text("Your Products:").is_visible()

    # Then I should see all my products
    # to be implemented?