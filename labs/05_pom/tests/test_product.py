from playwright.sync_api import Page, expect
from models.signup import SignupPage
from models.login import LoginPage
from models.home import HomePage
import time

def test_add_product_to_catalog(page: Page):
    signup = SignupPage(page)
    login = LoginPage(page)
    home = HomePage(page)

    username = "admin"
    password = "admin123"
    product_name = f"product_{int(time.time())}"

    # Given I am an admin user​
    signup.navigate()
    signup.register_user(username, password)
    login.login_user(username, password)

    # When I add a product to the catalog​
    home.add_product(product_name)

    # Then The product is available to be used in the app​
    expect(page.get_by_text(product_name)).to_be_visible()

def test_remove_product_from_catalog(page: Page):
    signup = SignupPage(page)
    login = LoginPage(page)
    home = HomePage(page)

    username = "admin"
    password = "admin123"
    product_name = f"product_{int(time.time())}"

    # Given I am an admin user​
    signup.navigate()
    signup.register_user(username, password)
    login.login_user(username, password)

    # create product
    home.add_product(product_name)

    # When I remove a product from the catalog​
    home.delete_product(product_name)

    # Then The product should not be listed in the app to be used​
    expect(page.get_by_text(product_name)).not_to_be_visible()