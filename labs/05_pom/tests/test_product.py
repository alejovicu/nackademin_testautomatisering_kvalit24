from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage


def test_add_product_to_catalog(page: Page):

    #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.navigate()
    #login_page.navigate_to_signup()
    login_page.login_as_admin()
    # Given I am an admin user​
    # When I add a product to the catalog​
    # Then The product is available to be used in the app
    product_name="doll"
    home_page.add_product(product_name)
    expect(page.get_by_text(product_name)).to_be_visible()





def test_delete_product_from_catalog(page: Page):
    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.navigate()
    #login_page.navigate_to_signup()
    login_page.login_as_admin()
    product_name="sauce pan"
    home_page.add_product(product_name)
    expect(page.get_by_text(product_name)).to_be_visible()
    #now delete it
    home_page.delete_product(product_name)
    expect(page.get_by_text(product_name)).not_to_be_visible()