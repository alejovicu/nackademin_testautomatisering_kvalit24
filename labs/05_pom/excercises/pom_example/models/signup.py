class SignupPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.get_by_placeholder('Username')
        self.signup_input_password = page.get_by_placeholder('Password')
        self.signup_btn_signup = page.locator('button.button-primary') #CSS locator
        self.signup_btn_login = page.locator('button.btn-blue')


    def signup(self,username,password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_signup.click()
