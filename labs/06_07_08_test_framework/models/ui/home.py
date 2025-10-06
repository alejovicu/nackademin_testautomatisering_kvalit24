import os
from playwright.sync_api import Page

FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:")

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_header_main_title = page.get_by_text("Nackademin Course App")
        self.login_input_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_btn_login = page.locator("button.button-primary")
        self.login_btn_signup = page.locator("#signup")

    def navigate(self):
        """
        Navigerar till frontend-sidan.
        """
        self.page.goto(FRONTEND_URL)

    def go_to_signup(self):
        """
        Klickar på signup-knappen för att gå till signup-sidan.
        """
        self.login_btn_signup.click()

    def login(self, username: str, password: str):
        """
        Loggar in användaren via UI.
        """
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()
