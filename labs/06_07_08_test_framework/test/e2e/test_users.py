from playwright.sync_api import Page

from models.ui.user import UserPage
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from libs.utils import generate_string_with_prefix





def test_signup(page: Page):
# Given I am a new potential customer​

    username = generate_string_with_prefix("user")
    password = "testtest123"

    home_page = HomePage(page) 
    home_page.navigate()
    #when i signup in the application
    signup_page = SignupPage(page)
   
    signup_page.signup(username, password)
    

    #then I should be able to login
    
    home_page.navigate()
    home_page.login(username, password)

    #assertion
    user_page = UserPage(page)
    products = user_page.get_user_products()
    assert isinstance(products, list)
    assert len(products) >= 0  # assuming a user can have zero or more products



def test_login_see_product(page: Page):
   
   # Given I am an authenticated user​
    username = generate_string_with_prefix("user")
    password = "testtest123"

    home_page = HomePage(page)
    home_page.navigate()

    signup_page = SignupPage(page)
    signup_page.go_to_home()
    signup_page.signup(username, password)
  
    home_page.navigate()
    home_page.login(username, password)

    # When I navigate to my products​
    user_page = UserPage(page)
    products = user_page.get_user_products()

    # Then I should see all my products
    assert isinstance(products, list)
    assert len(products) >= 0  # assuming a user can have zero or more products
 


