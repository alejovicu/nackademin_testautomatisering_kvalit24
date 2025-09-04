# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app


from playwright.sync_api import Page, expect
import time

USERNAME = "admin"
PASSWORD = "admin123"
PRODUCT_NAME = "Headphones"
BASEURL = "http://localhost:5173"


def test_admin_add_product(page: Page):
    
    page.goto(BASEURL)
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()


    page.get_by_placeholder("Product Name").fill(PRODUCT_NAME)
    page.get_by_role("button", name="Create Product").click()

    expect(page.get_by_text(PRODUCT_NAME)).to_be_visible()

    time.sleep(5)


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used

def test_admin_remove_product(page: Page):
    page.goto(BASEURL)
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()


    page.get_by_text(PRODUCT_NAME).locator("..").get_by_role("button", name="Delete").click()
    
    expect(page.get_by_text(PRODUCT_NAME)).not_to_be_visible()
    time.sleep(5)