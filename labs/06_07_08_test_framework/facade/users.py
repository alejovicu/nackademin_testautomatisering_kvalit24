import libs.utils

from models.home import HomePage
from models.signup import SignupPage


class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        # Generate fake user data
        user_data = libs.utils.generate_fake_user()
        username = user_data["username"]
        password = user_data["password"]

        # Navigate to signup page and create a new user
        signup_page = SignupPage(self.page)
        signup_page.goto()
        signup_page.signup(username=username, password=password)

        # Navigate to login page and log in
        home_page = HomePage(self.page)
        home_page.goto_login()
        home_page.login(username=username, password=password)

        # Return the new user's credentials for test verification
        return username, password
