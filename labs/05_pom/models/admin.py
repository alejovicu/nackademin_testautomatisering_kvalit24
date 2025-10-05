from playwright.sync_api import expect  

class AdminPage:
    def __init__(self, page):
        self.page = page
        self.product_item = page.locator(".product-item")  # list of products
        self.input_product = page.get_by_placeholder("Product Name")
        self.button_create = page.get_by_role("button", name="Create Product")
        self.logout = page.get_by_role("button", name="Logout")

    def create_product(self, product: str):
        """Fill in the product name and click Create."""
        expect(self.input_product).to_be_visible()  # wait for input
        self.input_product.fill(product)
        expect(self.button_create).to_be_visible()  # wait for button
        self.button_create.click()

    def delete_product(self, product: str):
        """Find product and click Delete."""
        product_locator = self.product_item.filter(has_text=product)
        expect(product_locator).to_be_visible()
        delete_button = product_locator.get_by_role("button", name="Delete")
        delete_button.click()

    def logout_admin(self):
        expect(self.logout).to_be_visible()
        self.logout.click()
