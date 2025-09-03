# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_input_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_button_login = page.locator("button.button-primary")
        self.login_button_signup = page.locator("#signup")

    def navigate_to_signup(self):
        self.login_button_signup.click()

    def login(self, username, password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_button_login.click()
