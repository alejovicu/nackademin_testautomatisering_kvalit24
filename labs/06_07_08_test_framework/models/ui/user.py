class UserPage:
    def __init__(self, page):
        self.page = page

    def get_user_products(self):
        return self.page.locator('.user-product-item')

    def add_product_to_user(self, product_name):
        product = self.page.locator(f"text={product_name}")
        product.get_by_role("button", name="Add").click()

    def remove_product_from_user(self, product_name):
        product = self.page.locator(f"text={product_name}")
        product.get_by_role("button", name="Remove").click()
