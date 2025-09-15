
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")  # korrekt selector från frontend
        self.input_password = page.get_by_placeholder("Password")
        self.button_login = page.locator("button.button-primary")
        self.button_signup = page.locator("#signup")

    def login(self, username: str, password: str):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()

    def navigate_to_signup(self):
        self.button_signup.click()
        # self.page.wait_for_url("**/signup")







