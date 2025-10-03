# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.header_title = page.get_by_text("Nackademin Course App")
        self.products_title = page.get_by_text("Your Products:")
        self.product_items = page.locator(".product-item")
        self.product_list = page.locator(".product-grid > .product-item > span")
        self.product_items_swagger = page.locator("div[style*='grid']").locator("div")
        

    def get_user_products(self):
        self.page.wait_for_selector(".product-item", timeout=5000)

        product_names = []

        try:
            self.page.wait_for_selector("product-item", timeout=2000)
        except:
            return product_names
        count = self.product_items.count()
        for i in range(count):
            name = self.product_items.nth(i).locator("span").inner_text()
            product_names.append(name.strip())

        return product_names
    
    def get_user_products_swagger(self):
        count = self.product_items_swagger.count()
        return [self.product_items_swagger.nth(i).inner_text().strip() for i in range(count)]

    # def add_product_to_user(self, product_name):
        # product = self.page.locator(".product-item").filter(
            # has=self.page.locator(f"span:text('{product_name}')")
        # )
        # product.locator("button.add").wait_for(state="visible", timeout=5000).click()
        

    # def remove_product_from_user(self, product_name):
        # product = self.page.locator(".product-item").filter(
            # has=self.page.locator(f"span:text('{product_name}')")
        # )
        # product.locator("button.remove").wait_for(state="visible").click()