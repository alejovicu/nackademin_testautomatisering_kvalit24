from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
from models.product import ProductPage
import time
import uuid


# two functions / tests, 
# 1 for signup, login, create product. --- test_add_product_to_catalog
# and 1 for login, create, delete product --- test_remove_product_from_catalog
# Only UI asserts for this


def test_add_product_to_catalog(page: Page):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    signup_page = SignupPage(page)

    home_page.navigate()
    login_page.navigate_to_signup()

    signup_page.sign_up("admin", "pass1234") # <-- this is what is sent into the signup function in the SignupPage class

    login_page.login("admin", "pass1234")

    # creates a product "test_course" with a random number attached.
    product = f"test_course_{uuid.uuid4()}"

    # GIVEN I am an admin user
    # WHEN I add a product to the catalog
    product_page.create_product(product)
    # THEN The product is available to be used in the app #asssert product added exists
    assert product_page.product_exists(product) #here im calling for the product_exist function in product.py
    

def test_remove_product_from_catalog(page: Page):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    home_page.navigate()
    login_page.login("admin", "pass1234")

    # creates a product "test_course" with a random number attached.
    product = f"test_course_{uuid.uuid4()}"

    # GIVEN I am an admin user
    # WHEN I add a product to the catalog
    product_page.create_product(product)
    # THEN The product is available to be used in the app #asssert product added exists
    assert product_page.product_exists(product)

    # GIVEN I am an admin user
    # WHEN I delete a product from the catalog
    product_page.delete_product(product)
    # THEN The product is not available to be used in the app
    product_page.product_does_not_exists(product)