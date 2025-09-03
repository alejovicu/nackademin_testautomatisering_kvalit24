import re
import pytest
from datetime import datetime
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()
    # test_product.py


# Updated app URL and admin credentials
APP_URL = "http://localhost:5173"
ADMIN_USERNAME = "admin_dev"
ADMIN_PASSWORD = "pass_1234"


def login_as_admin(page: Page):
    """Login to the app as admin"""
    page.goto(APP_URL)
    # Fill login form (placeholders come from Login.jsx)
    page.get_by_placeholder("Username").fill(ADMIN_USERNAME)
    page.get_by_placeholder("Password").fill(ADMIN_PASSWORD)
    page.get_by_role("button", name="Login").click()

    # After login, admin should see Products section
    expect(page.get_by_text("Products available:")).to_be_visible()


def add_product(page: Page, product_name: str):
    """Add a product as admin"""
    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name="Create Product").click()

    # Verify product is listed
    product_item = page.locator(".product-item", has_text=product_name)
    expect(product_item).to_be_visible()


def delete_product(page: Page, product_name: str):
    """Delete a product as admin"""
    product_item = page.locator(".product-item", has_text=product_name)
    expect(product_item).to_be_visible()
    product_item.get_by_role("button", name="Delete").click()

    # Verify product is gone
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(0)


def test_admin_adds_product(page: Page, browser_name):
    """Test: Admin can add a new product"""
    login_as_admin(page)
    unique = datetime.now().strftime("%Y%m%d%H%M%S")
    product_name = f"Playwright Product {unique}"
    add_product(page, product_name)


def test_admin_removes_product(page: Page, browser_name):
    """Test: Admin can remove a product"""
    login_as_admin(page)
    unique = datetime.now().strftime("%Y%m%d%H%M%S")
    product_name = f"Temp Product {unique}"

    # Precondition: create a product
    add_product(page, product_name)

    # Then delete it
    delete_product(page, product_name)
