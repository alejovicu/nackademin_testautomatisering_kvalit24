
import libs.utils
from models.ui.home import HomePage
from models.ui.signup import SignupPage

class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        username = libs.utils.generate_string_with_prefix()
        password = "test_1234?"

        home = HomePage(self.page)
        signup = SignupPage(self.page)

        home.navigate()
        home.go_to_signup()

        signup.signup(username, password)
        signup.go_to_home()

        home.login(username, password)

        return username, password
