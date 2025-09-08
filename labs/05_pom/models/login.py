# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_login = page.locator("button.button-primary")  # CSS 
        self.button_signup = page.locator("#signup")


    def navigate(self):
        self.page.goto("https://localhost:5173")


    def navigate_to_signup(self):
        self.button_signup.click()


    def login_as_admin(self):
        self.input_username.fill("admin")
        self.input_password.fill("admin")
        self.button_login.click()
        


