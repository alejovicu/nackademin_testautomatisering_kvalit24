# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_login = page.get_by_role("button").and_(page.get_by_text("Login"))
        self.button_signup = page.locator("#signup")

    def nav_to_signup(self):
        self.button_signup.click()

    def login(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()
