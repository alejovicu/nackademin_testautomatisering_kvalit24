# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

class LoginPage:
    def __init__(self, page):
        self.page = page
        #self.input_username = page.locator(??)
        #self.input_password = page.locator(??)
        #self.button_login = page.locator(??)
        self.button_signup = page.locator("#signup")

    def navigate_to_signup(self):
        self.button_signup.click()
