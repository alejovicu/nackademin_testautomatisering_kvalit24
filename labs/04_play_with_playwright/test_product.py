import re
from playwright.sync_api import Page, expect
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

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()
def handle_dialog(dialog):
    dialog.accept() # Exempel: När en användare har skapat så dyker en ruta upp, "Användare är skapad"

APP_URL = "http://localhost:5173/"

def create_test_admin():
    username = "admin"
    password = "admin"
    return username, password


def test_admin(page: Page):
    username, password = create_test_admin()
    product_name = "Banana"

    page.goto(APP_URL)
    page.on("dialog", handle_dialog)

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)

    page.get_by_role("button", name="Login").click()

#create product

    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name="Create Product").click()

#Verify that the product appers in the list
    expect(page.get_by_text(product_name)).to_be_visible()

    # Delete product
    # Hitta raden som innehåller produkten
    product_row = page.get_by_text(product_name).locator("..")  # ".." betyder parent

    # Klicka på delete-knappen i samma rad
    product_row.get_by_role("button", name="Delete").click()

    page.wait_for_selector(f"text={product_name}", state="detached")