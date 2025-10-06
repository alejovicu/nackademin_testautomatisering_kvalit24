class SignupPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.locator("#inp-username")
        self.signup_input_password = page.locator("#inp-password")
        self.signup_btn_signup = page.get_by_role("button", name="Sign Up")
        self.signup_btn_login_link = page.get_by_role("button", name="Login")

    def signup(self, username, password):
        self.page.fill(
            "#inp-username, input[placeholder='Username'], input[name='username']",
            username,
        )
        self.page.fill(
            "#inp-password, input[placeholder='Password'], input[name='password']",
            password,
        )
        self.page.get_by_role("button", name="Sign Up").first.click()

    def go_to_home(self):
        self.signup_btn_login_link.click()

        self.page.wait_for_selector(
            "#inp-username, input[placeholder='Username'], input[name='username']",
            state="visible",
            timeout=7000,
        )
        self.page.wait_for_selector(
            "#inp-password, input[placeholder='Password'], input[name='password']",
            state="visible",
            timeout=7000,
        )
