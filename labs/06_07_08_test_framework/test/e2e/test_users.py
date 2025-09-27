from playwright.sync_api import Page, expect
#from models.login import LoginPage
# complete imports
from models.ui.home import HomePage
from models.ui.signup import SignupPage
#from models.ui.admin import AdminPage
from models.ui.user import UserPage
#from models.api.user import UserAPI
import libs.utils



# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    # complete code
   
    username= libs.utils.generate_string_with_prefix("user")
    password="123"

    home_page= HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()
    

    signup= SignupPage(page)
   
    signup.signup(username, password)
    signup.go_to_home()

    

    home_page.login(username, password)
 
    assert(home_page.header).get_by_role(f"Welcome {username}")
   







   




# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_authenticated_user_signup(page: Page):
    # complete code
# Setup test data
    

    username = "asif"
    password = "khan"


    #login
    home_page = HomePage(page)
    home_page.navigate()

    home_page.login(username, password)
    assert(page.get_by_text("Your Products:"))
    #.to_be_visible()

    #see all products
    list_user_product = UserPage(page)
    items_count = list_user_product.get_user_products()

    #atleast one product should exist
    assert len(items_count) ==0 

    
