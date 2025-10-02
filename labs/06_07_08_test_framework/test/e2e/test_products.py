from playwright.sync_api import Playwright, Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os
import uuid
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")



def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = HomePage(page)
    admin_page = AdminPage(page)

    # Given I am an admin user​
    # note !! this admin-user must be added pre-test run
    home_page.navigate()
    login_page.login("admin", "pass1234")

    # When I add a product to the catalog​
    product = f"test_course_{uuid.uuid4()}"
    admin_page.create_product(product)

    # THEN The product is available to be used in the app
    admin_page.product_is_visible(product)


    # crosscheck API
    # note !!!!!!!!!!!!!
    ## note !! I know this might not be needed and will slow the test down.
    user_api = UserAPI(BACKEND_URL)
    user_api.login("admin", "pass1234")
    admin_api = AdminAPI(BACKEND_URL, user_api.token)
    assert admin_api.product_exists_in_backend(product)


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()

    # Given I am an admin user​ - UI login
    # note !! this admin-user must be added pre-test run
    login_page.login("admin", "pass1234")
    
    product = f"test_course_{uuid.uuid4()}"
    admin_page.create_product(product)
    admin_page.product_is_visible(product)

    # When I remove a product from the catalog​
    admin_page.delete_product_by_name(product)
    # Then The product should not be listed in the app to be used
    admin_page.product_to_not_be_visible(product)
    
    # crosscheck API to verify
    ## note !! I know this might not be needed and will slow the test down.
    user_api = UserAPI(BACKEND_URL)
    token = user_api.login("admin", "pass1234")  # stores
    admin_api = AdminAPI(BACKEND_URL, user_api.token)
    assert not admin_api.product_exists_in_backend(product)
