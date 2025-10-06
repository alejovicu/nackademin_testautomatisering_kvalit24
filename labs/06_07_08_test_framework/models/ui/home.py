# Landing page where the users could either login or
# navigate to signup
from config import FRONTEND_URL
import time
class HomePage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
       
        self.page_title = self.page.get_by_text('Nackademin Course App')
        self.login_input_username = self.page.get_by_placeholder('Username')
        self.login_input_password = self.page.get_by_placeholder('Password')
        self.login_btn_login = self.page.locator('button.button-primary')
        
        self.login_label_have_account = self.page.get_by_text("Don't have an account?")
        self.login_btn_signup = self.page.locator('#signup')

        # Post-login elements
        self.header = self.page.locator("text=Welcome") 
        self.products_section_title = self.page.locator("h3:has-text('Your Products:')")
        self.no_products_text = self.page.locator("p:has-text('No products assigned.')")
        self.header = self.page.get_by_role("heading", name="Welcome,User!")
        self.logout_button = self.page.get_by_role("button", name="Log out")


    def navigate(self):
        self.page.goto(FRONTEND_URL)
        self.page.wait_for_load_state("networkidle")

        
       

    def login(self,username,password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()
        time.sleep(0.5)
        self.page.wait_for_load_state("networkidle")

    def go_to_signup(self):
        # complete code
        self.login_btn_signup.click()
        self.page.wait_for_load_state("networkidle")