

class SignUpPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.get_by_role("textbox", name="Username")
        self.signup_input_password = page.get_by_role("textbox", name="Password")
        self.signup_button_login = page.get_by_role("button", name="Login")
        self.signup_button_signup = page.get_by_role("button", name="Sign Up")

    def navigate_to_login(self):
        self.signup_button_login.click()

    def signup(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_button_signup.click()