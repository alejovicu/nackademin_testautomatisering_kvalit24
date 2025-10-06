# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it


class UserPage:
    def __init__(self, username, page):
        self.page = page
        # page_(element-type)_(descriptive-name)
        self.header_title = page.get_by_text("Nackademin Course App")
        self.title_user = page.get_by_text(f"Welcome, {username}!")
        self.products_title = page.get_by_text("Your Products:")
        self.button_logout = page.get_by_role("button", name="Logout")

    def get_user_products(self):
        # Wait for products or "No products assigned." to display
        self.page.wait_for_selector(
            "p:has-text('No products assigned.'), #root > div > div div"
        )
        # If "No products assigned." displays, return an empty list
        if self.page.locator("p:has-text('No products assigned.')").is_visible():
            return []
        # Otherwise, fetch all product divs and return their text
        return [
            el.inner_text() for el in self.page.locator("#root > div > div div").all()
        ]
