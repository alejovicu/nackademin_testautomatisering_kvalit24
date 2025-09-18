# Page where the users could either create a new user or
# navigate to Home
class SignupPage:
    def __init__(self, page):
        self.page = page

        self.signup_input_username = page.get_by_placeholder('Username')
        self.signup_input_password = page.get_by_placeholder('Password')
        self.signup_btn_signup = page.locator('button.button-primary')
        self.signup_btn_login = page.locator('button.btn-blue')
<<<<<<< HEAD
        
=======
>>>>>>> 3edf30ae5023c79809e3dfcba1c96cc54596bd9c


    def signup(self,username,password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_signup.click()

    def go_to_home(self):
<<<<<<< HEAD
        self.signup_btn_login.click()
        # complete code
        
=======
        # complete code
>>>>>>> 3edf30ae5023c79809e3dfcba1c96cc54596bd9c
