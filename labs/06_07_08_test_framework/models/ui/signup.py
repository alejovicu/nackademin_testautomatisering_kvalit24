class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_input_username = self.page.get_by_placeholder("Username")
        self.signup_input_password = self.page.get_by_placeholder("Password")
        self.signup_btn_submit = self.page.get_by_role("button", name="Sign Up")
        self.login_link = self.page.get_by_role("button", name="Login")  # <— ADD THIS

    def wait_for_page(self):
        self.signup_input_username.wait_for(state="visible")

    def signup(self, username, password):
        self.wait_for_page()
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_submit.click()

    def go_to_home(self):
        self.login_link.click()
        self.page.wait_for_load_state("domcontentloaded")
