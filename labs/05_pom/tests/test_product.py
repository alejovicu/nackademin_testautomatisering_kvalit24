
from playwright.sync_api import Page, expect
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
import uuid


def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    # Generate unique admin username
    username = f"admin_{uuid.uuid4().hex[:6]}"

    # Given I am an admin user
    home_page.navigate()
    login_page.navigate_to_signup()
    signup_page.signup(username, "password123")
    login_page.login(username, "password123")

    # When I add a product to the catalog
    page.locator("#add-product").click()
    page.locator("#product-name").fill("Testprodukt")
    page.locator("#product-price").fill("199")
    page.locator("#save-product").click()

    # Then The product is available to be used in the app
    product_list = page.locator("#product-list")
    expect(product_list).to_contain_text("Testprodukt")


def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Use known existing admin (seeded or created in previous test)
    home_page.navigate()
    login_page.login("admin", "password123")

    # Given I am an admin user
    # When I remove a product from the catalog
    # (better locator: avoid hardcoding ID)
    page.get_by_role("button", name="Delete Testprodukt").click()

    # Then The product should not be listed
    product_list = page.locator("#product-list")
    expect(product_list).not_to_contain_text("Testprodukt")
