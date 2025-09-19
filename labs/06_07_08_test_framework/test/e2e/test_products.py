from playwright.sync_api import Page, expect
from facade.admin import AdminFacade
from models.ui.admin import AdminPage
import time

def test_add_product_to_catalog(page: Page):

    # GIVEN I AM AN ADMIN USER
    admin_page = AdminPage(page)
    admin_facade = AdminFacade(page)

    admin_facade.login_via_token()

    # WHEN I ADD A PRODUCT TO THE CATALOG
    new_product = f"product_{int(time.time())}"

    # Wait for product grid to appear on page
    admin_page.admin_grid_products.first.wait_for(state="attached", timeout=10000)

    count_before_adding = admin_page.get_current_product_count()
    admin_page.create_product(new_product)

    # THEN THE PRODUCT IS AVAILABLE TO BE USED IN THE APP
    expect(admin_page.admin_grid_products.nth(-1)).to_contain_text(new_product)
    expect(admin_page.admin_grid_products).to_have_count(count_before_adding + 1, timeout=10000)


def test_remove_product_from_catalog(page: Page):

    # GIVEN I AM AN ADMIN USER
    admin_page = AdminPage(page)
    admin_facade = AdminFacade(page)

    admin_facade.login_via_token()

    # WHEN I REMOVE A PRODUCT FROM THE CATALOG
    #Add product via API
    new_product_name = f"product_{int(time.time())}"
    new_product = admin_facade.create_product_for_test_via_api(new_product_name)
    count_before_removing = admin_page.get_current_product_count()

    # Delete product
    deleted_product = admin_page.delete_product_by_name(new_product)

    # THEN THE PRODUCT SHOULD NOT BE LISTED IN THE APP TO BE USED
    expect(deleted_product).to_have_count(0) # Check that product with that name does not exist anymore
    expect(admin_page.admin_grid_products).to_have_count(count_before_removing - 1, timeout=10000)