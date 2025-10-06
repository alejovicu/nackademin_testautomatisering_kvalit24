import os


class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_header_main_title = self.page.get_by_text("Nackademin Course App")
        self.login_input_username = self.page.locator("#inp-username")
        self.login_input_password = self.page.locator("#inp-password")
        self.login_btn_login = self.page.locator("#btn-login")
        self.login_label_have_account = self.page.get_by_text("Don't have an account?")
        self.login_btn_signup = self.page.locator("#signup")

    def navigate(self):
        base = os.getenv("FRONTEND_URL", "http://app-frontend:5173").strip().rstrip("/")
        if "#/login" not in base:
            base = f"{base}/#/login"
        self.page.goto(base, wait_until="domcontentloaded")
        self.page.wait_for_selector(
            "#inp-username, input[placeholder='Username'], input[name='username']",
            timeout=10000,
        )

    def login(self, username: str, password: str):
        self.page.fill("#inp-username", username)
        self.page.fill("#inp-password", password)
        self.login_btn_login.click()

        self.page.wait_for_load_state("networkidle")

    def go_to_signup(self):
        self.page.get_by_text("Don't have an account?").wait_for(timeout=5000)
        self.page.get_by_role("button", name="Sign Up").click()
        self.page.get_by_text("Signup", exact=True).wait_for(timeout=5000)
