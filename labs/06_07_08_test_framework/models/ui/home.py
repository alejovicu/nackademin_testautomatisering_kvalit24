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

    def login(self, username: str, password: str):
        self.page.fill(
            "#inp-username, input[placeholder='Username'], input[name='username']",
            username,
        )
        self.page.fill(
            "#inp-password, input[placeholder='Password'], input[name='password']",
            password,
        )

        with self.page.expect_response(
            lambda r: r.request.method == "POST" and "/login" in r.url,
            timeout=12000,
        ) as resp_info:
            self.page.get_by_role("button", name="Login").first.click()
        resp = resp_info.value
        if not (200 <= resp.status < 300):
            raise TimeoutError(f"Login failed, status: {resp.status}")

        logout = self.page.locator(
            "button:has-text('Logout'), a:has-text('Logout')"
        ).first
        try:
            logout.wait_for(state="visible", timeout=5000)
            return
        except:
            pass
        try:
            self.page.get_by_role("button", name="Add Product").wait_for(timeout=7000)
            return
        except:
            pass
        try:
            self.page.wait_for_url(lambda u: "#/user" in u, timeout=5000)
            return
        except:
            pass

        raise TimeoutError(
            "Login did not reach expected state after successful /login."
        )

    def go_to_signup(self):
        self.page.get_by_text("Don't have an account?").wait_for(timeout=5000)
        self.page.get_by_role("button", name="Sign Up").click()
        self.page.get_by_text("Signup", exact=True).wait_for(timeout=5000)
