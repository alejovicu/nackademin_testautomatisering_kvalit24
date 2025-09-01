import re
from playwright.sync_api import Page, expect, sync_playwright
import uuid

def handle_dialog(dialog):
    dialog.accept()

APP_URL = "http://localhost:5173/"

def create_test_admin():
    username = "nahom_admin"
    password = "1234"
    return username, password

def test_create_new_user_and_add_and_delete_a_product(page: Page):
    """
    Full end-to-end test with Playwright
    1. Open the app
    2. Sign up a new user
    3. Login with the user
    4. Create a product
    5. Verify that the product appears in the list
    6. Delete the product
    7. Verify deletion
    """

    username, password = create_test_admin()

    product = f"kaffe-{uuid.uuid4().hex[:4]}"

    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page: Page = context.new_page()

    page.goto(APP_URL)

    # # Create admin
    # page.get_by_role("button", name="Sign Up").click()

    # # Type in value in create user
    # page.get_by_placeholder("Username").fill(username)
    # page.get_by_placeholder("Password").fill(password)

    # # Press signup-button
    # page.get_by_role("button", name="Sign Up").click()

    # Login admin
    page.get_by_role("button", name="Login").click()

    # Type in login details
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)

    # Press login-button
    page.get_by_role("button", name="Login").click()

    # Create product
    expect(page.get_by_placeholder("Product Name")).to_be_visible()

    page.get_by_placeholder("Product Name").fill(product)
    page.get_by_role("button", name="Create Product").click()

    # Verify that the product appears in the list
    expect(page.get_by_text(product)).to_be_visible()

    # Radera produkt
    page.once("dialog", handle_dialog)
    page.get_by_role("button", name="Delete").click()
    expect(page.get_by_text(product, exact=True)).to_have_count(0)




