import re
import requests
from playwright.sync_api import Page, expect
import random


APP_URL='http://localhost:5173'
API_URL='http://127.0.0.1:8000/products'

def test_add_product(page: Page):
    page.goto(APP_URL)
    page.get_by_placeholder('Username').fill('admin')
    page.get_by_placeholder('Password').fill('admin1234')
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder('Product Name').fill('Apple')
    page.get_by_role("button", name="Create Product").click()

    expect(page.get_by_text("Apple").first).to_be_visible()




def test_add_and_delete_product(page: Page):
    unique_name = f"Apple-{random.randint(1000,9999)}"

    page.goto(APP_URL)
    page.get_by_placeholder('Username').fill('admin')
    page.get_by_placeholder('Password').fill('admin1234')
    page.get_by_role("button", name="Login").click()

    page.get_by_placeholder('Product Name').fill(unique_name)
    page.get_by_role("button", name="Create Product").click()

    expect(page.get_by_text(unique_name).first).to_be_visible()

    delete_button = page.locator(".product-item", has_text=unique_name).locator(".product-item-button", has_text="Delete").first
    delete_button.wait_for(state="visible", timeout=5000)
    delete_button.click()

    expect(page.locator(".product-item", has_text=unique_name)).to_have_count(0)
