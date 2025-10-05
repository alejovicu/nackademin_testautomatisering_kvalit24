class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_input_product_name = page.get_by_placeholder("Product Name")
        self.admin_btn_create = page.get_by_role("button", name="Create Product")
        self.product_items = page.locator("div.product-item")
        self.product_delete_buttons = page.get_by_role("button", name="Delete")

    def get_current_product_count(self):
        try:
            self.page.wait_for_selector(
                "div.product-item", state="attached", timeout=3000
            )
        except:
            pass
        self.page.wait_for_load_state("networkidle")
        return self.product_items.count()

    def create_product(self, product_name):
        self.admin_input_product_name.fill(product_name)
        self.admin_btn_create.click()
        self.page.wait_for_load_state("networkidle")

    def delete_product_by_name(self, product_name):
        row = self.page.locator(f"div.product-item:has-text('{product_name}')").first
        row.get_by_role("button", name="Delete").click()
        try:
            row.wait_for(state="detached", timeout=7000)
        except:
            pass
