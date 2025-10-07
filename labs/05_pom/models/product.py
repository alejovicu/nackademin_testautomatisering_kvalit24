from playwright.sync_api import Page, expect
class ProductPage:
    def __init__(self, page):
        self.page = page
        self.product_name = page.get_by_placeholder("Product Name")
        self.create_product = page.get_by_role("button", name="Create Product")
        self.product_list = page.locator(".product-item")
        self.get_delete= page.get_by_role("button", name = "Delete")

    def add_to_catalog(self, name:str):
        self.product_name.fill(name)
        self.create_product.click()
        self.page.wait_for_timeout(2000)  # wait for 2 seconds to ensure the product is added

    def validate_product_in_list(self, name:str):
        
        expect(self.page.locator(".product-item", has_text=name)).to_have_count(1)

    def remove_from_catalog(self, name: str):
        self.page.locator(".product-item", has_text=name).get_by_role("button", name="Delete").click()
    
    def validate_product_not_in_list(self, name:str):
        expect(self.page.locator(".product-item", has_text=name)).to_have_count(0)