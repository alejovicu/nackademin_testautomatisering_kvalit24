from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
import libs.utils


def test_signup(page: Page):
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "test_user1234"

    login_page = HomePage(page)
    login_page.navigate()
    login_page.go_to_signup()

    # When I signup in the app​
    signup_page = SignupPage(page)
    signup_page.signup(username, password)
    signup_page.go_to_home()

    # Then I should be able to log in with my new user
    login_page.login(username, password)
    expect(page.get_by_text("Logout")).to_be_visible()

    
def test_login(page: Page):
    # Given I am an authenticated user​
    username = "test_user"
    password = "user_test321"

    # When I log in into the application​
    login_page = HomePage(page)
    login_page.navigate()

    login_page.login(username, password)
    expect(login_page.login_header_main_title).to_be_visible()
    expect(page.get_by_text("Logout")).to_be_visible()

    # Then I should see all my products
    user_page = UserPage(page)
    product_count = user_page.get_user_products()

    assert len(product_count) > 0, "No products found for this user"