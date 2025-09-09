
class ProductPage:
    def __init__(self, page):
        self.page = page
        self.button_add_product = page.get_by_text("Create Product")
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_delete_product = page.locator(".delete-product")


    def add_product(self, name):
        self.button_add_product.wait_for(state="visible", timeout=5000)
        self.input_product_name.fill(name)
        self.button_add_product.click()


    def delete_product(self, name):
        self.page.locator(".product-item").filter(
            has=self.page.locator(f"span:text('{name}')")
        ).locator("button.product-item-button").click()

