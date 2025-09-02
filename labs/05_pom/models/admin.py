class AdminPage:
    def __init__(self, page):
        self.page = page
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role('button',  name= 'Create Product' )
        self.products = page.locator('.product-item')

    def add_product(self):
        product = "Headset"

        self.input_product_name.fill(product)
        self.button_create_product.click()
    
    def count_products(self):
        return self.products.count()

    def remove_product(self):
        product = self.products.last
        product.get_by_role("button", name="Delete").click()
        

