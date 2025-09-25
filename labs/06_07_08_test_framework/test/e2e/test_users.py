from playwright.sync_api import Page, expect
from models.ui.signup import SignupPage
from models.ui.home import HomePage
from models.ui.user import UserPage
# complete imports
import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    home = HomePage(page)
    home.navigate()
    home.go_to_signup()

    username = libs.utils.generate_string_with_prefix("user")
    password = libs.utils.generate_string_with_prefix("pass")

    register = SignupPage(page)
    register.signup(username, password)

    register.go_to_home()
    home.login(username, password)

    expect(page.get_by_text("Your Products:")).to_be_visible()


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    home = HomePage(page)
    home.navigate()
    
    username = "nahom50"
    password = "nahom50"

    home.login(username, password)

    user_products = UserPage(page)

    product_count = user_products.get_user_products()
    assert len(product_count) > 0, "No available items/products"
    