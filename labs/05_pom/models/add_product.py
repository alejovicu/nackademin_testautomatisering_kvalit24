from playwright.sync_api import expect


class ProductPage:
    def __init__(self, page):
        self.page = page
        self.addproduct_input_productname = page.get_by_placeholder("Product Name")
        self.create_btn_createproduct = page.get_by_role(
            "button", name="Create Product"
        )
        self.product_lists = page.locator(".product-grid")
        self.logout_btn = page.get_by_role("button", name="Logout")
        self.empty_product_message = page.get_by_text("No products avalible.")
        self.delete_btn = page.get_by_role("button", name="Delete")

    def create_product(self, productname: str):
        self.addproduct_input_productname.fill(productname)
        self.create_btn_createproduct.click()

    def logout(self):
        self.logout_btn.click()

    def remove_product(self):
        self.delete_btn.click()

    # def validate_product_in_list(self, product: str):
    #     expect(self.product_lists).to_contain_text(product)

    # def validate_product_not_in_list(self, product: str):
    #     expect(self.product_lists).get_by_text(product).not_to_be_visible()
