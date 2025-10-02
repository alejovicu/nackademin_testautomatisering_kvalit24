# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

#class UserPage:
    #def __init__(self, page):
        #self.page = page
        #page_(element-type)_(descriptive-name)
        # complete code

    #def get_user_products(self):
        # complete code

    #def add_product_to_user(self, product_name):
        # complete code

    #def remove_product_from_user(self, product_name):
        # complete code

# models/ui/user.py

class UserPage:
    def __init__(self, page):
        self.page = page
        self.product_items = page.locator(".product-item")

    def get_user_products(self):
        return self.product_items.all_text_contents()

    def assert_product_visible(self, product_name):
        product = self.page.get_by_text(product_name)
        assert product.is_visible(), f"Product '{product_name}' not visible for user."
