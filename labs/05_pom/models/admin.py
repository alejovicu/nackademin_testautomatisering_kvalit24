class AdminPage:
    def __init__(self, page):
        self.page = page
        self.input_productname = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role("button", name="Create Product")
        self.products = page.locator('.product-item')
        self.button_delete_product = page.get_by_role("button", name="Delete")

    def count_products(self) -> int:
        return self.products.count()

    def create_product(self, product: str):
        self.input_productname.fill(product)
        self.button_create_product.click()
    
    def remove_last_product(self):
        product = self.products.last
        product.get_by_role("button", name="Delete").click()