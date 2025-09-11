# # View where an user (non admin) can Choose
# # produts from the Product Catalog and/or
# # remove it

# class UserPage:
#     def __init__(self, page):
#         self.page = page
#         #page_(element-type)_(descriptive-name)
#         # complete code

#     def get_user_products(self):
#         # complete code

#     def add_product_to_user(self, product_name):
#         # complete code

#     def remove_product_from_user(self, product_name):
#         # complete code
from playwright.sync_api import Page


class UserPage:
    def __init__(self, page: Page):
        self.page = page
        # page_(element-type)_(descriptive-name)
        self.user_product_rows = page.locator(".user-product-row")  # each owned product
        self.catalog_rows = page.locator(".product-row")  # all catalog products

    def get_user_products(self) -> list[str]:
        """Return the list of product names currently owned by the user."""
        return self.user_product_rows.all_inner_texts()

    def add_product_to_user(self, product_name: str):
        """Click 'Add' for a product in the catalog by product name."""
        row = self.catalog_rows.filter(has_text=product_name)
        add_btn = row.locator(".add-product")
        add_btn.click()
        # Wait until product appears in user's product list
        self.page.locator(f".user-product-row:has-text('{product_name}')").wait_for()

    def remove_product_from_user(self, product_name: str):
        """Click 'Remove' for a product owned by the user by product name."""
        row = self.user_product_rows.filter(has_text=product_name)
        remove_btn = row.locator(".remove-product")
        remove_btn.click()
        # Wait until product disappears from user's product list
        row.wait_for(state="detached")
