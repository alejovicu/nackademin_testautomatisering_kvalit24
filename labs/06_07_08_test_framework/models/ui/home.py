import os

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173/")


class HomePage:
    def __init__(self, page):
        self.page = page
        self.header_main_title = page.get_by_text("Nackademin Course App")
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_login = page.locator("button.button-primary")
        self.button_signup = page.locator("#signup")

    def navigate(self):
        self.page.goto(frontend_url)

    def navigate_to_signup(self):
        self.button_signup.click()

    def login_user(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()
