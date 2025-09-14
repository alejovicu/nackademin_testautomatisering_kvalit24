# from playwright.sync_api import Page
# from models.login import LoginPage
# # complete imports

# # Given I am an admin user​
# # When I add a product to the catalog​
# # Then The product is available to be used in the app
# def test_add_product_to_catalog(page: Page):
#     # complete code
# # Given I am an admin user​
# # When I remove a product from the catalog​
# # Then The product should not be listed in the app to be used
# def test_remove_product_from_catalog(page: Page):
#     # complete code
import libs.utils
from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    home = HomePage(page)
    home.navigate()

    # Login as admin
    creds = libs.utils.get_admin_credentials()
    home.login(creds["username"], creds["password"])

    # Go to admin page
    admin_page = AdminPage(page)

    # Count before
    count_before = admin_page.get_current_product_count()

    # Create a new product
    product_name = libs.utils.generate_random_product_name()
    admin_page.create_product(product_name)

    # Count after should increase by 1
    count_after = admin_page.get_current_product_count()
    assert count_after == count_before + 1

    # Product should be visible in catalog
    assert page.locator(f".product-item:has-text('{product_name}')").is_visible()


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    home.navigate()

    # Login as admin
    creds = libs.utils.get_admin_credentials()
    home.login(creds["username"], creds["password"])

    # Go to admin page
    admin_page = AdminPage(page)

    # Create a product to delete
    product_name = libs.utils.generate_random_product_name()
    admin_page.create_product(product_name)

    # Ensure it exists
    assert page.locator(f".product-item:has-text('{product_name}')").is_visible()

    # Count before
    count_before = admin_page.get_current_product_count()

    # Delete the product
    admin_page.delete_product_by_name(product_name)

    # Count after should decrease by 1
    count_after = admin_page.get_current_product_count()
    assert count_after == count_before - 1

    # Product should no longer exist
    assert not page.locator(f".product-item:has-text('{product_name}')").is_visible()
