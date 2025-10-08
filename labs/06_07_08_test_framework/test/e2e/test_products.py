from playwright.sync_api import Page, expect

# from models.login import LoginPage ???
## complete imports
from models.ui.home import HomePage
from models.ui.admin import AdminPage

import libs.utils


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    # Step 1: Login as admin
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login("admin", "admin")

    # Step 2: Go to admin page
    admin_page = AdminPage(page)

    # Step 3: Create a unique product
    product_name = libs.utils.generate_string_with_prefix("test_product")
    # expect(admin_page.product_lists.first).to_be_visible()
    count_before = admin_page.get_current_product_count()
    admin_page.create_product(product_name)

    # Step 4: Assert product count increased
    count_after = admin_page.get_current_product_count()
    assert count_after == count_before + 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    # Step 1: Login as admin
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login("admin", "admin")

    # Step 2: Go to admin page
    admin_page = AdminPage(page)

    # Step 3: Ensure product exists
    product_name = libs.utils.generate_string_with_prefix("test_product")
    admin_page.create_product(product_name)
    count_before = admin_page.get_current_product_count()

    # Step 4: Delete product
    admin_page.delete_product_by_name(product_name)

    # Step 5: Assert product count decreased
    count_after = admin_page.get_current_product_count()
    assert count_after == count_before - 1
