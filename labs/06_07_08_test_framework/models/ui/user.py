# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        # complete code

def get_user_products(self):
    return self.page.locator(".user-product").all_inner_texts()

def add_product_to_user(self, product_name):
    self.page.locator("#product-name").fill(product_name)
    self.page.locator("#add-product").click()

def remove_product_from_user(self, product_name):
    self.page.locator(f"text={product_name} >> .. >> button.remove").click()