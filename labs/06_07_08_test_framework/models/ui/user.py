# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        self.header_title=page.get_by_text("Nackademin Course App")
        self.user_title=page.get_by_text("Welcome, User!")
        self.user_label_products=page.get_by_text("Your Products")
        self.button_logout=page.get_by_role("button",name="Logout")


    def get_user_products(self):
        # complete code
       
        container = self.page.locator("ul#user-products")  # change selector as needed

    # Check if container exists and is visible
        if container.count() == 0:
            # No container found, return empty list
            return []

        # Return list of product names (text) inside <li>
        return container.locator("li").all_text_contents()

        

    def add_product_to_user(self, product_name):
        # complete code
        self.page.get_by_role("button", name=f"Add {product_name}").click()
        self.page.wait_for_timeout(1000)  # wait for 1 second to ensure

    def remove_product_from_user(self, product_name):
        # complete code
        self.page.get_by_role("button", name=f"Remove {product_name}").click()
        self.page.wait_for_timeout(1000)  # wait for 1 second to ensure