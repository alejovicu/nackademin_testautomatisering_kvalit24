class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_header_main_title = page.get_by_text('Nackademin Course App') 
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_button = page.get_by_role("button", name="Login")

   
    def login(self,username,password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_button.click()