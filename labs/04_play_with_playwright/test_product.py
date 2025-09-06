import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()


#Given I am an admin user​
#When I add a product to the catalog​
#Then The product is available to be used in the app

app_url = "http://localhost:5173"
admin_username = "admin"
admin_password = "admin"

def login_as_admin(page: Page):
    page.goto(app_url)
    page.get_by_placeholder("Username").fill(admin_username)
    page.get_by_placeholder("Password").fill(admin_password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("products available")).to_be_visible()


def test_add_product(page: Page,product="blue berries"):
    login_as_admin(page)
    page.get_by_placeholder("Product name").fill(product)
    page.get_by_role("button", name="Create Product").click()

    expect(page.get_by_text("products available")).to_be_visible()
    #expect(page.locator(".product-item", has_text= product)).first_to_be_visible()
    #expect(page.locator(".product-item", has_text= product)).to_have_count(1)


def test_delete_product(page: Page, product="Coca cola"):
    login_as_admin(page)
   #<button class="product-item-button">Delete</button>
    product_item=page.locator(".product-item", has_text = product)
    product_item.get_by_role("button", name="Delete").click()

    expect(page.get_by_text("products available")).to_be_visible()
    expect(page.locator(".product-item",has_text=product)).to_have_count(0)


