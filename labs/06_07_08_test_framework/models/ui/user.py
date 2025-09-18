# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it


class UserPage:
    def __init__(self, page):
        self.page = page
        self.catalog_items = page.locator("div.product-item")

    def get_user_products(self):
        # Now only this message available
        if self.page.get_by_text("No products assigned.").count() > 0:
            return []
        # When the list of products will be available
        return [
            t.strip()
            for t in self.page.locator("div.product-item span").all_inner_texts()
        ]

    # def add_product_to_user(self, product_name):
    # complete code

    # def remove_product_from_user(self, product_name):
    # complete code
