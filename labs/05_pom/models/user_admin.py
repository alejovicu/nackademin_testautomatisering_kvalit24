from playwright.sync_api import expect
import re

class AdminUserPage:
    def __init__(self, page):
        self.page = page 
        self.addproduct_input_productname = page.get_by_placeholder("Product Name") # input fält
        self.create_product_btn = page.get_by_role("button", name="Create Product") # create product knappen
        self.product_lists = page.locator(".product-grid") # produktlista
        self.logout_btn = page.get_by_role("button", name="Logout") # logut knappen
        self.empty_product_message = page.get_by_text("No products available.") # 
        self.delete_btn = page.get_by_role("button", name="Delete")

    def navigate(self):
        """Go to homepage"""
        self.page.goto("http://localhost:5173/")

    def add_product(self, product_name: str):
        self.addproduct_input_productname.fill(product_name)
        self.create_product_btn.click()

    def logout(self):
        self.logout_btn.click()

    # def validate_product_in_list(self, product_name: str):
    #     expect(self.product_lists).to_contain_text(product_name)


    def remove_product(self):
        self.delete_btn.click()

    # def validate_product_not_in_list(self, product: str):
    #     expect(self.product_lists(product)
