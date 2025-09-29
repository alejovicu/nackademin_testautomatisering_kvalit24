from libs.utils import generate_string_with_prefix  # Import utility function
from models.ui.home import HomePage  # Import HomePage class
from models.ui.signup import SignupPage  # Import SignupPage class

class UsersFacade:
    """
    A facade class to handle user-related operations such as signing up and logging in.
    """

    def __init__(self, page):
        """
        Initialize the UsersFacade with a Playwright page instance.

        Args:
            page (Page): The Playwright page instance.
        """
        self.page = page

    def login_as_new_user(self):
        """
        Create a new user, sign up, and log in.

        Returns:
            tuple: A tuple containing the username and password of the new user.
        """
        # Generate a unique username and set a default password
        username = generate_string_with_prefix()
        password = "test_1234?"

        # Navigate to the home page and go to the signup page
        home_page = HomePage(self.page)
        home_page.navigate()
        home_page.go_to_signup()

        # Sign up the new user and navigate to the home page
        signup_page = SignupPage(self.page)
        signup_page.signup(username, password)
        signup_page.go_to_home()

        # Log in with the new user's credentials
        home_page.login(username, password)

        # Return the new user's credentials
        return username, password