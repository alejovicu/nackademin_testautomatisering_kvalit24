from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import libs.utils

def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "Test1234"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()

    sign_up = SignupPage(page)
    sign_up.signup(username, password)
    sign_up.go_to_home()
    home_page.login(username, password)
    expect(home_page.login_header_main_title).to_be_visible()

def test_login_admin(page: Page):
    username = "admin"
    password = "1234"
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    expect(home_page.login_header_main_title).to_be_visible()
