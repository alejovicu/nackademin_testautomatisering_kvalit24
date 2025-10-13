# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        # List/grid of products (each row has .product-item)
        self.products = page.locator(".product-grid .product-item")
        # Create controls
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.btn_create = page.get_by_role("button", name="Create Product")

    def get_current_product_count(self) -> int:
        return self.products.count()

    def create_product(self, product_name: str):
        #Fill name, click create, wait for +1 and row visible.
        before = self.get_current_product_count()
        self.input_product_name.fill(product_name)
        self.btn_create.click()
        # wait for the new row to appear and count to increase
        expect(self.products).to_have_count(before + 1)
        expect(self.page.locator(".product-item", has_text=product_name)).to_have_count(1)

    def delete_product_by_name(self, product_name: str):
        #Click 'Delete' in the row matching product_name and wait until it's removed.
        row = self.page.locator(".product-item", has_text=product_name)
        expect(row).to_be_visible()
        before = self.get_current_product_count()
        row.get_by_role("button", name="Delete").click()
        # after delete, count decreases and row disappears
        expect(self.products).to_have_count(before - 1)
        expect(self.page.locator(".product-grid .product-item").filter(has_text=product_name)).to_have_count(0)