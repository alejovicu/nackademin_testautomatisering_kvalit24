import libs.utils
import pytest
from models.api.user import UserAPI
from models.api.admin import AdminAPI


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog():  # complete code
    user_api = UserAPI("http://localhost:8000")
    admin_api = AdminAPI("http://localhost:8000")
    username = "Admin_user"
    password = "Automation53"
    admin_token = user_api.login_token(username, password)
    admin_api.set_token(admin_token)
    admin_api.create_product("New product")

    pass


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():  # complete code
    user_api = UserAPI("http://localhost:8000")
    admin_api = AdminAPI("http://localhost:8000")
    username = "Admin_user"
    password = "Automation53"
    admin_token = user_api.login_token(username, password)
    admin_api.set_token(admin_token)
    admin_api.delete_product_by_name("New product")

    pass
