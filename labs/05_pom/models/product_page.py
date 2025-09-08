from playwright.sync_api import Page
APP_URL = "http://localhost:5173/"

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_product(self, product_name: str):
        self.page.get_by_role("button", name="Add Product").click()
        self.page.get_by_placeholder("Product Name").fill(product_name)
        self.page.get_by_role("button", name="Save").click()

    def remove_last_product(self):
        # Hitta alla produkter (byt .product-item till din riktiga selector)
        products = self.page.locator(".product-item")
        count = products.count()

        if count == 0:
            raise Exception("Inga produkter att ta bort.")

        # Ta bort den sista produkten
        products.nth(count - 1).get_by_role("button", name="Remove").click()
