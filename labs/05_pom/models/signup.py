# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username

# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username

# 05-pom/models/signup.py
from playwright.sync_api import Page, expect
from .login import LoginPage


class SignupPage:
    def __init__(self, page: Page, app_url: str):
        self.page = page
        self.app_url = app_url.rstrip("/")

    def open_from_login(self, login_page: LoginPage):
        # self.page.goto(self.app_url + "/")
        # Wait until signup "Sign Up" button is visible
        expect(self.page.get_by_role("button", name="Sign Up")).to_be_visible()
        self.page.get_by_role("button", name="Sign Up").click()
        return self

    def signup(self, username: str, password: str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)

        # # The UI shows an alert "User registered OK." on success.
        with self.page.expect_event("dialog") as dialog_info:
            self.page.get_by_role("button", name="Sign Up").click()
        dialog = dialog_info.value
        dialog.accept()
