from playwright.sync_api import Page


class UserPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_add_product = page.get_by_role("button", name="Add Product")
        self.btn_logout = page.get_by_role("button", name="Logout")

    def add_product_to_user(self, product_name: str):
        self.btn_add_product.click()
        self.page.get_by_text("Select Products", exact=True).wait_for(timeout=7000)

        row = self.page.locator("li", has_text=product_name).first
        row.scroll_into_view_if_needed()
        row.get_by_role("button", name="Add").click()

        self.page.get_by_role("button", name="Close").click()
        self.page.get_by_text("Select Products", exact=True).wait_for(
            state="hidden", timeout=7000
        )

        self.page.locator("div", has_text=product_name).locator(
            "button.product-item-button"
        ).first.wait_for(timeout=10000)

    def remove_product_from_user(self, product_name: str):
        delete_btn = (
            self.page.locator("div", has_text=product_name)
            .locator("button.product-item-button")
            .first
        )

        delete_btn.scroll_into_view_if_needed()
        self.page.wait_for_timeout(100)
        delete_btn.click()

        self.page.locator("div", has_text=product_name).locator(
            "button.product-item-button"
        ).first.wait_for(state="detached", timeout=10000)
