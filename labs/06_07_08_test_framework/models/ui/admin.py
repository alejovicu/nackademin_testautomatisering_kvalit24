# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.button_add_product = page.get_by_text("Create Product")
        self.input_product_name = page.get_by_placeholder("Product name")
        self.product_items = page.locator(".product-item")

    def get_current_product_count(self):
        
        return self.product_items.count()

    def create_product(self,product_name):
        self.button_add_product.wait_for(state="visible", timeout=5000)
        self.input_product_name.fill(product_name)
        self.button_add_product.click()
        self.page.locator(".product-item", has_text=product_name).wait_for(state="visible", timeout=5000)

    def product_exists(self,product_name):
        product = self.page.locator(".product-item", has_text=product_name)
        return product.count() > 0

    def delete_product_by_name(self,product_name):
        product = self.page.locator(".product-item", has_text=product_name)
        delete_button = product.locator("button.product-item-button")
        delete_button.wait_for(state="visible", timeout=5000)
        delete_button.click()
        product.wait_for(state="detached", timeout=5000)
        