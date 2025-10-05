

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:3000"
ADMIN_USER = "admin"
ADMIN_PASS = "password"

def login_as_admin(page: Page):
    page.goto(f"{BASE_URL}/login")
    page.fill("#username", ADMIN_USER)
    page.fill("#password", ADMIN_PASS)
    page.click("#login-button")
    expect(page.locator("#catalog-page")).to_be_visible()

def add_product(page: Page, product_name: str):
    page.click("#add-product-button")
    page.fill("#product-name-input", product_name)
    page.click("#save-product-button")
    expect(page.locator(f"text={product_name}")).to_be_visible()

def remove_product(page: Page, product_name: str):
    page.click(f"text={product_name} >> ../.. >> .delete-button")
    page.click("#confirm-delete-button")
    expect(page.locator(f"text={product_name}")).not_to_be_visible()

def test_add_product_to_catalog(page: Page):
    login_as_admin(page)
    add_product(page, "Test Product 1")

def test_remove_product_from_catalog(page: Page):
    login_as_admin(page)
    remove_product(page, "Test Product 1")





