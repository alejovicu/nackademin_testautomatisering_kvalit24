from playwright.sync_api import Page, expect

from models.login import LoginPage
from models.home import HomePage
from models.admin import AdminPage

def test_add_product_to_catalog(page: Page):

    login_page = LoginPage(page)
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    home_page.navigate()

    # Given I am an admin user​
    login_page.login('admin1', '1234')
    
    # When I add a product to the catalog​
    expect(admin_page.products.first).to_be_visible()
    before_new_product = admin_page.count_products()
    admin_page.add_product('mobil')
    
    # Then The product is available to be used in the app
    expect(admin_page.products).to_have_count(before_new_product + 1)

def test_remove_product_from_catalog(page: Page):

    login_page = LoginPage(page)
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    home_page.navigate()

    # Given I am an admin user​
    login_page.login('admin1', '1234')

    # When I remove a product from the catalog​
    before_new_product = admin_page.count_products()
    expect(admin_page.products.first).to_be_visible()
    admin_page.delete_product("mobil")
    
    # Then The product should not be listed in the app to be used
    expect(admin_page.products).to_have_count(before_new_product - 1)
    