import re
from playwright.sync_api import Page, expect

APP_URL = "http://localhost:5173"


def test_admin_add_product(page: Page):
    page.goto(APP_URL)

    # Login as admin
    page.fill('//input[@placeholder="Username"]', "admin")
    page.fill('//input[@placeholder="Password"]', "1234")
    page.click('//button[normalize-space()="Login"]')

    # Add product
    page.fill('//input[@placeholder="Product Name"]', "IT course")
    page.click('//button[normalize-space()="Create Product"]')

    # Assert: product is visible in the app
    expect(page.locator("body")).to_contain_text("IT course")


def test_admin_remove_product(page: Page):
    page.goto(APP_URL)

    # Login as admin
    page.fill('//input[@placeholder="Username"]', "admin")
    page.fill('//input[@placeholder="Password"]', "1234")
    page.click('//button[normalize-space()="Login"]')

    # Remove a product from the catalog
    product_item = page.locator("div.product-item", has_text="IT course")
    page.click('//button[normalize-space()="Delete"]')

    # Assert: product is not visible in the app
    expect(page.locator("body")).not_to_contain_text("IT course")
