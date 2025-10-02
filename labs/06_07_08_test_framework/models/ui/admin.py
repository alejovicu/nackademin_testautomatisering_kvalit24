class AdminPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.get_by_placeholder('Product Name')
        self.add_btn = page.get_by_role('button', name='Create Product')
        self.items = page.locator('.product-item')

    def get_current_product_count(self):
        return self.items.count()

    def create_product(self, product_name):
        self.name_input.fill(product_name)
        self.add_btn.click()

    def delete_product_by_name(self, product_name):

        product = self.page.locator('.product-item', has_text=product_name)
        product.locator('.product-item-button').click()