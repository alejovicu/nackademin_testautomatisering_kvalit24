from playwright.sync_api import Page
import libs.utils
import pytest
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os
# from dotenv import load_dotenv


def test_add_product_to_catalog():  # complete code
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL"))
    username = "Admin_user"
    password = "Automation53"
    # Given I am an admin user​
    admin_token = user_api.login_token(username, password)
    admin_api.set_token(admin_token)
    # When I add a product to the catalog​
    new_product_added = admin_api.create_product("New product")
    new_product_name = admin_api.get_product_by_name("New product")
    # Then The product is available to be used in the app
    assert new_product_name == "New product"
    assert new_product_added.status_code == 200


def test_remove_product_from_catalog():  # complete code
    user_api = UserAPI(os.getenv("BACKEND_URL"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL"))
    username = "Admin_user"
    password = "Automation53"
    # Given I am an admin user​
    admin_token = user_api.login_token(username, password)
    admin_api.set_token(admin_token)
    # When I remove a product from the catalog​
    delete_product = admin_api.delete_product_by_name("New product")
    # Then The product should not be listed in the app to be used
    removed_product = admin_api.get_product_by_name("New product")
    assert delete_product.status_code == 200
    assert removed_product == None
