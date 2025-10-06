# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


#class AdminPage:
    #def __init__(self, page):
        #"self.page = page
        #page_(element-type)_(descriptive-name)
        #complete admin view elements

    #def get_current_product_count(self):
        # complete logic
        # return number of total products displayed

    #def create_product(self,product_name):
        # complete logic

    #def delete_product_by_name(self,product_name):
        # complete logic

   # models/ui/admin.py

class AdminPage:
    def __init__(self, page):
        self.page = page
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.btn_create_product = page.get_by_role("button", name="Create Product")
        self.btn_logout = page.get_by_role("button", name="Logout")
        self.product_items = page.locator(".product-item")

    def create_product(self, product_name):
        self.input_product_name.fill(product_name)
        self.btn_create_product.click()
        # ✅ Wait until the new product appears (up to 5 seconds)
        self.page.wait_for_selector(f"text={product_name}", timeout=5000)

    def get_current_product_count(self):
        return self.product_items.count()

    def delete_product_by_name(self, product_name):
        product = self.page.locator(f".product-item:has-text('{product_name}')")
        delete_button = product.locator(".product-item-button")
        delete_button.click()
        # ✅ Short delay to let frontend start the delete
        self.page.wait_for_timeout(300)
        # ✅ Wait until the product disappears completely
        self.page.wait_for_selector(f"text={product_name}", state="detached", timeout=5000)

    def logout(self):
        self.btn_logout.click()
