import libs.utils

from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage


class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self):
        # Complete code
        home_page = HomePage(self.page)
        signup_page = SignupPage(self.page)
        # generate username
        username = libs.utils.generate_string_with_prefix()
        password = "password123"
        # navigate to signup
        home_page.navigate()
        home_page.go_to_signup()
        # create new user
        signup_page.signup(username, password)
        # navigate to login
        signup_page.go_to_home()
        # login as new user
        home_page.login(username, password)
        # return username and password

    def check_product_list(self):
        # Given I am an authenticated user​
        home_page = HomePage(self.page)
        username = "test_user"
        password = "test_password"
        user_page = UserPage(self.page)

        # When I log in into the application​
        home_page.navigate()
        home_page.login(username, password)
        # Then I should see all my products
        products = user_page.get_user_products()
        assert len(products) > 0