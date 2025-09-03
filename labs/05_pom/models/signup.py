# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username

class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_input_username = page.get_by_placeholder("Username")
        self.signup_input_password = page.get_by_placeholder("Password")
        self.signup_button_signup = page.locator("button.button-primary")
        self.signup_button_login = page.locator("button.btn.btn-blue")
    def navigate_to_login(self):
        self.signup_button_login.click()

    def register_new_user(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_button_signup.click()

