

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.product = page.locator(".product-grid .product-item")
        self.product_field = page.get_by_role("textbox", name="Product Name")
        self.product_button = page.get_by_role("button", name="Create Product")

    def add_product(self, new_product):
        count_before_adding = self.product.count()
        self.product_field.fill(new_product)
        self.product_button.click()
        return count_before_adding
    
    def delete_product(self, new_product):
        self.page.locator(".product-item", has_text=new_product).get_by_role("button", name="Delete").click()
        deleted_product = self.page.locator(".product-grid .product-item").filter(has_text=new_product)
        return deleted_product

