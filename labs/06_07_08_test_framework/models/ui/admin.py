class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_input_product_name = page.locator('input[placeholder="Product Name"]')
        self.admin_btn_create_product = page.locator('button:has-text("Create Product")')
        
    def get_current_product_count(self):
        try:
            self.page.wait_for_timeout(1000)
            products = self.page.locator('.product-item').all()
            return len(products)
        except:
            return 0
    
    def create_product(self, product_name):
        self.admin_input_product_name.fill(product_name)
        self.admin_btn_create_product.click()
        self.page.wait_for_timeout(1500)
    
    def delete_product_by_name(self, product_name):
        product_container = self.page.locator(f'span:has-text("{product_name}")').locator('..')
        delete_button = product_container.locator('button:has-text("Delete")')
        delete_button.click()
        self.page.wait_for_timeout(1500)