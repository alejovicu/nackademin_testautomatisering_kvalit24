class AdminPage:    

    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        #complete admin view elements
        self.products = page.locator('.product-item')
        self.input_product_name = page.get_by_placeholder('Product Name')
        self.button_create_product = page.get_by_role("button", name="Create Product")

    def get_current_product_count(self):
        # complete logic
        # return number of total products displayed
        return self.products.count()

    def create_product(self,product_name):
        # complete logic
        self.input_product_name.fill(product_name)
        self.button_create_product.click()

    def delete_product_by_name(self,product_name):
        # complete logic
        product_to_delete = self.products.filter(has_text=product_name)
        product_to_delete.get_by_role("button", name = "Delete").click()

    