from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
# complete imports

import libs.utils


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    login_page = HomePage(page)
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    product = "mobil"
    home_page.navigate()

    # Given I am an admin user​
    login_page.login('admin1', '1234')

    # When I add a product to the catalog​
    expect(admin_page.products.first).to_be_visible()
    before_new_product = admin_page.get_current_product_count()
    admin_page.create_product(product)

    # Then The product is available to be used in the app
    expect(admin_page.products).to_have_count(before_new_product + 1)


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    login_page = HomePage(page)
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    product = "mobil"
    home_page.navigate()

    # Given I am an admin user​
    login_page.login('admin1', '1234')

    expect(admin_page.products.first).to_be_visible()

    # When I remove a product from the catalog​
    before_new_product = admin_page.get_current_product_count()
    admin_page.delete_product_by_name(product)

    # Then The product should not be listed in the app to be used
    expect(admin_page.products).to_have_count(before_new_product - 1)