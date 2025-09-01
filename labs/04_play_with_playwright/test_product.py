import re, time
from playwright.sync_api import sync_playwright, Page, expect

"""
Open app
Sign up a new user
Log in with user
create a product
Verify that the product appers in the list
Delete the product
Verify the deleted product
"""

def handle_dialog(dialog):
    dialog.accept() # Exempel: När en användare har skapat så dyker en ruta upp, "Användare är skapad"

APP_URL = "http://localhost:5173/"


def test_admin(page: Page):

    # Login
    username = "Test_admin"
    password = "Pass_12345"
    product = "Apple"
    product = "Apple"
    page.goto(APP_URL)
    page.on("dialog", handle_dialog)

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)

    page.get_by_role("button", name="Login").click()

    # Create product
    page.get_by_placeholder("Product Name").fill(product)
    page.get_by_role("button", name="Create Product").click()

    # Verify that the product appers in the list
    expect(page.get_by_text(product)).to_be_visible()

    # Delete product
    # Hitta raden som innehåller produkten
    product_row = page.get_by_text(product).locator("..")  # ".." betyder parent

    # Klicka på delete-knappen i samma rad
    product_row.get_by_role("button", name="Delete").click()

    page.wait_for_selector(f"text={product}", state="detached")
