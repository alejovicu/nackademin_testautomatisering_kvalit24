import re
from playwright.sync_api import Page, expect


def test_setup_data(page: Page):
    username = "Admin_user"
    password = "Automation53"
    # adding test data.
    product_1 = "Apple"
    product_2 = "Blueberries"
    product_3 = "Coconut"

    page.goto("http://localhost:5173/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()

    page.get_by_placeholder("Product Name").fill(product_1)
    page.get_by_role("button", name=re.compile("Create product", re.IGNORECASE)).click()
    page.get_by_placeholder("Product Name").fill(product_2)
    page.get_by_role("button", name=re.compile("Create product", re.IGNORECASE)).click()
    page.get_by_placeholder("Product Name").fill(product_3)
    page.get_by_role("button", name=re.compile("Create product", re.IGNORECASE)).click()


def test_admin_add_product(page: Page):
    username = "Admin_user"
    password = "Automation53"
    product_name = "Banana"  # add product.
    page.goto("http://localhost:5173/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()
    product_list_1 = page.locator("div.product-item").count()
    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name=re.compile("Create product", re.IGNORECASE)).click()
    product_list_2 = page.locator("div.product-item").count()

    expect(page.locator(f"text={product_name}")).to_be_visible()
    assert product_list_2 == product_list_1 + 1


def test_admin_remove_product(page: Page):
    username = "Admin_user"
    password = "Automation53"
    product_name = "Blueberries"  # remove product.
    page.goto("http://localhost:5173/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()

    product_list_1 = page.locator("div.product-item").count()

    remove_product = page.locator("div.product-item").filter(has_text=product_name)
    remove_product.get_by_role(
        "button", name=re.compile("Delete", re.IGNORECASE)
    ).click()

    product_list_2 = page.locator("div.product-item").count()

    expect(page.locator(f"text={product_name}")).not_to_be_visible()
    assert product_list_2 == product_list_1 - 1


def test_reset_data(page: Page):
    username = "Admin_user"
    password = "Automation53"
    # adding test data.
    product_1 = "Apple"
    product_2 = "Banana"
    product_3 = "Coconut"

    page.goto("http://localhost:5173/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()
    remove_product = page.locator("div.product-item").filter(has_text=product_1)
    remove_product.get_by_role(
        "button", name=re.compile("Delete", re.IGNORECASE)
    ).click()
    remove_product = page.locator("div.product-item").filter(has_text=product_2)
    remove_product.get_by_role(
        "button", name=re.compile("Delete", re.IGNORECASE)
    ).click()
    remove_product = page.locator("div.product-item").filter(has_text=product_3)
    remove_product.get_by_role(
        "button", name=re.compile("Delete", re.IGNORECASE)
    ).click()
