from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
from models.product import ProductPage
import time
import uuid




def test_add_product_to_catalog(page: Page):

    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate()
    login_page.navigate_to_signup()

    signup_page = SignupPage(page)
    signup_page.sign_up("admin", "pass1234")

    signup_page.page.get_by_role("button", name="Login").click()
    login_page.login("admin", "pass1234")

    product = f"test_course_{uuid.uuid4()}"
    product_page = ProductPage(page)
    product_page.create_product(product)
    

def test_remove_product_from_catalog(page: Page):

    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate()
    login_page.navigate_to_signup()

    signup_page = SignupPage(page)
    signup_page.sign_up("admin", "pass1234")

    signup_page.page.get_by_role("button", name="Login").click()
    login_page.login("admin", "pass1234")

    product = f"test_course_{uuid.uuid4()}"
    product_page = ProductPage(page)
    product_page.create_product(product)
    
    
    product_page.delete_product(product)




    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
    