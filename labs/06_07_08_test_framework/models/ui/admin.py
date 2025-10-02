# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        #page_(element-type)_(descriptive-name)
        self.page = page
        self.admin_input_productname = page.get_by_placeholder("Product Name")
        self.admin_button_create_product = page.get_by_role("button", name="Create Product")
        self.admin_products = page.locator('.product-item')
        self.admin_button_delete_product = page.get_by_role("button", name="Delete")

    def get_current_product_count(self):
        return self.admin_products.count()

    def create_product(self,product: str):
        self.admin_input_productname.fill(product)
        self.admin_button_create_product.click()

    def delete_product_by_name(self, product_name: str):
        product_to_delete = self.admin_products.filter(has_text=product_name)
        product_to_delete.get_by_role("button", name = "Delete").click()
        
    def remove_last_product(self):
        product = self.admin_products.last
        product.get_by_role("button", name="Delete").click()