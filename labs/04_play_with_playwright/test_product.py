import re
from playwright.sync_api import Page, expect
import time

# REQUIREMENTS
# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used

#SET UP
BASE_URL = "http://localhost:5173/"
username = "admin"
password = "admin123"
new_product = f"product_{int(time.time())}"

# SIGN UP
def signup(page: Page, username, password):
    page.locator('#signup').click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign Up").click()
    page.get_by_role("button", name="Login").click()

# LOG IN
def login(page: Page, username, password):
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

# ADD PRODUCT
def add_product(page: Page, new_product):
    product = page.locator(".product-grid .product-item")
    count_before_adding = product.count()
    page.get_by_role("textbox", name="Product Name").fill(new_product)
    page.get_by_role("button", name="Create Product").click()
    expect(page.locator(".product-grid .product-item").nth(-1)).to_contain_text(new_product)
    expect(product).to_have_count(count_before_adding + 1)

# DELETE PRODUCT
def delete_product(page: Page, new_product):
    page.locator(".product-item", has_text=new_product).get_by_role("button", name="Delete").click()
    deleted_product = page.locator(".product-grid .product-item").filter(has_text=new_product)
    expect(deleted_product).to_have_count(0)

# RUN TESTS
def test_admin_add_delete(page: Page):
    page.goto(BASE_URL, wait_until='networkidle')
    signup(page, username, password) # REMOVE WHEN NOT NEEDED
    login(page, username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible() # ADMIN SHOULD SEE CREATE BUTTON
    add_product(page, new_product)
    delete_product(page, new_product)