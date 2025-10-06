# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from playwright.sync_api import expect


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.input_create_product = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role("button", name="Create Product")
        self.product_cards = page.locator(".product-item")


    def get_current_product_count(self):
        return self.product_cards.count()
    

    def create_product(self, product):
        expect(self.page.locator("text=Add new product:")).to_be_visible(timeout=10000)
        expect(self.input_create_product).to_be_visible(timeout=10000)
        self.input_create_product.fill(product)
        self.button_create_product.click()
    

    def delete_product_by_name(self,product):
        # complete logic
        product_row = self.page.locator(f".product-item:has(span:text('{product}'))")
        expect(product_row).to_be_visible(timeout=10000)
        delete_button = product_row.get_by_role("button", name="Delete")
        expect(delete_button).to_be_enabled(timeout=5000)
        delete_button.click()
        expect(product_row).not_to_be_visible(timeout=10000)


    def product_exists(self, product: str) -> bool:
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        return product_locator.is_visible()
    
    def product_is_visible(self, product):
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        expect(product_locator).to_be_visible(timeout=10000)

    def product_to_not_be_visible(self, product):    
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        expect(product_locator).not_to_be_visible(timeout=10000)   