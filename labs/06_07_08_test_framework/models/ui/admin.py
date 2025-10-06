class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_products = page.locator('.product-item')
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role('button', name='Create Product')

    def count_products(self):
        return self.admin_products.count()

    def create_product_by_api(self, product_name):
        # Fyll bara och klicka, ingen väntan
        self.input_product_name.fill(product_name)
        self.button_create_product.click()

    def delete_product_by_name_by_api(self, product_name):
        delete_product = self.admin_products.filter(has_text=product_name)
        delete_product.get_by_role("button", name="Delete").click()
