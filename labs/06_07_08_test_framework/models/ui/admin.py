# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        #complete admin view elements

        self.admin_grid_products = page.locator(".product-grid .product-item")
        self.admin_input_product_name = page.get_by_role("textbox", name="Product Name")
        self.admin_btn_add_product = page.get_by_role("button", name="Create Product")

    def get_current_product_count(self):
        pass

    def create_product(self, product_name):
        count_before_adding = self.admin_grid_products.count()
        self.admin_input_product_name.fill(product_name)
        self.admin_btn_add_product.click()
        return count_before_adding


    def delete_product_by_name(self, product_name):
        self.page.locator(".product-item", has_text=product_name).get_by_role("button", name="Delete").click()
        deleted_product = self.page.locator(".product-grid .product-item").filter(has_text=product_name)
        return deleted_product