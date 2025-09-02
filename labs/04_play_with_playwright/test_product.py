# labs/04_play_with_playwright/test_product.py

import time
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5173"
USER = "admin"
PASS = "admin123"


def test_add_and_remove_product(page: Page):
    # === Given I am an admin user ===
    page.goto(f"{BASE_URL}/login")
    page.get_by_placeholder("Username").fill(USER)
    page.get_by_placeholder("Password").fill(PASS)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text(f"Welcome, {USER}")).to_be_visible()

    # === When I add a product to the catalog ===
    product_name = f"Playwright Item {int(time.time())}"
    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name="Create Product").click()

    # === Then the product is available to be used in the app ===
    expect(page.get_by_text(product_name)).to_be_visible()

    # === When I remove a product from the catalog ===
    row = page.locator(f"text={product_name}").locator("..")  # parent element
    row.get_by_role("button", name="Delete").click()

    # === Then the product should not be listed in the app ===
    expect(page.get_by_text(product_name)).to_have_count(0)
