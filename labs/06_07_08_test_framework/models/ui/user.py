# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        # Target the <h3> heading by its role and exact name
        self.products_header = self.page.get_by_role("heading", name="Your Products:")
        self.logout_btn = self.page.get_by_role("button", name="Logout")

    def wait_for_page(self):
        self.products_header.wait_for(state="visible", timeout=60000)

    def get_user_products(self):
        self.wait_for_page()

        # If "No products assigned." is visible → return empty list
        if self.page.get_by_text("No products assigned.", exact=True).is_visible():
            return []

        # Otherwise, collect products (adjust if your app later adds items)
        return self.page.locator("#root > div > div").all_inner_texts()

    def logout(self):
        self.logout_btn.click()
        self.page.wait_for_load_state("domcontentloaded")


def get_user_products(self):
    return self.page.locator(".user-product").all_inner_texts()

def add_product_to_user(self, product_name):
    self.page.locator("#product-name").fill(product_name)
    self.page.locator("#add-product").click()

def remove_product_from_user(self, product_name):
    self.page.locator(f"text={product_name} >> .. >> button.remove").click()