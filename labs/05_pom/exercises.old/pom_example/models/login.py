class LoginPage:
    def __init__(self, page):
        self.page = page
        # page_element-type_descriptive-name()
        self.login_header_main_banner = page.get_by_text("Nackademin Course App")
        self.login_input_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_btn_login = page.locator("button.button-primary")  # CSS Locator
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_submit = page.locator("button.signup")

    def navigate(self):
        self.page.goto("http://localhost:5173")

    def login(self, username, password):
        self.login_input_username.fill(username)
        self.login_input_username.fill(password)
        self.login_btn_login.click()
