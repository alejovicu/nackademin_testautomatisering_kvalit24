from playwright.sync_api import Page, expect

from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password =  "pass_test"

    home_page = HomePage(page)
    home_page.navigate()

    expect(page.get_by_text("Login")).to_be_visible(timeout=5000)

    home_page.go_to_signup()
    
    signup = SignupPage(page)
    signup.signup(username, password)

    page.wait_for_load_state("networkidle")
    expect(page.get_by_text("Login")).to_be_visible(timeout=5000)

    signup.go_to_home()

    home_page.login(username, password)
    expect(page.get_by_text("Your Products:")).to_be_visible()

    user_page = UserPage(page)
    items = user_page.get_user_products()
    assert isinstance(items, list)



# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    username = "test123"
    password = "test_123"
 
    
    #login
    home_page = HomePage(page)
    home_page.navigate()

    home_page.login(username, password)
    expect(home_page.login_header_main_title).to_be_visible()
    expect(page.get_by_text("Your Products:")).to_be_visible()

    #see all products
    list_user_product = UserPage(page)
    list_user_product.get_user_products()

    #atleast one product should exist
    expect(page.get_by_text("Your Products:")).to_be_visible()




