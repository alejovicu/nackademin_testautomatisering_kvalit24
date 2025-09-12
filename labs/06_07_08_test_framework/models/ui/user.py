# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.user_headline_products = page.get_by_role("heading", name="Your Products:")
        self.products_container = page.locator("div[style*='display: grid'][style*='grid-template-columns']")
        self.product_items = self.products_container.locator("div")

    def get_welcome_message(self, username):
        return self.page.get_by_text(f"Welcome, {username}!")

    def get_user_products(self):
        # loop through list of items and return list pf product names
        # strip removes whitespaces in the names
        return [p.strip() for p in self.product_items.all_inner_texts()]

    def add_product_to_user(self, product_name):
        # complete code
        pass

    def remove_product_from_user(self, product_name):
        # complete code
        pass