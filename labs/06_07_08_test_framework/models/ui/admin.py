# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_products = page.locator('.product-item')
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role('button',  name= 'Create Product' )

        
    #Count existing number of products 
    def count_products(self):
        return self.admin_products.count()
        
            
    #Create new product
    def create_product(self,product_name):
        self.input_product_name.fill(product_name)
        self.button_create_product.click()
        

    #Delete produkt BY NAME
    def delete_product_by_name(self,product_name):
        delete_product = self.admin_products.filter(has_text=product_name)
        delete_product.get_by_role("button", name = "Delete").click()
