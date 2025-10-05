import libs.utils
from models.ui.home import HomePage
from models.ui.signup import SignupPage

class UsersFacade:
    def __init__(self, page):
        self.page = page

    def login_as_new_user(self, base_url="http://app-frontend:5173"):
        username = libs.utils.generate_string_with_prefix("testuser")
        password = "Test123!@#"
        
        home_page = HomePage(self.page)
        signup_page = SignupPage(self.page)
        
        home_page.navigate(base_url)
        home_page.go_to_signup()
        signup_page.signup(username, password)
        self.page.wait_for_timeout(2000)
        signup_page.go_to_home()
        home_page.login(username, password)
        
        return username, password