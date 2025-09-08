import re
import time
import pytest
from playwright.sync_api import Page, expect, sync_playwright

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()

'''@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)  # 👈 See browser
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    time.sleep(30000)
    context.close()'''


#Given I am an admin user​
#When I add a product to the catalog​
#Then The product is available to be used in the app

app_url = "http://localhost:5173"
admin_username = "admin"
admin_password = "admin"

def login_as_admin(page: Page):
    page.goto(app_url)
    page.get_by_placeholder("Username").fill(admin_username)
    page.get_by_placeholder("Password").fill(admin_password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("products available")).to_be_visible()


def test_add_product(page: Page,product="choclate"):
    login_as_admin(page)
    page.get_by_placeholder("Product name").fill(product)
    page.get_by_role("button", name="Create Product").click()

    added_product=page.locator(".product-item", has_text= product)
    expect(page.get_by_text("products available")).to_be_visible()
    expect(added_product.nth(0)).to_be_visible()
   
  


def test_delete_product(page: Page, product="apples"):
    login_as_admin(page)
 
    product_items=page.locator(".product-item", has_text = product)
    product_items.nth(0).get_by_role("button", name="Delete").click()   #first matching product

    initial_count=product_items.count()

    expect(page.get_by_text("products available")).to_be_visible()
    expect (product_items).to_have_count(initial_count-1)
    #expect(page.locator(".product-item", has_text= product)).not_to_be_visible()

 
   


