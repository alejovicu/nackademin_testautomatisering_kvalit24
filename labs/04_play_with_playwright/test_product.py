import re
from playwright.sync_api import Page, expect
import pytest
import time


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()
APP_URL = "http://localhost:5173"
API_URL = "http://localhost:8000"
API_LOGIN_URL = f"{API_URL}/login"
API_PRODUCTS_URL = f"{API_URL}/products"


def test_signup_login_create_product_delete(page: Page):

    username = "Admin1"
    password = "AdminPassword"
    product = "Test_course"


    page.goto(APP_URL)
    time.sleep(0.5)  

    # Signup
    page.click("#signup")
    page.fill("input[placeholder='Username']", username)
    page.fill("input[placeholder='Password']", password)
    page.click("text=Sign Up")

    # Login
    page.click("text=Login")
    time.sleep(0.2)
    page.fill("input[placeholder='Username']", username)
    page.fill("input[placeholder='Password']", password)
    page.locator("button.button-primary", has_text="Login").click()
    time.sleep(0.5)

    # Add product
    page.fill("input[placeholder='Product Name']", product)
    page.click("text=Create Product")


    expect(page.locator(f".product-item span:text('{product}')").first).to_be_visible()


    request_context = page.context.request
    login_response = request_context.post(
        API_LOGIN_URL,
        data={"username": username, "password": password}
    )
    token = login_response.json()["access_token"]

    response = request_context.get(
        API_PRODUCTS_URL,
        headers={"Authorization": f"Bearer {token}"}
    )
    products = response.json()
    product_names = [p["name"] for p in products]
    assert product in product_names, f"Product '{product}' not found in backend."
    print(f"{product} found in backend! All products: {product_names}")

    # Delete product
    page.locator("div.product-item", has_text=product).get_by_role("button", name="Delete").click()
    expect(page.locator(f".product-item span:text('{product}')").first).to_be_hidden()

    # Backend assert - product deleted
    login_response = request_context.post(
        API_LOGIN_URL,
        data={"username": username, "password": password}
    )
    token = login_response.json()["access_token"]

    response = request_context.get(
        API_PRODUCTS_URL,
        headers={"Authorization": f"Bearer {token}"}
    )
    products = response.json()
    product_names = [p["name"] for p in products]
    assert product not in product_names
    print(f"{product} has been deleted successfully.")
