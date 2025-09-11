class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        # Correct way to find a button with role + text
        #self.button_login = page.get_by_role("button", name="Login")
        self.button_login = page.locator("button.button-primary")
        self.button_signup = page.locator("#signup")

    def navigate_to_signup(self):
        """Navigate to the signup page by clicking the signup button"""
        self.button_signup.click()

    def login(self, username, password):
        """Fill in username and password, then click login"""
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_login.click()
