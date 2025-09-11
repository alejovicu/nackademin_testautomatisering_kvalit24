from playwright.sync_api import Page


class AuthPage:
    def __init__(self, page: Page):
        self.browser_page = page

        # Elements
        self.title = page.get_by_text("Nackademin Course App")
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.submit_button = page.locator("button.button-primary")
        self.signup_label = page.get_by_text("Don't have an account?")

    def open(self):
        self.browser_page.goto("http://localhost:5173")

    def login_as_admin(self, user, pwd):
        self.username_field.fill(user)
        self.password_field.fill(pwd)
        self.submit_button.click()