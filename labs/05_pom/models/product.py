

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.input_create_product = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role("button", name="Create Product")

    def create_product(self, product):
        self.input_create_product.fill(product)
        self.button_create_product.click()

    def delete_product(self, product):
        #self.page.locator("div.product-item", has_text=product).get_by_role("button", name="Delete").click()
        product_row = self.page.locator(f".product-item:has(span:text('{product}'))")
        delete_button = product_row.get_by_role("button", name="Delete")
        delete_button.click()