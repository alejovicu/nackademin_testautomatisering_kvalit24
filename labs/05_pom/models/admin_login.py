class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_header_title = page.get_by_text("Nackademin Course App")
        self.login_input_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_btn_login = page.locator("button.button-primary")  # css
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        
    def navigate_to_login(self):
        self.page.goto("http://localhost:5173/")

    def admin_login(self, username, password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()
