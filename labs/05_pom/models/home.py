class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:5173/")

    def add_product(self,product_name):
        self.page.get_by_placeholder("Product name").fill(product_name)
        self.page.get_by_role("button", name="Create Product").click()


    def delete_product(self,product_name):
        product_item=self.page.locator(".product-item", has_text=product_name)
        delete_button=product_item.get_by_role("button", name="Delete")
        delete_button.click()