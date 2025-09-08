from playwright.sync_api import Page, expect
from facade.admin import AdminFacade
from models.ui.admin import AdminPage
import time

username = "admin"
password = "admin123"

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    admin_page = AdminPage(page)
    admin_facade = AdminFacade(page)

    new_product = f"product_{int(time.time())}"

    admin_facade.signup_and_login(username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()

    # Add product + assert
    count_before_adding = admin_page.create_product(new_product)
    expect(admin_page.admin_grid_products.nth(-1)).to_contain_text(new_product)
    expect(admin_page.admin_grid_products).to_have_count(count_before_adding + 1)


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    admin_page = AdminPage(page)
    admin_facade = AdminFacade(page)

    new_product = f"product_{int(time.time())}"

    admin_facade.signup_and_login(username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()

    # Add product + assert
    admin_page.create_product(new_product)

    # Delete product + assert
    deleted_product = admin_page.delete_product_by_name(new_product)
    expect(deleted_product).to_have_count(0)