import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):

    page.goto("http://localhost:5173/")
    expect(page).to_have_title(re.compile("Course App"))

    username = "testuser"
    password = "testpassword"
    product_name = "Test Product"

    # Sign up
    page.click("button#signup")
    expect(page.locator("text= Signup")).to_be_visible()

    page.fill("//input[@placeholder='Username']", username)
    page.fill("//input[@placeholder='Password']", password)
    page.click("//button[text()='Sign Up']")

    # Log in
    page.click("//button[text()='Login']")
    page.fill("//input[@placeholder='Username']", username)
    page.fill("//input[@placeholder='Password']", password)
    page.click("//button[text()='Login']")

    expect(page.locator("text=Welcome, testuser!")).to_be_visible()

    # Create Product
    products_with_name_before = page.locator(
        f".product-item:has-text('{product_name}')")
    count_before = products_with_name_before.count()

    page.fill("//input[@placeholder='Product Name']", product_name)
    page.click("//button[text()='Create Product']")

    products_with_name_after = page.locator(
        f".product-item:has-text('{product_name}')")
    count_after = products_with_name_after.count()

    assert count_after == count_before + 1

    # Delete Product
    products_grid = page.locator(".product-grid")
    expect(products_grid.first).to_be_visible()

    products = products_grid.locator(".product-item")
    number_of_products_before = products.count()

    last_product = products.nth(-1)
    last_product.get_by_role("button", name="Delete").click()

    products_after = page.locator(".product-item")
    expect(products_after).to_have_count(number_of_products_before - 1)
