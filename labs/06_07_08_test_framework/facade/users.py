from libs.utils import generate_string_with_prefix

from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.api.user import UserAPI
import os


class UsersFacade:
    def __init__(self, page):
        self.page = page
        self.signup_page = SignupPage(page)
        self.login_page = HomePage(page)

        self.base_url = os.getenv("APP_BACK_URL", "http://localhost:8000")
        self.frontend_url = os.getenv("APP_FRONT_URL", "http://localhost:5173/")
        self.user_api = UserAPI(self.base_url)


    def login_as_new_user(self):
        username = generate_string_with_prefix(prefix="user")
        password = "password123"

        self.login_page.navigate()
        self.login_page.go_to_signup()

        self.signup_page.signup(username, password)

        self.signup_page.go_to_home()

        self.login_page.login(username, password)
        return username, password
    

    def login_via_token(self, username, password):
        self.user_api.login(username, password) #call the user API-model's login function
        self.token = self.user_api.token
        self.page.add_init_script(f""" window.localStorage.setItem('token', '{self.token}')""") #script that is run directly in browser local storage
        self.page.goto(self.frontend_url) #go to start page, token is read from localstorage

    
    def get_user_products_names(self):
        response = self.user_api.get_user_products() # GET request from API-model
        return [p["name"] for p in response.json()["products"]] # parse to json, loop each product and extract product name