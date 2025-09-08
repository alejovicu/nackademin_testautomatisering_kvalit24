from models.ui.home import HomePage
from models.ui.signup import SignupPage

class AdminFacade:
    def __init__(self, page):
        self.page = page
        self.signup_page = SignupPage(page)
        self.login_page = HomePage(page)

    # FLÖDE FÖR SIGN-UP --> LOGIN
    def signup_and_login(self, username, password):

        self.login_page.navigate()
        self.login_page.go_to_signup()
        self.signup_page.signup(username, password)
        self.signup_page.go_to_home()
        self.login_page.login(username, password)