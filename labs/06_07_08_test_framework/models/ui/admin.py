class AdminPage:
    def __init__(self, page):
        self.page = page
        self.header_main_title = page.get_by_text("Nackademin Course App")
        self.welcome_message = page.locator("h2:has-text('Welcome')")
        self.products_header = page.get_by_text("Products available:")
        self.add_product_header = page.get_by_role("h3", name="Add new product:")
        self.empty_product_list = page.get_by_role("p", name="No products available.")
        self.product_list = page.locator(".product-grid")
        self.product_item_in_list = page.locator(".product-item")
        self.input_add_product = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_text("Create Product")
        self.button_logout = page.get_by_role("button", name="Logout")

    def add_product(self, product):
        self.input_add_product.fill(product)
        self.button_create_product.click()

    def locate_latest_product_name(self):
        return self.page.locator(".product-item > span").last

    def delete_latest_product(self):
        latest_product = self.page.locator(".product-item").last
        delete_button = latest_product.locator(
            ".product-item-button", has_text="Delete"
        )
        delete_button.click()
