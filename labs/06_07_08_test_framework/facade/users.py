# import libs.utils

# from models.home import HomePage
# from models.signup import SignupPage

# class UsersFacade:
#     def __init__(self, page):
#         self.page = page

#     def login_as_new_user(self):
#         # Complete code
#         # generate username
#         # navigate to signup
#         # create new user
#         # navigate to login
#         # login as new user
#         # return username and password
import libs.utils
from models.home import HomePage
from models.signup import SignupPage


class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        """
        Creates and logs in as a brand new user via the UI.

        Returns:
            tuple: (username, password) of the new user
        """
        # Generate new credentials
        username = libs.utils.generate_string_with_prefix()
        password = libs.utils.get_test_password()

        # Navigate to home
        home = HomePage(self.page)
        home.navigate()

        # Go to signup
        home.go_to_signup()
        signup = SignupPage(self.page)

        # Create new user
        signup.signup(username, password)

        # Go back to login
        signup.go_to_home()

        # Login with the new credentials
        home.login(username, password)

        return username, password
