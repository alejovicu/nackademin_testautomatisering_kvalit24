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
        base = os.getenv("FRONTEND_URL", "http://app-frontend:5173").strip().rstrip("/")
        if "#/login" not in base:
            base = f"{base}/#/login"
        self.page.goto(base, wait_until="domcontentloaded")
        self.page.wait_for_selector(
            "#inp-username, input[placeholder='Username'], input[name='username']",
            timeout=10000,
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
        self.page.get_by_role("button", name="Login").first.click()

        self.page.wait_for_load_state("networkidle")

        targets = [
            self.page.locator("button:has-text('Logout'), a:has-text('Logout')").first,
            self.page.get_by_role("button", name="Add Product"),
            self.page.get_by_text("Your products:", exact=False),
        ]

        deadline = self.page.context._impl_obj._loop.time() + 10  # ~10s общий лимит
        for loc in targets:
            try:
                loc.wait_for(timeout=3000)
                return
            except Exception:
                pass
            if self.page.context._impl_obj._loop.time() > deadline:
                break

        err = self.page.get_by_text("Invalid", exact=False)
        try:
            if err.is_visible():
                raise TimeoutError(
                    "Login failed: invalid credentials or backend error."
                )
        except Exception:
            pass

        raise TimeoutError(
            "Login did not reach expected state (no Logout/Add Product/'Your products:')."
        )

    def go_to_signup(self):
        self.page.get_by_text("Don't have an account?").wait_for(timeout=5000)
        self.page.get_by_role("button", name="Sign Up").click()
        self.page.get_by_text("Signup", exact=True).wait_for(timeout=5000)
