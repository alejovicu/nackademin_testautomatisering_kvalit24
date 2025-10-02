# Page where the users could either create a new user or
# navigate to Home
class SignupPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.get_by_placeholder("Username")
        self.signup_input_password = page.get_by_placeholder("Password")
        self.button_signup = page.get_by_role("button").and_(
            page.get_by_text("Sign Up")
        )
        self.signup_btn_login = page.locator("button.btn-blue")

    def signup(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.button_signup.click()

    def go_to_home(self):
        self.signup_btn_login.click()
        # complete code
