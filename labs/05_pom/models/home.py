from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        """Navigate to the home page and wait for main content to load."""
        self.page.goto("http://localhost:5173/")
        # Wait for main content to be visible
        expect(self.page.locator('#root')).to_be_visible()
