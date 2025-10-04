class SignupPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.locator("#inp-username")
        self.signup_input_password = page.locator("#inp-password")
        self.signup_btn_signup = page.get_by_role("button", name="Sign Up")
        self.signup_btn_login_link = page.get_by_role("button", name="Login")

    def signup(self, username, password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_signup.click()

    def go_to_home(self):
        self.signup_btn_login_link.click()
        self.page.wait_for_url(lambda u: "#/login" in u, timeout=7000)
        self.page.get_by_text("Login", exact=True).wait_for(timeout=7000)
        self.page.locator("#inp-username, input[placeholder='Username']")
        self.page.locator("#inp-password, input[placeholder='Password']")
