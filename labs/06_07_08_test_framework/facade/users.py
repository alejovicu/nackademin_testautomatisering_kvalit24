import libs.utils

from models.home import HomePage
from models.signup import SignupPage

class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        # Complete code
        # generate username
        # navigate to signup
        # create new user
        # navigate to login
        # login as new user
        # return username and password
        username = libs.utils.generate_string_with_prefix("user")
        password = "Password123!"
        home_page = HomePage(self.page)
        home_page.navigate()
        home_page.go_to_signup()
        signup_page = SignupPage(self.page)
        signup_page.signup(username, password)
        home_page.navigate()
        home_page.login(username, password)
        return username, password
        # return username and password
        return username, password
    
    