class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_input_product_name = page.get_by_placeholder("Product Name")
        self.admin_btn_create = page.get_by_role("button", name="Create Product")
        self.product_items = page.locator("div.product-item")
        self.product_delete_buttons = page.locator("button.product-item-button")

    def get_current_product_count(self):
        return self.product_items.count()

    def create_product(self, product_name):
        self.admin_input_product_name.fill(product_name)
        self.admin_btn_create.click()

    def delete_product_by_name(self, product_name):
        row = self.page.locator(f"div.product-item:has-text('{product_name}')").first
        row.locator("button.product-item-button").click()
