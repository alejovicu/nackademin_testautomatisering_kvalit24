from playwright.sync_api import Page


class UserPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_add_product = page.get_by_role("button", name="Add Product")
        self.btn_logout = page.get_by_role("button", name="Logout")

    def add_product_to_user(self, product_name: str):
        self.btn_add_product.click()
        try:
            modal = self.page.get_by_role("dialog", name="Select Products")
            modal.wait_for(timeout=5000)
        except:
            self.page.get_by_text("Select Products", exact=True).wait_for(timeout=7000)
            modal = (
                self.page.locator("section, div, form")
                .filter(has_text="Select Products")
                .first
            )
        row = modal.locator("li", has_text=product_name).first
        row.scroll_into_view_if_needed()
        add_btn = row.get_by_role("button", name="Add").first
        add_btn.wait_for(state="visible", timeout=5000)
        add_btn.click()
        try:
            modal.get_by_role("button", name="Close").click()
        except:
            self.page.get_by_role("button", name="Close").click()
        try:
            modal.wait_for(state="hidden", timeout=7000)
        except:
            self.page.get_by_text("Select Products", exact=True).wait_for(
                state="hidden", timeout=7000
            )
        self.page.locator("div.product-item").filter(
            has_text=product_name
        ).first.wait_for(timeout=10000)

    def remove_product_from_user(self, product_name: str):
        card = self.page.locator("div.product-item").filter(has_text=product_name).first
        delete_btn = card.locator("button.product-item-button").first
        delete_btn.scroll_into_view_if_needed()
        self.page.wait_for_timeout(100)
        delete_btn.click()
        card.wait_for(state="detached", timeout=10000)
