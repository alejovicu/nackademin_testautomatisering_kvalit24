from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5173"
USERNAME = "monica"
PASSWORD = "pass_monica"


def login_as_admin(page: Page):
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.locator('button.button-primary, button:has-text("Login")').first.click()

    # Add product
    page.get_by_placeholder("Product Name").fill("Apple")
    page.get_by_role("button", name="Create Product").click()

    # Validate
    added_product = page.locator("span", has_text="Apple")
    expect(added_product).to_be_visible()
    expect(added_product).to_have_text("Apple")


def test_admin_delete_product(page: Page):
    # Login
    login_as_admin(page)

    # Delete
    product_item = page.locator(
        "div.product-item", has=page.get_by_text("Apple", exact=True)
    )
    delete_btn = product_item.get_by_role("button", name="Delete")
    delete_btn.click()

    # Validate
    expect(page.locator("body")).not_to_contain_text("Apple")
