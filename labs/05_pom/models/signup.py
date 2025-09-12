
from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_input_username = page.locator("#signup-username")
        self.signup_input_password = page.locator("#signup-password")
        self.signup_button_register = page.locator("#signup-submit")

    def signup(self, username: str, password: str):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_button_register.click()

