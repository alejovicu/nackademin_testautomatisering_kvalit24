# Implement PO for signup
# 2 inputs and 1 button
# Naming example:  signup_input_username

class SignupPage:
    def __init__(self, page):
        self.page = page
        #self.input_username = page.locator("Username")
        #self.input_password = page.locator("Password")
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_signup = page.locator("#signup")          # id selector
        self.button_login = page.locator(".button-primary")     # class selector
        

    
    def signup(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_signup.click()


    def navigate_to_login(self):
        self.button_login.click()