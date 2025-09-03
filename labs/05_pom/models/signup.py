# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username


class SignupPage:
    def __init__(self, page):
        self.page = page
        self.header_main_title = page.get_by_text("Nackademin Course App")
        self.sub_header_main_title = page.get_by_text("Sign Up")
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_signup = page.locator("button.button-primary")
        self.button_login = page.locator("button.btn-blue")

    def navigate_to_login(self):
        self.button_login.click()

    def signup_user(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_signup.click()
