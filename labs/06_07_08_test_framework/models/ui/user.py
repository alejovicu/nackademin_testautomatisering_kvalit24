# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        # complete code

    def get_user_products(self):
        user_product = self.page.locator("div[style*='grid-template-columns'] > div").all_text_contents()
        
        return user_product

    
    def add_product_to_user(self, product_name):
        # complete code
        pass

    def remove_product_from_user(self, product_name):
        # complete code
        pass