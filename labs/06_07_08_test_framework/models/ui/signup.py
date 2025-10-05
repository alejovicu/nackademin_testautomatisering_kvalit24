class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_input_username = page.get_by_placeholder('Username')
        self.signup_input_password = page.get_by_placeholder('Password')
        self.signup_btn_signup = page.locator('#btn-signup')

    def signup(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_signup.click()
        self.page.wait_for_timeout(2000)

    def go_to_home(self):
        login_btn = self.page.locator('button').filter(has_text='Login').first
        login_btn.click()
        self.page.wait_for_timeout(500)