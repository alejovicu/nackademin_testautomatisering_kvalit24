# # View  where the admin user can manage the products
# # that are in the Product Catalog to be used
# # by all the users


# class AdminPage:
#     def __init__(self, page):
#         self.page = page
#         #page_(element-type)_(descriptive-name)
#         #complete admin view elements

#     def get_current_product_count(self):
#         # complete logic
#         # return number of total products displayed

#     def create_product(self,product_name):
#         # complete logic

#     def delete_product_by_name(self,product_name):
#         # complete logic
from playwright.sync_api import Page


class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        # UI selectors (adjust if your frontend uses different IDs/classes/texts)
        self.input_product_name = page.locator("input[placeholder='Product Name']")
        self.button_create = page.get_by_role("button", name="Create Product")

    def get_current_product_count(self) -> int:
        """Return the number of products displayed in the catalog table/list."""
        product_rows = self.page.locator(".product-item")  # each row container
        return product_rows.count()

    def create_product(self, product_name: str):
        """Type a product name and click Create Product."""
        self.input_product_name.fill(product_name)
        self.button_create.click()
        # Wait for product list to update (new product visible)
        self.page.wait_for_selector(f".product-item:has-text('{product_name}')")

    def delete_product_by_name(self, product_name: str):
        """Delete a product row by its name."""
        row = self.page.locator(f".product-item:has-text('{product_name}')")
        delete_btn = row.locator(".product-item-button")
        delete_btn.click()
        # Wait until the product row is gone
        row.wait_for(state="detached")
