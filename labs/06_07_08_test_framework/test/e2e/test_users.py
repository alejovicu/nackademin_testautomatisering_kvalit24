from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import libs.utils


def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()

    signup_page = SignupPage(page)
    
    # Vänta på signup response
    with page.expect_response(lambda r: r.url.endswith("/signup") and r.status == 200):
        signup_page.signup(username, password)

    signup_page.go_to_home()
    home_page.login(username, password)
    
    # Verifiera att login lyckades
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()


def test_login(page: Page):
    username = "user"
    password = "1234"
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    
    # Verifiera att admin är inloggad (ändra detta beroende på vad som visas för admin)
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()