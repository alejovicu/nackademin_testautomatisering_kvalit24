# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from playwright.sync_api import expect


class AdminPage:
    def __init__(self, page):
        #page_(element-type)_(descriptive-name)
        self.page = page
        self.product_delete_btn = page.locator("button.product-item-button")
        self.product_create_btn = page.get_by_role(
            "button", name="Create Product")
        self.product_name_input = page.get_by_placeholder("Product Name")
        self.product_card = page.locator(".product-item")

    def get_current_product_count(self):
        count_products =  self.product_card.count()
        return count_products

    def create_product(self,product_name):

        self.product_name_input.fill(product_name)
        self.product_create_btn.click()

    def delete_product_by_name(self,product_name):
        product_locator = self.page.locator(".product-item", has_text=product_name)
        expect(product_locator).to_have_count(1)
        product_locator.locator("button").click()
        expect(product_locator).to_have_count(0)
