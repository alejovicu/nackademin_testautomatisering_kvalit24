from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
from test.conftest import setup, reset
import libs.utils
import sys
import os
# complete imports


def test_add_product_to_catalog(page: Page):
    setup()
    user_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    product = "Java-programmering för nybörjare"
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    username = os.getenv("admin_username", "Admin_user")
    password = os.getenv("admin_password", "Admin53")
    # Given I am an admin user​
    token = user_api.login_token(username, password)
    page.add_init_script(f"window.localStorage.setItem('token', '{token}')")
    home_page.nav()
    # When I add a product to the catalog​
    expect(admin_page.product_item.filter(has_text=product)).not_to_be_visible()
    admin_page.create_product(product)
    # Then The product is available to be used in the app
    expect(admin_page.product_item.filter(has_text=product)).to_be_visible()
    admin_page.logout_admin()


def test_remove_product_from_catalog(page: Page):
    user_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    product_name = os.getenv("product04", "Avancerad Java-programmering")
    # Given I am an admin user​
    username = os.getenv("admin_username", "Admin_user")
    password = os.getenv("admin_password", "Admin53")
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    token = user_api.login_token(username, password)
    page.add_init_script(f"window.localStorage.setItem('token', '{token}')")
    home_page.nav()
    # When I remove a product from the catalog​
    expect(admin_page.product_item.filter(has_text=product_name)).to_be_visible()
    admin_page.delete_product_by_name(product_name)
    # Then The product should not be listed in the app to be used
    expect(admin_page.product_item.filter(has_text=product_name)).not_to_be_visible()
    admin_page.logout_admin()
    reset()
