# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page

    def user_login(self, username, password):
        pass
    
    def get_user_products(self):
        # Get all product names from the user's product grid

        return self.page.locator("div[style*='grid-template-columns'] > div").all_text_contents()

    def add_product_to_user(self, product_name):
        pass

    def remove_product_from_user(self, product_name):
        pass