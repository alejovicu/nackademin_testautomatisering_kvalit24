import libs.utils

from models.home import HomePage
from models.signup import SignupPage


class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        # generate username
        username = libs.utils.generate_string_with_prefix("user", 8)
        password = libs.utils.generate_string_with_prefix("pw", 12)

        # navigate to signup
        home = HomePage(self.page)
        home.navigate()
        home.go_to_signup()

        # create new user
        signup = SignupPage(self.page)
        signup.signup(username, password)

        # navigate to login
        signup.go_to_home()

        # login as new user
        home.login(username, password)

        # return username and password
        return username, password
