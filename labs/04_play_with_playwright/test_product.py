import re
from playwright.sync_api import Page, expect

def test_log_in_admin(page:Page):
    username = "admin1"
    password = "1234"
    product = "new product"
    page.goto("http://localhost:5173/")

    # Given I am an admin user​
    page.get_by_placeholder('Username').fill(username)
    page.get_by_placeholder('Password').fill(password)
    page.get_by_role("button", name="Login").click()

    # When I add a product to the catalog​
    products = page.locator('.product-item')
    expect(products.first).to_be_visible()
    before_new_product = products.count()

    page.get_by_placeholder('Product Name').fill(product)
    page.get_by_role("button", name="Create Product").click()
    
    # Then The product is available to be used in the app
    products = page.locator('.product-item')
    expect(products).to_have_count(before_new_product + 1)
       
    
def test_delete_product(page:Page):
    username = "admin1"
    password = "1234"
    page.goto("http://localhost:5173/")

    # Given I am an admin user​
    page.get_by_placeholder('Username').fill(username)
    page.get_by_placeholder('Password').fill(password)
    page.get_by_role("button", name="Login").click()

    # When I remove a product from the catalog​
    products = page.locator('.product-item')
    expect(products.first).to_be_visible()
    before_new_product = products.count()

    products = page.locator(".product-grid .product-item")
    last_product = products.nth(-1)
    last_product.get_by_role("button", name="Delete").click()

    # Then The product should not be listed in the app to be used
    # 
    products = page.locator('.product-item')
    expect(products).to_have_count(before_new_product -1)
