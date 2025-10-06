# Landing page where the users could either login or
# navigate to signup
import os

class HomePage:
    def __init__(self, page):
        self.page = page
        #page_(element-type)_(descriptive-name)
        self.login_header_main_title = page.get_by_text('Nackademin Course App') # Locator som hittar sidans huvudtitel via exakt text. Bra för att kolla att rätt sida laddats.
        self.login_input_username = page.get_by_placeholder('Username') # Locators för användarnamn- och lösenordsfältet.
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator('button.button-primary') # Locator för Login-knappen via CSS (button.button-primary).
        self.login_label_have_account = page.get_by_text("Don't have an account?") # Locator för en textetikett på sidan — kan användas som “är sidan rätt?”-check.
        self.login_btn_signup = page.locator('#signup') # Locator för Sign up-knappen via id (#signup).
        self.base_url = os.getenv("FRONTEND_URL", "http://localhost")

    # Öpnnar appen i webbläsaren. Används i början av testet för att komma till startsidan.
    def navigate(self):
        self.page.goto(self.base_url)


    def login(self,username,password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()
        self.page.wait_for_load_state("networkidle")

    def go_to_signup(self):
        self.login_btn_signup.click()
        self.page.wait_for_load_state("networkidle")