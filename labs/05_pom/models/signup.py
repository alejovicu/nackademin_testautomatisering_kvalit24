
from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_input_username = page.get_by_placeholder("Username")  # check frontend IDs
        self.signup_input_password = page.get_by_placeholder("Password")
        self.signup_button_register = page.locator("button.button-primary") #button-primary

    def signup(self, username: str, password: str):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_button_register.click()



