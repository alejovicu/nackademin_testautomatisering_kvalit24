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

    def _wait_admin_view_loaded(self):
        expect(self.page.get_by_text("Products available:")).to_be_visible(timeout=5000)
        expect(self.input_product_name).to_be_visible(timeout=5000)

    def get_current_product_count(self) -> int:
        self._wait_admin_view_loaded()
        return self.products.count()

    def create_product(self, product_name: str):
        self._wait_admin_view_loaded()
        self.input_product_name.fill(product_name)
        self.btn_create.click()
        expect(self.products.filter(has_text=product_name).first).to_be_visible(timeout=5000)

    def delete_product_by_name(self, product_name: str):
        row = self.products.filter(has_text=product_name)
        row.get_by_role("button", name="Delete").click()
        expect(row).to_have_count(0)