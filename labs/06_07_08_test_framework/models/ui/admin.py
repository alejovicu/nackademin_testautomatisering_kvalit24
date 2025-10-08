# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from playwright.sync_api import expect

class AdminPage:
    def __init__(self, page):
        self.page = page
        self.product_name_input = page.get_by_placeholder("Product Name")
        self.create_product_btn = page.get_by_role("button", name="Create Product")
        self.product_items = page.locator(".product-item")
        self.delete_buttons = page.get_by_role("button", name="Delete")
        self.login_inpu_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def wait_loaded(self):
        expect(self.product_name_input).to_be_visible(timeout=10000)
    
    def login(self, username, password):
        self.login_inpu_username.fill(username)
        self.login_input_password.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(500)  # wait for navigation to admin page
    
    def get_current_product_count(self):
        self.wait_loaded()
        # return number of total products displayed
        return self.product_items.count()

    def create_product(self,product_name):
        self.wait_loaded()
        self.product_name_input.fill(product_name)
        self.create_product_btn.click()
        self.page.wait_for_timeout(500)  # wait for the product to be created

    def delete_product_by_name(self,product_name):
        row = self.page.locator(f".product-item:has-text('{product_name}')")
        row.get_by_role("button", name="Delete").click()
       
        expect(row).not_to_be_visible(timeout=5000)