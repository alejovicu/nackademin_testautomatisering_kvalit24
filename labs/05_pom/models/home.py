from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page
        self.input_product = self.page.locator("input[placeholder='Product Name']")
        self.button_create = self.page.locator("button:has-text('Create Product')")

    def navigate(self):
        self.page.goto("http://localhost:5173/")

    def add_product(self, name: str):
        self.input_product.fill(name)
        self.button_create.click()

    def assert_product_visible(self, name: str):
        expect(self.page.locator("div.product-item", has_text=name)).to_be_visible()

    def remove_product(self, name: str):
        self.page.locator("div.product-item", has_text=name).get_by_role(
            "button", name="Delete"
        ).click()

    def assert_product_not_visible(self, name: str):
        expect(self.page.locator("div.product-item", has_text=name)).to_have_count(0)
