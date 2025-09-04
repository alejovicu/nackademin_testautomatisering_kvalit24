    
class AdminPage:
    def __init__(self, page):
        self.products = page.locator('.product-item')
        self.input_product_name = page.get_by_placeholder('Product Name')
        self.button_create_product = page.get_by_role("button", name="Create Product")


    def add_product(self, product):
        self.input_product_name.fill(product)
        self.button_create_product.click()

    def count_products(self):
        return self.products.count()
        
    def delete_product(self, product):
        product_to_delete = self.products.filter(has_text=product)
        product_to_delete.get_by_role("button", name = "Delete").click()

