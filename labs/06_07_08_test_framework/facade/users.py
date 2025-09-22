import libs.utils

from models.home import HomePage
from models.signup import SignupPage

class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        username = libs.utils.generate_string_with_prefix()
        password = "test_1234?"

        home_page = HomePage(self.page)
        home_page.navigate()
        home_page.go_to_signup()

        signup_page = SignupPage(self.page)
        signup_page.signup(username, password)
        signup_page.go_to_home()

        home_page.login(username, password)
        return username, password