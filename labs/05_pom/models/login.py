# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.header_title = page.get_by_text("Nackademin Course App")
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_login = page.locator("button.button-primary")
        self.label_signup = page.get_by_text("Don't have an account?")
        self.button_signup = page.locator("#signup")

    def login(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()

    def navigate_to_signup(self):
        self.button_signup.click()

    def navigate_to_login(self):
        self.button_login.click()
