from playwright.sync_api import Page
from models.ui.admin import AdminPage
from models.ui.home import HomePage
import libs.utils


def test_add_product_to_catalog(page: Page):
    # Navigate to the admin page
    admin_page = AdminPage(page)
    admin_page.navigate()
    admin_page.login_as_admin()  # Logs in as an admin user

    # Add a product to the catalog
    product_name = libs.utils.generate_string_with("Product_")
    admin_page.create_product(product_name)

    # Verify the product is listed in the catalog
    assert product_name in admin_page.get_current_product_list()


def test_remove_product_from_catalog(page: Page):
    # Navigate to the admin page
    admin_page = AdminPage(page)
    admin_page.navigate()
    admin_page.login_as_admin()  # Logs in as an admin user

    # Add a product to ensure it exists
    product_name = libs.utils.generate_string_with("Product_")
    admin_page.create_product(product_name)

    # Remove the product from the catalog
    admin_page.delete_product_by_name(product_name)

    # Verify the product is no longer listed in the catalog
    assert product_name not in admin_page.get_current_product_list()