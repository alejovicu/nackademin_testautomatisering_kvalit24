# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        # complete code


    def get_user_products(self):
        items = self.page.locator("div[style*='grid-template-columns'] > div")
        return items.all_text_contents()


    #Should not be done
    #def add_product_to_user(self, product_name):
       

    #def remove_product_from_user(self, product_name):
       