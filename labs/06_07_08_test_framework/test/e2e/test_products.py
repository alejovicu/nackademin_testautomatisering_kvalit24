from playwright.sync_api import Playwright, Page
#from models.login import LoginPage
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI

import uuid
import sqlite3
import pytest
import libs.utils
import requests

API_URL = "http://localhost:8000"


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()

    # UI login
    login_page.login("admin", "pass1234")

    # API login
    user_api = UserAPI(API_URL)
    token = user_api.login("admin", "pass1234")
    admin_api = AdminAPI(API_URL, token)

    product = f"test_course_{uuid.uuid4()}"
    admin_page.create_product(product)
    # THEN The product is available to be used in the app
    assert admin_page.product_exists(product)

    # crosscheck API
    products = admin_api.get_products()
    assert product in [p["name"] for p in products]
    

# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()

    # Given I am an admin user​ - UI login
    login_page.login("admin", "pass1234")
    
    # API login
    user_api = UserAPI(API_URL)
    token = user_api.login("admin", "pass1234")
    admin_api = AdminAPI(API_URL, token)

    product = f"test_course_{uuid.uuid4()}"
    admin_page.create_product(product)


    # When I remove a product from the catalog​
    admin_page.delete_product_by_name(product)
    # Then The product should not be listed in the app to be used
    assert not admin_page.product_exists(product)
    
     # crosscheck API to verify
    products = admin_api.get_products()
    assert product not in [p["name"] for p in products]