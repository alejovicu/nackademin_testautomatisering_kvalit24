from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
# complete imports

import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "Tomat_123"

    login_home_page = HomePage (page)
    login_home_page.navigate()
    login_home_page.go_to_signup()

    page_signup = SignupPage(page)
    page_signup.signup(username, password)
    page_signup.go_to_home()

    login_home_page.login(username, password)
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()



# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    username  = "användare"
    password = "Flagga_123"

    login_home_page = HomePage (page)
    login_home_page.navigate()

    login_home_page.login(username, password)
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()

    user_product_page = UserPage(page)
    current_product = user_product_page.get_user_products()

    assert len(current_product) > 0, "No products found"