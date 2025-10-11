from playwright.sync_api import Page, expect

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "http://localhost:5173/"

    def navigate(self):
        # Gå till signup-sidan
        self.page.goto(self.base_url, wait_until="networkidle")
        self.page.locator("#signup").click()

    def register_user(self, username: str, password: str):
        # Fyll i formuläret
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Sign Up").click()

        # Klicka login efter registrering
        self.page.get_by_role("button", name="Login").click()