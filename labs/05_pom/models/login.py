# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_username = page.locator("#username")
        self.input_password = page.locator("#password")
        self.button_login = page.locator("#login")
        self.button_signup = page.locator("#signup")

    def login(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()

    def navigate_to_signup(self):
        self.button_signup.click()

