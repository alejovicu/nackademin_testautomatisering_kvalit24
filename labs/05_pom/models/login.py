class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_login = page.get_by_role("button", name="Login")
        self.button_signup = page.locator("#signup")

    def navigate_to_signup(self):
        self.button_signup.click()

    def login_as_admin(self, username="admin", password="admin123"):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()
