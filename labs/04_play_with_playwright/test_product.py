import re
from playwright.sync_api import Page, expect
import re, time
from playwright.sync_api import sync_playwright, Page, expect


def handle_dialog(dialog):
    dialog.accept() 

APP_URL = "http://localhost:5173/"

def create_test_admin():
    username = "testare_arre"
    password = "testare_123"
    return username, password


def test_admin(page: Page):
    username, password = create_test_admin()
    product_name = "Banana"

    page.goto(APP_URL)
    page.on("dialog", handle_dialog)

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()



    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name="Create Product").click()

    expect(page.get_by_text(product_name)).to_be_visible()

   
    product_row = page.get_by_text(product_name).locator("..")  
    product_row.get_by_role("button", name="Delete").click()
    page.wait_for_selector(f"text={product_name}", state="detached")