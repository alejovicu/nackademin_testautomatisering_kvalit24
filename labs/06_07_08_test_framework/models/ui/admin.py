# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.input_create_product = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role("button", name="Create Product")
        self.product_cards = page.locator(".product-item")


    def get_current_product_count(self):
        return self.product_cards.count()
    

    def create_product(self, product):
        # complete logic
        self.input_create_product.fill(product)
        self.button_create_product.click()
    

    def delete_product_by_name(self,product):
        # complete logic
        product_row = self.page.locator(f".product-item:has(span:text('{product}'))")
        delete_button = product_row.get_by_role("button", name="Delete")
        delete_button.click()


    def product_exists(self, product: str) -> bool:
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        return product_locator.is_visible()