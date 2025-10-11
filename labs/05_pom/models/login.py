from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "http://localhost:5173/"

    def navigate(self):
        self.page.goto(self.base_url, wait_until="networkidle")

    def login_user(self, username: str, password: str):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
