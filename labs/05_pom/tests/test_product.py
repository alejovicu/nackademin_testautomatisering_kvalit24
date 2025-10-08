from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
from models.product import ProductPage

admin_username = "test_user"
admin_password = "testtest123"

def test_add_product_to_catalog(page: Page):

    #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    home_page.navigate()
    login_page.navigate()

    # Navigate to signup
    login_page.login_btn_signup.click()
    # Create new user
    signup_page.signup(admin_username,admin_password)
    # Navigate to login
    signup_page.signup_btn_login.click()
    
    # Given I am an admin user​
    login_page.login(admin_username,admin_password)
    

    # When I add a product to the catalog​
    product_name = "Test Product"
    product_page = ProductPage(page)
    product_page.add_to_catalog(product_name)

    # Then The product is available to be used in the app

    product_page.validate_product_in_list(product_name)



  
def test_remove_product_from_catalog(page: Page):


    home_page = HomePage(page)
    login_page = LoginPage(page)
   
    # Given I am an admin user​
    home_page.navigate()
    login_page.navigate()
    login_page.login(admin_username,admin_password)

    # When I remove a product from the catalog​
    product_name = "Test Product"
    product_page = ProductPage(page)    
    product_page.remove_from_catalog(product_name)

    # Then The product should not be listed in the app to be used
    product_page.validate_product_not_in_list(product_name)



