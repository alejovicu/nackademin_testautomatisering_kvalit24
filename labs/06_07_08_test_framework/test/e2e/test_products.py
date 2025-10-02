#from playwright.sync_api import Page
#from models.login import LoginPage
# complete imports

#import libs.utils


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
#def test_add_product_to_catalog(page: Page):
    # complete code


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
#def test_remove_product_from_catalog(page: Page):
    # complete code

from playwright.sync_api import Page
import libs.utils
from models.ui.home import HomePage
from models.ui.admin import AdminPage

def test_admin_can_create_product(page: Page):
    product_name = libs.utils.generate_string_with_prefix("product")

    home = HomePage(page)
    home.navigate()
    home.login("admin_qa", "pass_5678")

    admin = AdminPage(page)
    admin.create_product(product_name)

    product_item = page.locator(f"text={product_name}")
    assert product_item.is_visible()

def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin_qa", "pass_5678")

    admin = AdminPage(page)

    product_name = libs.utils.generate_string_with_prefix("product")
    admin.create_product(product_name)

    product_item = page.locator(f"text={product_name}")
    assert product_item.is_visible()

    admin.delete_product_by_name(product_name)

    assert page.locator(f"text={product_name}").count() == 0
