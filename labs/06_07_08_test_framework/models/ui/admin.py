from playwright.sync_api import TimeoutError
import time


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.header_main_title = page.get_by_text("Nackademin Course App")
        self.welcome_message = page.locator("h2:has-text('Welcome')")
        self.products_header = page.get_by_text("Products available:")
        self.add_product_header = page.get_by_role("h3", name="Add new product:")
        self.empty_product_list = page.get_by_role("p", name="No products available.")
        self.product_list = page.locator(".product-grid")
        self.product_item_in_list = page.locator(".product-item")
        self.input_add_product = page.get_by_placeholder("Product Name")
        self.button_create_product = page.get_by_text("Create Product")
        self.button_logout = page.get_by_role("button", name="Logout")

    def add_product(self, product):
        self.input_add_product.fill(product)
        self.button_create_product.click()

    def locate_latest_product_name(self):
        return self.page.locator(".product-item > span").last

    def delete_latest_product(self):
        latest_product = self.page.locator(".product-item").last
        delete_button = latest_product.locator(
            ".product-item-button", has_text="Delete"
        )
        delete_button.click()

    def wait_for_product_list_to_load(self, timeout=3000):
        # If the empty list message is visible, skip waiting for products
        if self.empty_product_list.is_visible():
            return
        else:
            # Otherwise, wait for a product to appear
            latest_product = self.page.locator(".product-item").last
            latest_product.wait_for(state="visible", timeout=timeout)

    # Added function to await product change
    def wait_for_product_count_change(self, stock_count, count_value):
        try:
            self.page.wait_for_function(
                "count => document.querySelectorAll('.product-item').length === count",
                arg=stock_count + count_value,
                timeout=3000,
            )
        except TimeoutError:
            # If query fails on timeout, revert to wait for 5 seconds(apperent wait_for_locator issue specific to firefox)
            time.sleep(5)
