
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:5173/")


