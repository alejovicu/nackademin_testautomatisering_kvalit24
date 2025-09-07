from models.login import LoginPage
from models.signup import SignupPage
from models.home import HomePage
from playwright.sync_api import Page, expect
from libs import utils


# Test valid Login with existing user

def test_valid_login(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate()
    login_page.login("test", "test123")




    expect(page.locator("h2")).to_contain_text("test")


# Test signup and login with new user

def test_signup_new_user(page: Page):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    
    username = utils.generate_username()
    password = utils.generate_password()

    home_page.navigate()
    login_page.navigate_to_signup()
    signup_page.signup(username, password)

    expect(page.locator("button:has-text('Login')")).to_be_visible()


def test_login_new_user(page: Page):
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    login_page = LoginPage(page)

    username = utils.generate_username()
    password = utils.generate_password()

    home_page.navigate()
    login_page.navigate_to_signup()
    signup_page.signup(username, password)

    login_page.navigate()
    login_page.navigate_to_signup()
    signup_page.signup(username, password)

    login_page.navigate()
    login_page.login(username, password)

    
    expect(page.locator("h2")).to_contain_text(username)

   