# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it


class UserPage:
    def __init__(self, username, page):
        self.page = page
        self.header_title = page.get_by_text("Nackademin Course App")
        self.title_user = page.get_by_text(f"Welcome, {username}!")
        self.products_title = page.get_by_text("Your Products:")
        self.button_logout = page.get_by_role("button", name="Logout")

    def get_user_products(self):
        # Selecting the potential product grid
        grid_locator = self.page.locator("#root > div > div")

        # Check if user has no products assigned
        if grid_locator.locator("p", has_text="No products assigned.").is_visible():
            return []

        # If user has products, list them
        product_divs = grid_locator.locator("div")
        product_texts = [div.inner_text() for div in product_divs.all()]
        return product_texts

    def add_product_to_user(self, product_name):
        # Functionality to be implemented in frontend first
        pass

    def remove_product_from_user(self, product_name):
        # Functionality to be implemented in frontend first
        pass

    # Just for testing purposes
    def logout(self):
        self.button_logout.click()
