# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users

class AdminPage:
    def __init__(self, page):
        self.page = page

        self.input_product_name = page.get_by_placeholder('Product Name')
        self.create_product_btn = page.get_by_role('button', name='Create Product')
        self.delete_product = page.locator('.product-item')


    def get_current_product_count(self):
        # return number of total products displayed 
           
        return self.page.locator('.product-item').count()


    def create_product(self,product_name):
        self.input_product_name.fill(product_name)
        self.create_product_btn.click()
        

    def delete_product_by_name(self,product_name):
        remove_product = self.page.locator('.product-item', has_text=product_name)
        remove_product.locator('.product-item-button').click()