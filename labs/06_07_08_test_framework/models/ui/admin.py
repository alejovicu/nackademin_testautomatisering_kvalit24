# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.product_item = page.locator(".product-item")
        self.input_product = page.get_by_placeholder("Product Name")
        self.button_create = page.get_by_text("Create Product")
        self.select_product = page.get_by_role("span")
        self.logout = page.get_by_role("button").and_(page.get_by_text("Logout"))
        # complete admin view elements

    def get_current_product_count(self):
        # complete logic
        # return number of total products displayed
        pass

    def create_product(self, product_name):
        self.input_product.fill(product_name)
        self.button_create.click()

    def delete_product_by_name(self, product_name):
        remove_product = self.product_item.filter(has_text=product_name)
        remove_product.get_by_role("button").and_(
            remove_product.get_by_text("Delete")
        ).click()

    def logout_admin(self):
        self.logout.click()
