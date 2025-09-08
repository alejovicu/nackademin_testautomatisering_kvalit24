from libs.utils import generate_string_with_prefix

from models.ui.home import HomePage
from models.ui.signup import SignupPage

class UsersFacade:
    def __init__(self, page):
        self.page = page
        self.signup_page = SignupPage(page)
        self.login_page = HomePage(page)

    def login_as_new_user(self):
        # generate username
        username = generate_string_with_prefix(prefix="user")
        password = "password123"

        # navigate to signup
        self.login_page.navigate()
        self.login_page.go_to_signup()

        # create new user
        self.signup_page.signup(username, password)

        # navigate to login
        self.signup_page.go_to_home()

        # login as new user
        self.login_page.login(username, password)

        # return username and password
        return username, password