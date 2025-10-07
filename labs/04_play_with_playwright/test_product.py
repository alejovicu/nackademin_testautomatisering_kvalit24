import re
from playwright.sync_api import Page, expect

APP_URL = "http://localhost:5173"
admin_username = "test_user"
admin_password = "testtest123"


def admin_login(page: Page):
    page.goto(APP_URL, wait_until="networkidle")
    page.get_by_placeholder("Username").fill(admin_username)
    page.get_by_placeholder("Password").fill(admin_password)
    page.get_by_role("button", name="Login").click()
    # Om du vill asserta välkomsttexten:
    # expect(page.get_by_text(re.compile(r"Welcome,\s*test_user!"))).to_be_visible()


def add_product(page: Page, product_name: str):
    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name="Create Product").click()
    # vänta implicit genom att förvänta att den finns
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(1)


def product_exists(page: Page, product_name: str):
    expect(page.locator("div.product-item span", has_text=product_name).first).to_be_visible()


def remove_product(page: Page, product_name: str):
    row = page.locator(".product-item", has_text=product_name)
    row.locator(".product-item-button").click()
    # Bekräfta att raden försvann
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(0)


# -------- Tests --------

def test_admin_edit_product(page: Page):
    admin_login(page)
    product_name = "Test Product"
    add_product(page, product_name)
    product_exists(page, product_name)

    remove_product(page, product_name)

    # Bekräfta att produkten inte längre finns
    if page.locator('div.product-item span', has_text=product_name).count() == 0:
        print(f"Product '{product_name}' has been successfully removed.")
    

    #row = page.locator(".product-item", has_text=product_name).first
    #row.locator(".product-item-button").click()



