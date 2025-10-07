# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the user


class AdminPage:
    def __init__(self, page):
        self.page = page
        # Input-fältet har placeholder "Product Name"
        self.admin_input_product = page.get_by_placeholder("Product Name")
        # Knappen har texten "Create Product"
        self.admin_create_product_button = page.get_by_role("button", name="Create Product")
        # Produkter är inte i .product-item utan visas som text med Delete-knapp
        self.admin_products = page.locator("text=/^(keyboard|test_product|[^\\s]+).*Delete$/")
        
    def get_current_product_count(self):
        # Räkna antalet Delete-knappar (= antal produkter)
        return self.page.get_by_role("button", name="Delete").count()
    
    def create_product(self, product_name):
        # Vänta på att input är synligt
        self.admin_input_product.wait_for(state="visible", timeout=5000)
        self.admin_input_product.fill(product_name)
        self.admin_create_product_button.click()
        # Vänta lite så produkten hinner skapas
        self.page.wait_for_timeout(1000)
    
    def delete_product_by_name(self, product_name):
        # Hitta raden med produktnamnet och klicka på dess Delete-knapp
        # Använd en mer specifik locator
        product_row = self.page.locator(f"text={product_name}").first
        delete_button = product_row.locator(".. >> button:has-text('Delete')").first
        delete_button.click()
        # Vänta lite så produkten hinner tas bort
        self.page.wait_for_timeout(1000)
        