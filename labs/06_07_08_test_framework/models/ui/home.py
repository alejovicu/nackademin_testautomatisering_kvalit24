from playwright.sync_api import expect
import time
import os

class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = os.getenv("FRONTEND_URL", "http://localhost")
        self.login_header_main_title = page.get_by_text('Nackademin Course App')
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator('button.button-primary')
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator('#signup')


    def navigate(self):
        self.page.goto(self.url)


    def login(self,username,password):
        self.login_input_username.fill(username)
        time.sleep(0.5)
        self.login_input_password.fill(password)
        time.sleep(0.5)
        self.login_btn_login.click()
        time.sleep(2)
        
        self.page.screenshot(path=f"/tmp/login_{username}.png")


    def go_to_signup(self):
        self.login_btn_signup.click()