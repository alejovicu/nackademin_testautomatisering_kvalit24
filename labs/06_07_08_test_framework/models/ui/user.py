# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.user_headline_products = page.get_by_role("heading", name="Your Products:")

    def get_welcome_message(self, username):
        return self.page.get_by_text(f"Welcome, {username}!")

    def get_user_products(self):
        # complete code
        pass

    def add_product_to_user(self, product_name):
        # complete code
        pass

    def remove_product_from_user(self, product_name):
        # complete code
        pass