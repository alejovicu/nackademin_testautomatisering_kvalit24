from playwright.sync_api import Page, expect
from facade.admin import AdminFacade
from models.ui.admin import AdminPage
import time

username = "admin"
password = "admin123"

def test_add_product_to_catalog(page: Page):

    # GIVEN I AM AN ADMIN USER
    admin_page = AdminPage(page)
    admin_facade = AdminFacade(page)

    admin_facade.signup_and_login(username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()

    # WHEN I ADD A PRODUCT TO THE CATALOG
    new_product = f"product_{int(time.time())}"
    count_before_adding = admin_page.get_current_product_count()
    admin_page.create_product(new_product)

    # THEN THE PRODUCT IS AVAILABLE TO BE USED IN THE APP
    expect(admin_page.admin_grid_products.nth(-1)).to_contain_text(new_product)
    expect(admin_page.admin_grid_products).to_have_count(count_before_adding + 1)


def test_remove_product_from_catalog(page: Page):

    # GIVEN I AM AN ADMIN USER
    admin_page = AdminPage(page)
    admin_facade = AdminFacade(page)

    admin_facade.signup_and_login(username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()

    # WHEN I REMOVE A PRODUCT FROM THE CATALOG

    # Add product (to make test self-contained)
    new_product = f"product_{int(time.time())}"
    admin_page.create_product(new_product)

    # Delete product
    deleted_product = admin_page.delete_product_by_name(new_product)

    # THEN THE PRODUCT SHOULD NOT BE LISTED IN THE APP TO BE USED
    expect(deleted_product).to_have_count(0) #check that product with that name does not exist anymore (in this case, product-name is uniquely generated)