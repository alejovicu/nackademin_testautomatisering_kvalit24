# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page, base_url="http://localhost:5173"):
        self.page = page
        self.base_url = base_url

    def navigate(self):
        self.page.goto(f"{self.base_url}/login")
        self.page.wait_for_load_state("networkidle")

    def login(self, username: str, password: str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def expect_logged_in_as(self, username: str):
        expect(self.page.get_by_text(f"Welcome, {username}")).to_be_visible()
