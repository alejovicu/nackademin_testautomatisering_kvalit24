from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.admin import AdminPage


def test_add_product_to_catalog(page: Page):

    #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    home_page.navigate()
    login_page.admin_login()
    number_of_products_before = admin_page.count_products()
    admin_page.add_product()
    expect(admin_page.products).to_have_count(number_of_products_before + 1)




    # Given I am an admin user​
    # When I add a product to the catalog​
    # Then The product is available to be used in the app
    

def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    home_page.navigate()
    login_page.admin_login()
    number_of_products_before = admin_page.count_products()
    admin_page.remove_product()
    expect(admin_page.products).to_have_count(number_of_products_before - 1)