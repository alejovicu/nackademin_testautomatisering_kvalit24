from playwright.sync_api import Playwright, Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI

import uuid
import requests

API_URL = "http://localhost:8000"



def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = HomePage(page)
    admin_page = AdminPage(page)

    # Given I am an admin user​
    home_page.navigate()
    login_page.login("admin", "pass1234")

    # When I add a product to the catalog​
    product = f"test_course_{uuid.uuid4()}"
    admin_page.create_product(product)
    # THEN The product is available to be used in the app
    assert page.get_by_text("Products available:").is_visible()
    assert page.get_by_text(product).is_visible()


    # crosscheck API
    # note !!!!!!!!!!!!!
    ## note !! I know this might not be needed and will slow the test down.
    user_api = UserAPI(API_URL)
    token = user_api.login("admin", "pass1234")  # returns token string
    assert token is not None

    admin_api = AdminAPI(API_URL, token)
    products = admin_api.get_products()
    assert product in [p["name"] for p in products]


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()

    # Given I am an admin user​ - UI login
    login_page.login("admin", "pass1234")
    
    product = f"test_course_{uuid.uuid4()}"
    admin_page.create_product(product)

    # When I remove a product from the catalog​
    admin_page.delete_product_by_name(product)
    # Then The product should not be listed in the app to be used
    expect(page.get_by_text(product)).not_to_be_visible()
    assert not admin_page.product_exists(product)
    
    # crosscheck API to verify
    # note !!!!!!!!!!!!!
    ## note !! I know this might not be needed and will slow the test down.
    user_api = UserAPI(API_URL)
    token = user_api.login("admin", "pass1234")  # returns token string
    assert token is not None

    admin_api = AdminAPI(API_URL, token)
    product_list = admin_api.get_products()
    assert product not in [p["name"] for p in product_list]
