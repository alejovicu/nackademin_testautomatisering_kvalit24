from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import libs.utils


def test_signup(page: Page):
    home = HomePage(page)
    home.navigate()
    home.go_to_signup()

    signup = SignupPage(page)
    username = libs.utils.generate_string_with_prefix("user", 8)
    password = libs.utils.generate_string_with_prefix("pw", 12)
    signup.signup(username, password)

    signup.go_to_home()

    home.login(username, password)
    page.reload(wait_until="domcontentloaded")

    expect(page.get_by_text("Your products:"))
