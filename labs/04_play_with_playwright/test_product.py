# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app


import requests
from playwright.sync_api import Page, expect

BASEURL = "http://127.0.0.1:8000"

USERNAME = "admin_test"
PASSWORD = "admin123"

PRODUCT_NAME = "Headphones"


def get_token(user_name: str, password: str) -> str:
    response = requests.post(
        f"{BASEURL}/api/auth/login",
        json={"username": user_name, "password": password},
    )
    response.raise_for_status()
    return response.json()["token"]

def create_product(token: str, product_name: str) -> int:
    response = requests.post(
        f"{BASEURL}/api/products",
        json={"name": product_name, "price": 100, "description": "Test product"},
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["id"]

def test_add_product(page: Page):
    token = get_token(USERNAME, PASSWORD)

    # Create product via API
    product_id = create_product(token, PRODUCT_NAME)

    # Go to the app
    page.goto(BASEURL)

    # Verify the product is visible in the UI
    product_locator = page.locator(f"text={PRODUCT_NAME}")
    expect(product_locator).to_be_visible()

    # Optionally, verify the product details page
    product_locator.click()
    expect(page.locator("h1")).to_have_text(PRODUCT_NAME)

    def test_add_product(page: Page):
    
    page.goto("http://localhost:5173/")
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button:has-text('Login')")
