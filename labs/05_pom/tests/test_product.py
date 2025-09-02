from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignUpPage
from models.product_page import ProductPage
import time


#SET UP
BASE_URL = "http://localhost:5173/"
username = "admin"
password = "admin123"


def test_add_and_remove_product_to_catalog(page: Page):

    # Skapar objekt av klasserna ("Models")
    home_page = HomePage(page) 
    login_page = LoginPage(page)
    signup_page = SignUpPage(page)
    product_page = ProductPage(page)

    # Genererar produktnamn
    new_product = f"product_{int(time.time())}"

    # Go to homepage
    home_page.navigate() 

    # Attempt sign-up
    login_page.navigate_to_signup() 
    signup_page.signup(username, password)

    # Login + assert admin
    signup_page.navigate_to_login()
    login_page.login(username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()

    # Add product + assert
    count_before_adding = product_page.add_product(new_product)
    expect(product_page.product.nth(-1)).to_contain_text(new_product)
    expect(product_page.product).to_have_count(count_before_adding + 1)

    # Delete product + assert
    deleted_product = product_page.delete_product(new_product)
    expect(deleted_product).to_have_count(0)