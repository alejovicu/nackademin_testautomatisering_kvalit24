
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignUpPage

class AuthFacade:
    def __init__(self, page):
        self.page = page
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)
        self.signup_page = SignUpPage(page)

    # FLÖDE FÖR SIGN-UP --> LOGIN
    def signup_and_login(self, username, password):
        self.home_page.navigate()

        self.login_page.navigate_to_signup()
        self.signup_page.signup(username, password)

        self.signup_page.navigate_to_login()
        self.login_page.login(username, password)