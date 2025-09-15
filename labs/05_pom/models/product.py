
from playwright.sync_api import Page

class ProductPage:   # ✅ stor bokstav
    def __init__(self, page: Page):
        self.page = page
        self.add_product_button =page.get_by_role("button", name="Create Product")
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.product_list = page.locator(".product-grid")
        self.logout =page.get_by_role("button", name="Logout") 
        #self.save_product_button = "#save-product"
        #self.product_list = "#product-list"

    def add_product(self, name: str):
        self.input_product_name.fill(name)
        self.add_product_button.click()


    def remove_product(self, name: str):
        self.page.click(f"#delete-{name}")

    def is_product_listed(self, name: str) -> bool:
        return self.page.is_visible(f"text={name}")


