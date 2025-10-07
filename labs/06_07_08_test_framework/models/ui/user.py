# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.user_welcome_message = page.get_by_text("Welcome")
        self.user_products_title = page.get_by_text("Your products:")
        self.user_products = page.locator("div[style*='display: grid'] > div")
        self.user_add_product_button = page.get_by_role("button", name="Add product")

    def get_user_products(self):
        return self.user_products

    def add_product_to_user(self, product_name):
        self.user_add_product_button.click()
        product = self.page.locator("li", has_text=product_name)
        product.get_by_role("button", name="Add").click()

    def remove_product_from_user(self, product_name):
        self.user_products.filter(has_text=product_name).get_by_role("button", name="Delete").click()