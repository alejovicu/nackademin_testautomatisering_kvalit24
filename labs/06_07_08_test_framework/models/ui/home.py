import os


class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_header_main_title = page.get_by_text("Nackademin Course App")
        self.login_input_username = page.locator(
            "#inp-username, input[placeholder='Username']"
        )
        self.login_input_password = page.locator(
            "#inp-password, input[placeholder='Password']"
        )
        self.login_btn_login = page.locator("#btn-login, button:has-text('Login')")
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator("#signup")

    def navigate(self):
        base = os.getenv("FRONTEND_URL", "http://localhost/#/login").strip()
        self.page.goto(base, wait_until="domcontentloaded")
        self.page.wait_for_selector(
            "#inp-username, input[placeholder='Username']", timeout=10000
        )

    def login(self, username, password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_input_password.press("Enter")

    def go_to_signup(self):
        self.page.get_by_text("Don't have an account?").wait_for(timeout=5000)
        self.page.get_by_role("button", name="Sign Up").click()
        self.page.get_by_text("Signup", exact=True).wait_for(timeout=5000)
