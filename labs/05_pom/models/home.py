from playwright.sync_api import Page, expect
import re

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "http://localhost:5173/"

    def navigate(self):
        self.page.goto(self.base_url, wait_until="networkidle")

    def add_product(self, product_name: str):
        product = self.page.locator(".product-grid .product-item")
        before = product.count()

        self.page.get_by_role("textbox", name="Product Name").fill(product_name)
        self.page.get_by_role("button", name=re.compile("Create Product", re.I)).click()

        # Kolla att produkten finns
        expect(self.page.locator(".product-grid .product-item").nth(-1)).to_contain_text(product_name)
        expect(product).to_have_count(before + 1)

    def delete_product(self, product_name: str):
        self.page.locator(".product-item", has_text=product_name).get_by_role("button", name="Delete").click()
        gone = self.page.locator(".product-grid .product-item").filter(has_text=product_name)
        expect(gone).to_have_count(0)
