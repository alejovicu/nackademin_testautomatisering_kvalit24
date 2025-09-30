# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page

        self.product_input = page.get_by_placeholder('Product Name')
        self.create_p_button = page.get_by_role('button', name = "Create Product")
        self.p_del = page.locator('.product-item')
        
       
    
    def get_current_product_count(self):
        items = self.page.locator(".product-item").all()
        return len(items)


    
    def create_product(self,product_name):
        self.product_input.fill(product_name)
        self.create_p_button.click()


    def delete_product_by_name(self,product_name): 
        del_product = self.page.locator('.product-item', has_text=product_name)
        del_product.locator('.product-item-button').click()