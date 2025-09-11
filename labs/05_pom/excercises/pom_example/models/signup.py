class CatalogAdmin:
    def __init__(self, browser_page):
        self.browser_page = browser_page
        self.items = browser_page.locator("div.product-item")

        self.name_field = browser_page.get_by_placeholder("Product Name")
        self.add_button = browser_page.get_by_role("button", name="Create Product")

    def open_catalog(self):
        self.browser_page.goto("http://localhost:5173/")

    def create_item(self, name: str):
        self.name_field.fill(name)
        self.add_button.click()

    def total_items(self) -> int:
        return self.items.count()

    def remove_item(self, name: str):
        row = self.browser_page.get_by_text(name).locator("..")
        row.locator("button.product-item-button").click()