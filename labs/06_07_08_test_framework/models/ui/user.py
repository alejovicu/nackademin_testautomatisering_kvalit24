# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import re
from playwright.sync_api import expect

class UserPage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        self.grid = page.locator('h3:has-text("Your Products:") + div')
        self.items = self.grid.locator("div")

    def get_user_products(self):
        return [t.strip() for t in self.items.all_text_contents()]
    