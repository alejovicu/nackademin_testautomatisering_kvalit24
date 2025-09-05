import re
from playwright.sync_api import Page, expect


def test_admin_add_product(page: Page):
    # --- LOGIN ---
    page.goto("http://localhost:5173/")
    page.wait_for_load_state("networkidle")

    page.fill("input[placeholder='Username']", "admin_user")
    page.fill("input[placeholder='Password']", "pass_1234")
    page.click("button:has-text('Login')")

    page.wait_for_load_state("networkidle")
    # --ADD PRODUCT---
    page.wait_for_selector("input[placeholder='Product Name']")
    page.fill("input[placeholder='Product Name']", "peach")
    page.click("button:has-text('Create Product')")

    page.wait_for_load_state("networkidle")

    # --- VALIDATE THE PRODUCT IS ADDED ---
    added_product = page.locator("span:has-text('peach')")
    expect(added_product).to_be_visible()
    expect(added_product).to_have_text("peach")


def test_admin_delete_product(page: Page):
    # --- Login ---
    page.goto("http://localhost:5173/")
    page.wait_for_load_state("networkidle")

    page.fill("input[placeholder='Username']", "admin_user")
    page.fill("input[placeholder='Password']", "pass_1234")
    page.click("button:has-text('Login')")

    # --- DELETE PRODUCT ---
    product_item = page.locator(
        "div.product-item", has=page.get_by_text("peach", exact=True)
    )
    delete_btn = product_item.get_by_role("button", name="Delete")
    delete_btn.click()

    # --- VALIDATE PRODUCT IS DELETED ---
    expect(page.locator("body")).not_to_contain_text("peach")
