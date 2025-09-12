class UserPage:
    def __init__(self, page):
        self.page = page
        self.header_main_title = page.get_by_text("Nackademin Course App")
        self.welcome_message = page.locator("h2:has-text('Welcome')")
        self.products_container = page.locator('div > h3:has-text("Your Products")')
        self.empty_product_list = page.get_by_role("p", name="No products assigned.")
        self.product_list = page.locator("div[style*='display: grid']")
        self.product_item_in_list = page.locator("div[style*='border: 1px solid']")
        self.button_logout = page.get_by_role("button", name="Logout")

    def get_user_products(self):
        # Feature does currently not require steps or actions in E2E
        # Products fetched directly on UserPage when loaded
        pass

    def add_product_to_user(self, product_name):
        # Feature not yet implemented in E2E
        pass

    def remove_product_from_user(self, product_name):
        # Feature not yet implemented in E2E
        pass
