# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username

class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_input_username = page.locator("#username")
        self.signup_input_password = page.locator("#password")
        self.button_signup = page.locator("#signup")

    def sign_up(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.button_signup.click()
        
        