# Landing page where the users could either login or
# navigate to signup
import os

BASE_URL = os.getenv("APP_URL","http://localhost:5173/")

class HomePage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        self.login_header_main_title = self.page.get_by_text('Nackademin Course App')
        self.login_input_username = self.page.get_by_placeholder('Username')
        self.login_input_password = self.page.get_by_placeholder('Password')
        self.login_btn_login = self.page.locator('#btn-login')
        self.login_label_have_account = self.page.get_by_text("Don't have an account?")
        self.login_btn_signup = self.page.locator('#signup')

    def navigate(self):
        self.page.goto(BASE_URL)

    def login(self,username,password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()

    def go_to_signup(self):
        self.login_btn_signup.click()