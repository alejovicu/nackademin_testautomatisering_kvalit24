from playwright.sync_api import Page


class UserPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_add_product = page.get_by_role("button", name="Add Product")
        self.btn_logout = page.get_by_role("button", name="Logout")

    def add_product_to_user(self, product_name: str):
        self.btn_add_product.click()
        modal = self.page.get_by_text("Select Products", exact=True)
        modal.wait_for(timeout=7000)

        self.page.evaluate("window.scrollTo(0, 0)")
        modal.locator("..").first.scroll_into_view_if_needed()

        list_container = self.page.locator(
            "role=dialog[name='Select Products'] ul, role=dialog[name='Select Products'] .modal-body, role=dialog[name='Select Products'] section"
        ).first
        row = (
            self.page.locator("role=dialog[name='Select Products'] li")
            .filter(has_text=product_name)
            .first
        )

        try:
            row.scroll_into_view_if_needed()
        except:
            pass
        try:
            list_container.evaluate(
                "(el, name) => {"
                "  const li=[...el.querySelectorAll('li')].find(n=>n.textContent.includes(name));"
                "  li && li.scrollIntoView({block:'center', inline:'center'});"
                "}",
                product_name,
            )
        except:
            pass

        add_btn = row.get_by_role("button", name="Add").first
        add_btn.wait_for(state="visible", timeout=5000)

        try:
            add_btn.click()
        except:
            box = add_btn.bounding_box()
            assert box is not None
            self.page.mouse.move(
                box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
            )
            self.page.mouse.click(
                box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
            )

        self.page.get_by_role("button", name="Close").click()
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
