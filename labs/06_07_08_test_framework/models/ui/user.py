# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
from playwright.sync_api import Page, expect

class UserPage:
    def __init__(self, page: Page):
        self.page = page
        self.catalog_items = page.locator(".catalog .product-item")       
        self.user_items = page.locator(".user-products .product-item")    

    def get_user_products(self) -> int:
        return self.user_items.count()

    def add_product_to_user(self, product_name: str):
        
        #Find the product in the catalog list and click its 'Add' button.
        #Wait until it appears under the user's products.
        # row in catalog that contains product_name
        row = self.page.locator(".catalog .product-item", has_text=product_name)
        expect(row).to_be_visible()
        row.get_by_role("button", name="Add").click()
        # wait until it shows up under user products
        expect(self.user_items.filter(has_text=product_name)).to_have_count(1)

    def remove_product_from_user(self, product_name: str):
        row = self.page.locator(".user-products .product-item", has_text=product_name)
        expect(row).to_be_visible()
        before = self.get_user_products()
        row.get_by_role("button", name="Delete").click()
        # wait until count decreases and the row is gone
        expect(self.user_items).to_have_count(before - 1)
        expect(self.user_items.filter(has_text=product_name)).to_have_count(0)