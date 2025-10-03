# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.header_title = page.get_by_text("Nackademin Course App")
        self.products_title = page.get_by_text("Your Products:")
        
        self.user_products = page.locator("div[style*='display: grid'] > div")
        

    def get_user_products(self):
        return self.user_products
        
        
    

    # def add_product_to_user(self, product_name):
        # product = self.page.locator(".product-item").filter(
            # has=self.page.locator(f"span:text('{product_name}')")
        # )
        # product.locator("button.add").wait_for(state="visible", timeout=5000).click()
        

    # def remove_product_from_user(self, product_name):
        # product = self.page.locator(".product-item").filter(
            # has=self.page.locator(f"span:text('{product_name}')")
        # )
        # product.locator("button.remove").wait_for(state="visible").click()