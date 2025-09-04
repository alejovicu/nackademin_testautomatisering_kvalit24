class AdminPage:
    def __init__(self, page):
        self.page = page
        self.product_item = page.locator(".product-item")
        self.input_product = page.get_by_placeholder("Product Name")
        self.button_create = page.get_by_text("Create Product")
        self.select_product = page.get_by_role("span")
        self.logout = page.get_by_role("button").and_(page.get_by_text("Logout"))

    def select_product(self, product):  # find product.
        self.product_item.filter(has_text=product)

    def create_product(self, product):  # add product.
        self.input_product.fill(product)
        self.button_create.click()

    def delete_product(self, product):  # remove product.
        remove_product = self.product_item.filter(has_text=product)
        remove_product.get_by_role("button").and_(
            remove_product.get_by_text("Delete")
        ).click()

    def logout_admin(self):
        self.logout.click()


# expect(locator).to_have_text("product").and_(locator.not_to_have_role("role"))
