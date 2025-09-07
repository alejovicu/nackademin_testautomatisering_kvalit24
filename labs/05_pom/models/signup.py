
class SignupPage:
    
    def __init__(self, page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.button_signup = page.locator("button.button-primary")
        self.label_have_account = page.get_by_text("Already have an account?")
        self.button_login = page.locator("button.btn-blue")

    
    def navigate(self):
        self.page.goto("http://localhost:5173/signup")


    def signup(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.button_signup.click()