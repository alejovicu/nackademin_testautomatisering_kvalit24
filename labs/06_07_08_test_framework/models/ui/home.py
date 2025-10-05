from playwright.sync_api import expect
import os

class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = os.getenv("FRONTEND_URL", "http://localhost")
        self.login_header_main_title = page.get_by_text('Nackademin Course App')
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator('button.button-primary')
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator('#signup')


    def navigate(self):
        self.page.goto(self.url)


    def login(self, username, password):

        self.page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))
        self.page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        try:
            self.login_input_username.fill(username)
            self.login_input_password.fill(password)
            self.login_btn_login.click()
            
            # Wait longer to see if anything happens
            self.page.wait_for_timeout(3000)
            
            # Check for error messages
            page_content = self.page.content()
            if "Invalid" in page_content or "error" in page_content.lower():
                print(f"Found error on page: {page_content}")
            
            # Print current state
            print(f"Current URL: {self.page.url}")
            print(f"Is login form still visible? {self.login_input_username.is_visible()}")
            
            # Check what's on the page
            body_text = self.page.locator("body").inner_text()
            print(f"Page text: {body_text[:500]}")
            
            self.page.wait_for_load_state("networkidle")
            expect(self.page.get_by_text("Welcome", exact=False)).to_be_visible(timeout=10000)
        except Exception as e:
            screenshot_dir = "/var/jenkins_home/workspace/Jenkins lab_13_14 integration and e2e/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            self.page.screenshot(path=os.path.join(screenshot_dir, f"login_{username}.png"))
            raise e


    def go_to_signup(self):
        self.login_btn_signup.click()