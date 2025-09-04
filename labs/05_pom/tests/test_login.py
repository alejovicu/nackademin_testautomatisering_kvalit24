class Loginpage:
    
    import libs.utils
    
    def __init__(self, page):
        self.page = page
        # page_(element-type)_(descriptive-name)
        self.login_header_main_title = page.get_by_text("Nackademin course app")
        self.login_input_username = page.get_by_placeholder("Username")
        self.login_input_password = page.get_by_placeholder("Password")
        self.login_button_login = page.get_by_locator("button.button-primary") #CSS locator
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_button_login = page.locator("button.signup") #CSS locator


        
    pass
def navigate(self):
    self.page.goto("https://localhost:5173/")

def test_valid_login(page):
    login_page = Loginpage(page)
    page.goto("https://course-app-fe.vercel.app/login")
    assert login_page.login_header_main_title.is_visible()
    assert login_page.login_input_username.is_visible()
    assert login_page.login_input_password.is_visible()
    assert login_page.login_button_login.is_visible()
    assert login_page.login_label_have_account.is_visible()
    assert login_page.login_button_login.is_visible()
    
    login_page.login_input_username.fill("testuser")
    login_page.login_input_password.fill("Test@123")
    login_page.login_button_login.click()
    
    # Add assertion to verify successful login, e.g., check for a specific element on the landing page
    # Example: assert page.get_by_text("Welcome, testuser!").is_visible()

    # Navigate to signup
    po_login.login_btn_signup.click()
    # create a new user
    username = libs.utils.generate_username()
    password = libs.utils.generate_password()

    # navigate to login
    # login with the new user