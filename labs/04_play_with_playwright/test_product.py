import re
import time
from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    # just testing so it even runs before i touch my app
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()

# ---------------------- CONFIG STUFF ------------------------------
BASE_URL = "http://localhost:5173/"
admin_user = "admin"
admin_pass = "admin123"
random_product = f"prod_{int(time.time())}"

# ---------------------- SIGN UP FUNC ------------------------------
def do_signup(page: Page, username, password):
    page.locator("#signup").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    # click signup and then back to login
    page.get_by_role("button", name="Sign Up").click()
    page.get_by_role("button", name="Login").click()

# ---------------------- LOGIN FUNC ------------------------------
def do_login(page: Page, username, password):
    # classic login flow
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

# ---------------------- ADD PRODUCT ------------------------------
def add_new_product(page: Page, product_name):
    # get how many products before
    current_items = page.locator(".product-grid .product-item")
    before_count = current_items.count()

    # type in product name
    page.get_by_role("textbox", name="Product Name").fill(product_name)
    # press the button
    page.get_by_role("button", name=re.compile("Create Product", re.I)).click()

    # verify product appear last
    expect(page.locator(".product-grid .product-item").nth(-1)).to_contain_text(product_name)
    # verify number of items increased
    expect(current_items).to_have_count(before_count + 1)

# ---------------------- DELETE PRODUCT ------------------------------
def remove_product(page: Page, product_name):
    page.locator(".product-item", has_text=product_name).get_by_role("button", name="Delete").click()
    gone = page.locator(".product-grid .product-item").filter(has_text=product_name)
    expect(gone).to_have_count(0)

# ---------------------- MAIN TEST ------------------------------
def test_admin_can_add_and_delete(page: Page):
    # go to homepage first
    page.goto(BASE_URL, wait_until="networkidle")

    do_signup(page, admin_user, admin_pass)

    do_login(page, admin_user, admin_pass)

    # admin should see create btn
    expect(page.get_by_role("button", name=re.compile("Create Product", re.I))).to_be_visible()

    # test adding new product
    add_new_product(page, random_product)

    # then test deleting it
    remove_product(page, random_product)