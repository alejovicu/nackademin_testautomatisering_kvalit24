# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        #complete admin view elements

        # skapa ny produkt
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.btn_create_product = page.get_by_role("button", name ="Create Product")
        
        # Produktlistan
        self.rows = page.locator(".product-item") # varje produktrad
        self.btn_del_in_rows = self.rows.locator(".product-item-button") # delete-knapp i en rad

        # logga ut
        self.btn_logout = page.get_by_role("button", name = "Logout")


    def get_current_product_count(self):
        # return number of total products displayed
        return self.rows.count()

    def create_product(self, product_name):
        self.input_product_name.fill(product_name)
        self.btn_create_product.click()

    def delete_product_by_name(self,product_name):
        row = self.rows.filter(has_text=product_name).first
        row.locator(".product-item-button").click()
