# # Page where the users could either create a new user or
# # navigate to Home
# class SignupPage:
#     def __init__(self, page):
#         self.page = page

#         self.signup_input_username = page.get_by_placeholder('Username')
#         self.signup_input_password = page.get_by_placeholder('Password')
#         self.signup_btn_signup = page.locator('button.button-primary')
#         self.signup_btn_login = page.locator('button.btn-blue')


#     def signup(self,username,password):
#         self.signup_input_username.fill(username)
#         self.signup_input_password.fill(password)
#         self.signup_btn_signup.click()

#     def go_to_home(self):
#         # complete code
from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

        self.signup_input_username = page.get_by_placeholder("Username")
        self.signup_input_password = page.get_by_placeholder("Password")
        self.signup_btn_signup = page.locator("button.button-primary")
        self.signup_btn_login = page.locator("button.btn-blue")

    def signup(self, username: str, password: str):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_signup.click()

    def go_to_home(self):
        """Click the 'Login' button on the signup page and wait for login form."""
        self.signup_btn_login.click()
        # Wait until the Login form appears
        self.page.get_by_text("Login").wait_for()
