# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from config import FRONTEND_URL

class AdminPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        #complete admin view elements
        self.header_title = page.get_by_text('Nackademin Course App')
        self.h2_title = page.get_by_text('Welcome, admin!')

        self.grid_title = page.get_by_text("Products available:")
        
        self.product_list = page.locator(".product-item")

        self.product_list_delete_btn = page.locator(
            ".product-item > .product-item-button"
        )
       
        
        self.h3_title = page.get_by_text("Add new product:")
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role("button", name="Create Product")
        self.button_logout = page.get_by_role("button", name="Logout")

      


    def navigate(self):
       self.page.goto(FRONTEND_URL)



    def get_current_product_count(self):
        # complete logic
        # return number of total products displayed
        return self.product_list.count()
        
        
    

    def create_product(self, product):
        # complete logic
        self.input_product_name.fill(product)
        self.button_create_product.click()
        
       

    def delete_product(self,product):
        # complete logic
        product_items = self.product_list
        count = product_items.count()

        for i in range(count):
            item = product_items.nth(i)
            text = item.inner_text()
            print(text)
            
            if text.startswith(product):
                
                self.page.locator(".product-item > .product-item-button").nth(i).click()
                #self.page.wait_for_timeout(1000)  # wait for 1 second to ensure
                break
        
        
  