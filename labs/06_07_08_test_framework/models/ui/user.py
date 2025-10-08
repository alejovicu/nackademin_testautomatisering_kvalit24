# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.product_items = page.locator(".product-item")
        self.add_buttons = page.get_by_role("button", name="Create Product")
        self.product_name_input = page.get_by_placeholder("Product Name")
        self.remove_buttons = page.get_by_role("button", name="Delete")
       

    def get_user_products(self):
        # return list of products added to the user
        products = []
        count = self.product_items.count()
        for i in range(count):
            products.append(self.product_items.nth(i).inner_text())
        return products

    def add_product_to_user(self, product_name):
        self.product_name_input.fill(product_name)
        self.add_buttons.click()
        self.page.wait_for_timeout(500)  # wait for the product to be added

    def remove_product_from_user(self, product_name):
        self.remove_buttons(product_name).click()
        self.page.wait_for_timeout(500)  # wait for the product to be removed