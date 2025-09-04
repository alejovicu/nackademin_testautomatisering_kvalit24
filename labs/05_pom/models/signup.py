# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username


class SignUpPage:
    def __init__(self, page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_signup = page.get_by_role("button").and_(
            page.get_by_text("Sign Up")
        )
        self.button_login = page.locator("button.btn-blue")

    def nav_to_login(self):
        self.button_login.click()

    def sign_up(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_signup.click()
