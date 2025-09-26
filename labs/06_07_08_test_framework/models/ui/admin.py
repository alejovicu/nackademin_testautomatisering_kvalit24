# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users


class AdminPage:
    def __init__(self, page):
        self.page = page
        # page_(element-type)_(descriptive-name)
        self.header_title = page.get_by_text("Nackademin Course App")
        self.h2_title = page.get_by_text("Welcome, admin!")
        self.grid_title = page.get_by_text("Products available:")
        self.product_grid = page.locator(".product-grid")
        self.product_list = page.locator(".product-grid > .product-item > span")
        self.product_list_delete_btn = page.locator(
            ".product-grid > .product-item > .product-item-button"
        )
        self.h3_title = page.get_by_text("Add new product:")
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_role("button", name="Create Product")
        self.button_logout = page.get_by_role("button", name="Logout")

    def find_product(self, product_name):
        return self.product_list.filter(has_text=product_name)

    def create_product(self, product_name):
        self.input_product_name.fill(product_name)
        self.button_create_product.click()

    def delete_product_by_name(self, product_name):
        product_div = self.page.locator(
            f'//div[@class="product-item"][span[text()="{product_name}"]]'
        )
        product_div.locator("button.product-item-button").click()
