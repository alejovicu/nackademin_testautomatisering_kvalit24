
class AdminPage:
    def __init__(self, page):
        self.page = page

        self.admin_grid_products = page.locator(".product-grid .product-item")
        self.admin_input_product_name = page.get_by_role("textbox", name="Product Name")
        self.admin_btn_add_product = page.get_by_role("button", name="Create Product")

    def get_current_product_count(self):
        return self.admin_grid_products.count()

    def create_product(self, product_name):
        self.admin_input_product_name.fill(product_name)
        self.admin_btn_add_product.click()

    def delete_product_by_name(self, product_name):
        self.page.locator(".product-item", has_text=product_name).get_by_role("button", name="Delete").click()
        deleted_product = self.page.locator(".product-grid .product-item").filter(has_text=product_name)
        return deleted_product