# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        self.login_user_main_title = page.get_by_text('Nackademin Course App')
        self.user_welcome_title = page.get_by_text('Welcome,')
        self.page_product_list = page.get_by_text("Your Products:")
        self.user_products = page.locator("h3:text('Your Products:') + div")
        self.button_add_product = page.get_by_role('button',  name= 'Add Product' )


    def get_user_products(self):
        return self.user_products
        

    def add_product_to_user(self, product_name):
        self.button_add_product.click()
        product_list = self.page.locator(f"li:has-text('{product_name}')")
        add_button = product_list.locator("button:has-text('Add')")
        add_button.click()
    



        

    def remove_product_from_user(self, product_name):
        product_list = self.user_products.locator(f"text={product_name}")
        remove_button = product_list.locator("button:has-text('Delete')")
        remove_button.click()
        