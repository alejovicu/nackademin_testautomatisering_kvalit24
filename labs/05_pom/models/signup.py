class SignUpPage:
    def __init__(self, page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        # Correct locator for the Sign Up button
        self.button_signup = page.get_by_role("button", name="Sign Up")
        # Locator for "Log in" button to navigate back
        self.button_login = page.locator("button.btn-blue")

    def nav_to_login(self):
        """Navigate back to the login page"""
        self.button_login.click()

    def sign_up(self, username, password):
        """Fill in signup form and submit"""
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_signup.click()
