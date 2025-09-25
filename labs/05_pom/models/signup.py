# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username


class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_input_username = page.get_by_placeholder("Username")
        self.signup_input_password = page.get_by_placeholder("Password")
        self.button_signup = page.get_by_role("button", name="Sign up")
        self.button_login = page.get_by_role("button", name="Login")

    def signup(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.button_signup.click()

    def navigate_to_login(self):
        self.button_login.click()
