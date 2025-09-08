# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

class AdminPage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator('.product-item')

        self.input_product_name = page.get_by_placeholder("Product Name")
        self.create_product_btn = self.page.get_by_role("button", name="Create Product")

    def navigate_to_create_product(self):
        self.page.goto("http://localhost:5173/")

    # Add product
    def add_product(self, product_name):
        self.input_product_name.fill(product_name)
        self.create_product_btn.click()

    def count_products(self):
        return self.page.locator("div.product-item").count()

    # Delete Product
    def delete_product(self, product):
        product_to_delete = self.page.get_by_text(product).locator("..")
        product_to_delete.locator("button.product-item-button").click()