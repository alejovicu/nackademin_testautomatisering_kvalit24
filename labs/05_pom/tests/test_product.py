from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage


product = "Test_course"

def test_add_product_to_catalog(page: Page):

    #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.navigate()
    login_page.navigate_to_signup()

    login_page.login("admin", "pass1234")

    #product = "Test_course"
    page.fill("input[placeholder='Product Name']", product)
    page.click("text=Create Product")

    # UI assert - check if product is visible
    expect(page.locator(f".product-item span:text('{product}')").first).to_be_visible()
    # Given I am an admin user​
    # When I add a product to the catalog​
    # Then The product is available to be used in the app

def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
    pass