class HomePage:
    def __init__(self, page):
        self.page = page
        self.input_product_name = page.get_by_placeholder("Product Name")
        self.button_add_product = page.get_by_role("button", name="Add Product")
        self.button_logout = page.get_by_role("button", name="Logout")

    def navigate(self):
        self.page.goto("http://localhost:5173/")

    def add_product(self, product_name: str):
        self.input_product_name.fill(product_name)
        self.button_add_product.click()

    def assert_product_visible(self, product_name: str):
        self.page.get_by_text(product_name).wait_for()

    def remove_product(self, product_name: str):
        self.page.get_by_role("button", name=f"Delete {product_name}").click()

    def assert_product_not_visible(self, product_name: str):
        self.page.get_by_text(product_name).wait_for(state="detached")

    def logout(self):
        self.button_logout.click()
