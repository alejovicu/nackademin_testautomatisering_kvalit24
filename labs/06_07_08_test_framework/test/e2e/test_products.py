from playwright.sync_api import Page

from models.ui.user import UserPage
from models.ui.admin import AdminPage
from models.ui.home import HomePage    
from libs.utils import generate_string_with_prefix


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):

    admin_username = "test_user"
    admin_password = "testtest123"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(admin_username, admin_password)
   

    admin_page = AdminPage(page)
    product_name = generate_string_with_prefix("Product", 5)

    before_add= admin_page.get_current_product_count()
    admin_page.create_product(product_name)

    after_add = admin_page.get_current_product_count()

    assert after_add == before_add + 1, f"Expected product count to be {before_add + 1}, but got {after_add}"



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):

    admin_username = "test_user"
    admin_password = "testtest123"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(admin_username, admin_password)

    admin_page = AdminPage(page)
    product_name = generate_string_with_prefix("Product", 5)

    # First, add a product to ensure there is something to delete
    admin_page.create_product(product_name)
    before_delete = admin_page.get_current_product_count()

    # Now, delete the product
    admin_page.delete_product_by_name(product_name)
    after_delete = admin_page.get_current_product_count()

    assert after_delete == before_delete - 1, f"Expected product count to be {before_delete - 1}, but got {after_delete}"
    