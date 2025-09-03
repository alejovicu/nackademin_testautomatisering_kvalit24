import re
from playwright.sync_api import Page, expect

product_name = "Saras Kalaspuffar"
username = "admin"
password = "1234"


def test_admin_add_product(page: Page):
    page.goto("http://localhost:5173/", wait_until="networkidle")

    page.fill("input[placeholder='Username']", username)
    page.fill("input[placeholder='Password']", password)
    page.click("button:has-text('Login')")
    page.wait_for_load_state("networkidle")

    expect(page.get_by_text("Welcome, admin!")).to_be_visible()

    product_containers = page.locator("div.product-grid > div.product-item > span")
    product_name_amount = page.locator(
        f"div.product-grid > div.product-item > span:has-text('{product_name}')"
    )  # If more of the same name
    amount_of_products_before = product_containers.count()
    amount_of_identical_names_before = product_name_amount.count()

    page.fill("input[placeholder='Product Name']", product_name)
    page.click("button:has-text('Create Product')")

    page.wait_for_load_state("networkidle")
    amount_of_products_after = product_containers.count()
    amount_of_identical_names_after = product_name_amount.count()
    assert (
        amount_of_products_after == amount_of_products_before + 1
    )  # To make sure product was added even if an identical product already existed (won't have this issue working with IDs rather than names)
    assert (
        amount_of_identical_names_after == amount_of_identical_names_before + 1
    )  # To make sure 1 product was added
    assert page.is_visible(f"text={product_name}")


def test_admin_delete_product(page: Page):
    page.goto("http://localhost:5173/", wait_until="networkidle")

    page.fill("input[placeholder='Username']", username)
    page.fill("input[placeholder='Password']", password)
    page.click("button:has-text('Login')")
    page.wait_for_load_state("networkidle")

    expect(page.get_by_text("Welcome, admin!")).to_be_visible()

    product_containers = page.locator("div.product-grid > div.product-item > span")
    amount_of_products_before = product_containers.count()

    last_product_container = page.locator(f"div:has-text('{product_name}')").last
    last_product_container.get_by_role("button", name="Delete").click()

    page.wait_for_load_state("networkidle")

    amount_of_products_after = product_containers.count()
    assert (
        amount_of_products_after == amount_of_products_before - 1
    )  # To make sure 1 product was removed
    assert not page.is_visible(
        f"text={product_name}"
    )  # To make sure no product has the name. Won't work if there already was a product that was named identically, but working with IDs there wouldn't be this issue
