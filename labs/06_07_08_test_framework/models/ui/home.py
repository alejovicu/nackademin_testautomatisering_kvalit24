
class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator("button.button-primary", has_text="Login")
        self.login_btn_signup = page.locator('#signup')

    def navigate(self):
        self.page.goto("http://localhost:5173/")

    def login(self, username, password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()

    def go_to_signup(self):
        self.login_btn_signup.click()
