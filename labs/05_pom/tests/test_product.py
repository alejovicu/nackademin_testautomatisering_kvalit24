# from playwright.sync_api import Page, expect

# from models.home import HomePage
# from models.login import LoginPage


# def test_add_product_to_catalog(page: Page):

#   #PO usage example
#  home_page = HomePage(page)
#   login_page = LoginPage(page)
#   home_page.navigate()
#  login_page.navigate_to_signup()


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
# pass

# def test_remove_product_from_catalog(page: Page):
# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
#    pass

import os
import uuid
import sys
import pathlib
from playwright.sync_api import Page
from models.login import LoginPage
from models.signup import SignupPage
from models.home import AdminPage

# Add the parent folder (05-pom) to sys.path so "models" can be imported
ROOT = pathlib.Path(__file__).resolve().parents[1]  # points to 05-pom folder
sys.path.insert(0, str(ROOT))


APP_URL = os.getenv("APP_URL", "http://localhost:5173")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin_dev")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "pass_1234")


def test_signup_can_register_new_user(page: Page):
    login = LoginPage(page, APP_URL).open()
    signup = SignupPage(page, APP_URL).open_from_login(login)

    username = f"user_{uuid.uuid4().hex[:6]}"
    password = "Password123!"
    signup.signup(username, password)
    # If you want, you can then return to login and attempt login (optional).
    # Here we just assert no exception and dialog accepted.


def test_admin_adds_product(page: Page):
    """Given I am an admin user
    When I add a product to the catalog
    Then the product is available to be used in the app
    """
    login = LoginPage(page, APP_URL).open()
    login.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    admin = AdminPage(page, APP_URL).expect_admin_dashboard()

    product_name = f"POM Product {uuid.uuid4().hex[:8]}"
    admin.add_product(product_name)

    # cleanup: remove product to keep test idempotent
    admin.delete_product(product_name)
