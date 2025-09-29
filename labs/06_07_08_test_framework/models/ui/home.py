class HomePage:
    def __init__(self, page):
        self.page = page
        # Use placeholders for login form
        self.login_input_username = self.page.get_by_placeholder("Username")
        self.login_input_password = self.page.get_by_placeholder("Password")
        self.login_btn_login = self.page.get_by_role("button", name="Login")
        self.signup_btn = self.page.get_by_role("button", name="Sign Up")

    def navigate(self):
        self.page.goto("http://localhost:5173/")
        self.page.wait_for_load_state("domcontentloaded")

    def login(self, username, password):
        self.login_input_username.wait_for(state="visible")
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()

    def go_to_signup(self):
        self.signup_btn.click()
        self.page.wait_for_load_state("domcontentloaded")
