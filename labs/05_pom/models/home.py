from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:5173/")


# 05-pom/models/home.py


class AdminPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def expect_admin_dashboard(self):
        # Admin view contains "Add new product:"
        expect(self.page.get_by_text("Add new product:")).to_be_visible()
        return self

    def add_product(self, product_name: str):
        self.page.get_by_placeholder("Product Name").fill(product_name)
        self.page.get_by_role("button", name="Create Product").click()
        # wait for the product to appear in the grid
        expect(
            self.page.locator(".product-grid").get_by_text(product_name)
        ).to_be_visible()

    def delete_product(self, product_name: str):
        # find the product-item that has the product_name and click its Delete button
        row = self.page.locator(".product-item", has_text=product_name).first
        expect(row).to_be_visible()
        row.get_by_role("button", name="Delete").click()
        # verify product removed
        expect(
            self.page.locator(".product-grid").get_by_text(product_name)
        ).to_have_count(0)
