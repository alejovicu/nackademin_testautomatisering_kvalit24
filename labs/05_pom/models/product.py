from playwright.sync_api import expect


class ProductPage:
    def __init__(self, page):
        self.page = page
        self.product_delete_btn = page.locator("button.product-item-button")
        self.product_create_btn = page.get_by_role(
            "button", name="Create Product")
        self.product_name_input = page.get_by_placeholder("Product Name")

    def create_product(self, product_name):
        products_with_name_before = self.page.locator(
            f".product-item:has-text('{product_name}')")
        count_before = products_with_name_before.count()

        self.product_name_input.fill(product_name)
        self.product_create_btn.click()

        products_with_name_after = self.page.locator(
            f".product-item:has-text('{product_name}')")
        count_after = products_with_name_after.count()

        assert count_after == count_before + 1

    def delete_product(self):

        products = self.page.locator(".product-item")
        products = products.count()

        delet_product_list = self.page.locator(".product-item button")
        delet_product_list.last.click()

        products_after = self.page.locator(".product-item")
        products_after = products_after.count()

        assert products_after == products - 1

        # alternative way to delete all products
        # while products.count() > 0:
        #     # Always delete the last product in the list
        #     products.last.locator(".product-item-button").click()
