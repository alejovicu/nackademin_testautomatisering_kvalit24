from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
# complete imports

import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    # complete code
    username = libs.utils.generate_string_with_prefix("user_")
    password = libs.utils.generate_string_with_prefix("pass_")

    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()
    signup_page = SignupPage(page)
    signup_page.signup(username, password)
    signup_page.go_to_home()
    home_page.login(username, password)

    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    username = "user_account"
    password = "user_pass"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)

    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()
    expect(page.locator('h3:has-text("Your Products")')).to_be_visible()