import re
from playwright.sync_api import Page, expect

####     RUN signup.py to add admin credentials     #### (Requires selenium)

# Test Data
username = "admin"
password = "admin123"
product_name = "Kalaspuffar"

## REQUIREMENT
# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app


def test_login_to_admin_page_and_add_product(page: Page):
    ### ACT AND ARRANGE

    # Login
    page.goto("http://localhost:5173/", wait_until="networkidle")
    page.fill('input[placeholder="Username"]', username)
    page.fill('input[placeholder="Password"]', password)
    page.click("button.button-primary:has-text('Login')")

    # Get current stock count
    current_stock_count = page.locator("div.product-item").count()

    # Fill out productform and submit
    page.fill('input[placeholder="Product Name"]', product_name)
    page.click("button:has-text('Create Product')")

    # Get post addition stock
    post_addition_stock = page.locator("div.product-item").count()

    ### ASSERT

    # Assert the stock has been increased by 1
    assert post_addition_stock == current_stock_count + 1

    # Assert product has been added
    fetch_product = page.locator("div.product-item > span").last
    expect(fetch_product).to_have_text(product_name)


## REQUIREMENT
# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used


def test_login_to_admin_page_and_remove_product(page: Page):
    ### ACT AND ARRANGE

    # Login
    page.goto("http://localhost:5173/", wait_until="networkidle")
    page.fill('input[placeholder="Username"]', username)
    page.fill('input[placeholder="Password"]', password)
    page.click("button.button-primary:has-text('Login')")

    # Get current stock count
    current_stock_count = page.locator("div.product-item").count()

    # Locate the product name and delete
    fetch_product = page.locator(
        "div.product-item", has=page.locator("span", has_text=product_name)
    ).last

    fetch_product.locator("button.product-item-button:has-text('Delete')").click()

    # Get post deletion stock count
    post_deletion_stock = page.locator("div.product-item").count()

    ### ASSERT

    # Assert stock contains 1 product less post deletion
    assert post_deletion_stock == current_stock_count - 1

    # Assert the product is no longer visible
    expect(page.locator(f"text={product_name}")).not_to_be_visible()
