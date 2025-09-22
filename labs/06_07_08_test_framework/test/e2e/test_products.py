from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils


def test_add_product_to_catalog(page: Page):
    # Navigate to the home page
    home_page = HomePage(page)
    home_page.navigate()

    # Log in as an admin user
    home_page.login(username="DB_admin", password="admin123")

    # Admin-specific functionality
    admin_page = AdminPage(page)

    # Add a product to the catalog
    product_name = libs.utils.generate_string_with_prefix("Product_")  # Updated function name
    admin_page.create_product(product_name)

    # Verify the product is listed in the catalog
    product_list = admin_page.get_current_product_list()
    assert product_name in product_list


def test_remove_product_from_catalog(page: Page):
    # Navigate to the home page
    home_page = HomePage(page)
    home_page.navigate()

    # Log in as an admin user
    home_page.login(username="DB_admin", password="admin123")

    # Admin-specific functionality
    admin_page = AdminPage(page)

    # Add a product to ensure it exists
    product_name = libs.utils.generate_string_with_prefix("Product_")
    admin_page.create_product(product_name)

    # Remove the product from the catalog
    admin_page.delete_product_by_name(product_name)

    # Wait for the product grid to stabilize
    page.wait_for_timeout(1000)  # Wait for 1 second

    # Verify the product is no longer listed in the catalog
    product_list = admin_page.get_current_product_list()
    assert product_name not in product_list