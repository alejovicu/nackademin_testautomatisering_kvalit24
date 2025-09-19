# Page where the users could either create a new user or
# navigate to Home
class SignupPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.get_by_placeholder('Username')
        self.signup_input_password = page.get_by_placeholder('Password')
        self.signup_btn_signup = page.locator('button.button-primary')
        self.signup_btn_login = page.locator('button.btn-blue')


    def signup(self,username,password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)

        # Wait for alert to appear while clicking signup
        # Needed to catch alert reliably, issues with slowmo/non-slowmo runs
        with self.page.expect_event("dialog") as dialog_info:
            self.signup_btn_signup.click()

        dialog = dialog_info.value
        dialog.accept()


    def go_to_home(self):
        self.signup_btn_login.click()