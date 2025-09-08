# Implement PO for login
# 2 inputs and 1 button
# Naming example:  input_username

# class LoginPage:
# def __init__(self, page):
#   self.page = page
# self.input_username = page.locator(??)
# self.input_password = page.locator(??)
# self.button_login = page.locator(??)
#  self.button_signup = page.locator("#signup")

# def navigate_to_signup(self):

#  self.button_signup.click()

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(self.app_url + "/login")
        # ensure login button is visible
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()
        return self

    def click_signup_link(self):
        # App.jsx uses <button id='signup'>Sign Up</button> to toggle screens
        self.page.locator("#signup").click()

    def login(self, username: str, password: str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        # wait for the welcome header (should appear after successful login)
        expect(self.page.locator("h2")).to_contain_text("Welcome,")
