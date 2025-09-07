from playwright.sync_api import Page, expect

from models.home import HomePage
from models.admin_login import LoginPage
from models.admin_page import AdminPage



def test_add_product_to_catalog(page: Page):

    #Given I am an admin user
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.admin_login("nermin123", "nermin_123")


    # When I add a product to the catalog​
    product_page = AdminPage(page)
    product_page.navigate_to_create_product()
    product_page.add_product("Lemon")

    # Then The product is available to be used in the app
    expect(page.get_by_text("New product")).to_be_visible()
    

def test_remove_product_from_catalog(page: Page, product = "Lemon"):

    # Given I am an admin user​
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.admin_login("nermin123", "nermin_123")

    # When I remove a product from the catalog​
    admin_page = AdminPage(page)
    before_count = admin_page.count_products()
    admin_page.delete_product(product)
   

    # Then The product should not be listed in the app to be used
    expect(admin_page.products).to_have_count(before_count - 1)
    expect(page.get_by_text(product)).not_to_be_visible()
