import re
from playwright.sync_api import Page, expect


# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")
#     expect(page).to_have_title(re.compile("Playwright"))
#     expect(page.get_by_text("Get started")).to_be_visible()

def test_admin_add_product(page: Page):
    username = "admin"
    password = "123"
    product_name = "bord"
    
    page.goto("http://localhost:5173")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_placeholder("Product Name")).to_be_visible()

    num_of_products_before = page.locator(".product-item").count()

    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name="Create Product").click()


    expect(page.locator(".product-item")).to_have_count(num_of_products_before + 1)


def test_admin_remove_product(page: Page):
    username = "admin"
    password = "123"
    
    page.goto("http://localhost:5173")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_placeholder("Product Name")).to_be_visible()

    num_of_products_before = page.locator(".product-item").count()

    page.locator(".product-item").last.get_by_role("button", name="Delete").click()

    expect(page.locator(".product-item")).to_have_count(num_of_products_before - 1)






