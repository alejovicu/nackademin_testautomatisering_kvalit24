# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.addproduct_input_productname = page.get_by_placeholder("Product Name")
        self.create_btn_createproduct = page.get_by_role("button", name="Create Product")
        self.product_lists = page.locator(".product-grid .product-item")
        self.logout_btn = page.get_by_role("button", name="Logout")
        self.empty_product_message = page.get_by_text("No products avalible.")
        self.delete_btn = page.get_by_role("button", name="Delete")

    def get_current_product_count(self):
        # if self.empty_product_message.is_visible():
        #     return 0
        return self.product_lists.count()

    def create_product(self, product_name):
        # Inputs name of product
        self.addproduct_input_productname.fill(product_name)
        # Clicks the button
        self.create_btn_createproduct.click()

        # Waits until the product appears
        new_product = self.page.get_by_text(product_name, exact=True)
        new_product.wait_for(state="visible")

    def delete_product_by_name(self, product_name):
        product_item = self.page.locator(f".product-item:has-text('{product_name}')")

        if product_item.count() == 0:
            raise ValueError(f"Product '{product_name}' not found.")

        product_item.get_by_role("button", name="Delete").click()

        # Waits until the product dissappears
        product_item.wait_for(state="detached")
