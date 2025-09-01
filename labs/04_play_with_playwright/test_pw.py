from playwright.sync_api import sync_playwright, Page, expect
import pytest
import time


#URL variables
APP_URL = "http://localhost:5173"
API_URL = "http://localhost:8000"
API_LOGIN_URL = f"{API_URL}/login"
API_PRODUCTS_URL = f"{API_URL}/products"


def test_signup_login_create_product_delete():

    #my variables
    username = "admin"
    password = "pass1234"
    product = "Test_course"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(APP_URL)

        # Signup
        page.click("#signup")
        page.fill("input[placeholder='Username']", username)
        page.fill("input[placeholder='Password']", password)
        page.click("text=Sign Up")

        # Login ( Here I also wanted to try click login button a different way )
        page.click("text=Login")
        time.sleep(0.2)
        page.fill("input[placeholder='Username']", username)
        page.fill("input[placeholder='Password']", password)
        page.locator("button.button-primary", has_text="Login").click()

        # Add product
        page.fill("input[placeholder='Product Name']", product)
        page.click("text=Create Product")

        # UI assert - check if product is visible
        expect(page.locator(f".product-item span:text('{product}')").first).to_be_visible()

        # Asser product in backend
        request_context = p.request.new_context()
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

        # Delete product and assert product is not found - UI
        #page.locator(f"//div[@class='product-item'][span[text()='{product}']]//button[text()='Delete']").click()
        # ----  Above works aswell, but the one below is cleaner and easier to read.
        page.locator("div.product-item", has_text=product).get_by_role("button", name="Delete").click()
        expect(page.locator(f".product-item span:text('{product}')").first).to_be_hidden()

        # Assert that product has been deleted
        request_context = p.request.new_context()
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
        print(f"{product} Has been deleted.")
        #pytest -s to see it more verbose



        browser.close()