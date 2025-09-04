from playwright.sync_api import expect

class HomePage:
    def __init__(self, page, base_url="http://localhost:5173"):
        self.page = page
        self.base_url = base_url

    def navigate(self):
        self.page.goto(f"{self.base_url}/products")
        self.page.wait_for_load_state("networkidle")

    def add_product(self, name: str):
        self.page.get_by_placeholder("Product Name").fill(name)
        self.page.get_by_role("button", name="Create Product").click()

    def remove_product(self, name: str):
        row = self.page.get_by_text(name).locator("..")  # parent element
        row.get_by_role("button", name="Delete").click()

    def expect_product_listed(self, name: str):
        expect(self.page.get_by_text(name)).to_be_visible()

    def expect_product_not_listed(self, name: str):
        expect(self.page.get_by_text(name)).to_have_count(0)
