from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import libs.utils
import sys
import os
import pytest
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(dotenv_path=env_path)
# complete imports


@pytest.mark.order(1)
def test_setup_admin():
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL"))
    username = os.getenv("admin_username")
    password = os.getenv("admin_password")
    normal_user = "user83"
    normal_password = "pass83"
    course01 = os.getenv("product01")
    course02 = os.getenv("product02")
    course03 = os.getenv("product03")
    course04 = os.getenv("product04")
    user_api.signup(username, password)
    user_api.signup(normal_user, normal_password)
    token = user_api.login_token(username, password)
    admin_api.set_token(token)
    admin_api.create_product(course01)
    admin_api.create_product(course02)
    admin_api.create_product(course03)
    admin_api.create_product(course04)


@pytest.mark.order(2)
def test_add_product_to_catalog(page: Page):
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    product = "Java-programmering för nybörjare"
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    username = os.getenv("admin_username")
    password = os.getenv("admin_password")
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


@pytest.mark.order(3)
def test_remove_product_from_catalog(page: Page):
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    product_name = os.getenv("product04")
    # Given I am an admin user​
    username = os.getenv("admin_username")
    password = os.getenv("admin_password")
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


@pytest.mark.order(4)
def test_reset_data_admin():
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL"))
    username = os.getenv("admin_username")
    password = os.getenv("admin_password")
    course01 = os.getenv("product01")
    course02 = os.getenv("product02")
    course03 = os.getenv("product03")
    course04 = "Java-programmering för nybörjare"
    token = user_api.login_token(username, password)
    admin_api.set_token(token)
    admin_api.delete_product_by_name(course01)
    admin_api.delete_product_by_name(course02)
    admin_api.delete_product_by_name(course03)
    admin_api.delete_product_by_name(course04)
