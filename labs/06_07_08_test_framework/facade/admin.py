from models.api.admin import AdminAPI
from models.ui.admin import AdminPage
import os

class AdminFacade:
    def __init__(self, page):
        self.page = page
        self.admin_page = AdminPage(page)
        self.base_url = os.getenv("APP_BACK_URL", "http://localhost:8000")
        self.frontend_url = os.getenv("APP_FRONT_URL", "http://localhost:5173/")
        self.api = AdminAPI(base_url=self.base_url)

    def login_via_token(self):
        self.api.get_admin_token() # call api-model
        self.page.add_init_script("window.localStorage.clear()")
        self.page.add_init_script(f""" window.localStorage.setItem('token', '{self.api.token}')""") # put token directly in local storage
        self.page.goto(self.frontend_url, wait_until="domcontentloaded") # load frontend


    def create_product_for_test_via_api(self, product_name):
        response = self.api.create_product(product_name)
        assert response.status_code == 200, "Failed to create product via API"
        self.page.goto(self.frontend_url) # update page to see new product
        return product_name