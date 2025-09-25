from playwright.sync_api import expect


class UserPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        # complete code
        # page_(element-type)_(descriptive-name)
        self.header_title = page.get_by_text('Nackademin Course App')
        self.product_title = page.get_by_text('Your Products:')
        self.product_list = page.locator("xpath=//h3[text()='Your Products:']/following-sibling::div[1]/div"
                                         )

    def get_user_products(self) -> list[str]:

        expect(self.product_list).to_have_count(1)
        # complete code
        count = self.product_list.count()
        products = []
        for i in range(count):
            products.append(self.product_list.nth(i).inner_text())
        return products
