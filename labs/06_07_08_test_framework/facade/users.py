import libs.utils

from models.home import HomePage
from models.signup import SignupPage

class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        
        # generate username
        username = libs.utils.generate_string_with_prefix("user")
        password = "testtest123"

        # navigate to signup
        signup_page = SignupPage(self.page)

        # create new user
        signup_page.signup(username, password)

        # navigate to login
        signup_page.go_to_home()
        home_page = HomePage(self.page)
        home_page.go_to_login()

        # login as new user
        home_page.login(username, password)

        # return username and password
        return username, password