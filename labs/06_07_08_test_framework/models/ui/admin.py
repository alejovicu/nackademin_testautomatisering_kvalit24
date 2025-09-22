class AdminPage:
    def __init__(self, page):
        self.page = page
        # Updated selectors for product-related elements
        self.product_name_input = self.page.locator("#root > div > div > div:nth-child(3) > input[type=text]")
        self.add_product_btn = self.page.locator("#root > div > div > div:nth-child(3) > button")
        self.product_grid = self.page.locator("#root > div > div > div.product-grid")  # Correct selector for the product grid

    def create_product(self, product_name):
        """
        Adds a product to the catalog.
        :param product_name: Name of the product to add.
        """
        # Wait for the product name input field to be visible
        self.page.wait_for_selector("#root > div > div > div:nth-child(3) > input[type=text]")

        # Debugging: Print the product name being added
        print(f"Adding product: {product_name}")

        # Fill in the product name and click the add button
        self.product_name_input.fill(product_name)
        self.add_product_btn.click()

        # Wait for the product grid to update
        self.page.wait_for_selector(f"#root > div > div > div.product-grid >> text={product_name}")
        print(f"Product '{product_name}' added successfully.")

    def get_current_product_list(self):
        """
        Returns the list of product names in the catalog.
        """
        # Wait for the product grid to be visible
        self.page.wait_for_selector("#root > div > div > div.product-grid")

        # Retrieve all product containers in the product grid
        product_containers = self.product_grid.locator("div")  # Adjusted to locate all product items

        # Debugging: Print the number of product containers
        print(f"Number of product containers: {product_containers.count()}")

        # Extract only the product names
        product_list = []
        for i in range(product_containers.count()):
            try:
                product_name = product_containers.nth(i).locator("span").inner_text()  # Locate the product name dynamically
                product_list.append(product_name)
            except Exception as e:
                print(f"Error retrieving product name for container {i}: {e}")

        print(f"Current product list: {product_list}")  # Debugging: Print the product list
        return product_list

    def delete_product_by_name(self, product_name):
        """
        Deletes a product from the catalog by its name.
        :param product_name: Name of the product to delete.
        """
        print(f"Attempting to delete product: {product_name}")

        # Locate the product in the product grid
        product_locator = self.page.locator(f"#root > div > div > div.product-grid >> text={product_name}")

        # Check if the product exists
        if not product_locator.is_visible():
            print(f"Product '{product_name}' not found in the product grid!")
            raise Exception(f"Product '{product_name}' not found in the product grid!")

        # Locate the delete button for the product
        delete_button = product_locator.locator("..").locator("button")  # Adjusted to find the delete button relative to the product

        # Check if the delete button is visible
        if not delete_button.is_visible():
            print(f"Delete button for product '{product_name}' not found!")
            raise Exception(f"Delete button for product '{product_name}' not found!")

        # Click the delete button
        delete_button.click()

        # Wait for the product to be removed from the product grid
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the product grid updates
        print(f"Product '{product_name}' deleted successfully.")