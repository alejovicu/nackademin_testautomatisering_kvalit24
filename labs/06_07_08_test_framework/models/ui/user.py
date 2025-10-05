class UserPage:
    def __init__(self, page):
        self.page = page
        self.user_btn_add_product = page.locator('button:has-text("Add Product")')
        
    def get_user_products(self):
        try:
            self.page.wait_for_timeout(1000)
            products = self.page.locator('h3:has-text("Your Products:") ~ div > div').all()
            product_names = []
            for product in products:
                text = product.inner_text()
                if text and "Delete" in text:
                    name = text.replace("Delete", "").strip()
                    if name:
                        product_names.append(name)
            return product_names
        except:
            return []
    
    def add_product_to_user(self, product_name):
        self.user_btn_add_product.click()
        self.page.wait_for_timeout(1000)
        product_row = self.page.locator(f'li:has-text("{product_name}")')
        add_button = product_row.locator('button:has-text("Add")')
        add_button.click()
        self.page.wait_for_timeout(1000)
        self.page.locator('button:has-text("Close")').click()
        self.page.wait_for_timeout(500)
    
    def remove_product_from_user(self, product_name):
        product_div = self.page.locator(f'div:has-text("{product_name}")').filter(has=self.page.locator('button:has-text("Delete")')).first
        delete_button = product_div.locator('button:has-text("Delete")')
        delete_button.click()
        self.page.wait_for_timeout(1000)