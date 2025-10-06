# Landing page where the users could either login or
# navigate to signup
import os

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")

class HomePage:
    def __init__(self, page):
        self.page = page

        self.login_header_main_title = page.get_by_text("Nackademin Course App")
        self.login_input_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_btn_login = page.locator("button.button-primary")
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator("#signup")

    def navigate(self):
        self.page.goto(FRONTEND_URL)

    def login(self, username, password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()

    def go_to_signup(self):
        self.login_btn_signup.click()
