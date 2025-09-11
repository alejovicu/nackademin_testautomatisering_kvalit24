from libs.utils import get_admin_token
from models.api.admin import AdminAPI
from models.ui.admin import AdminPage

class AdminFacade:
    def __init__(self, page):
        self.page = page
        self.admin_page = AdminPage(page)
        self.token = None

    
    def login_via_token(self):
        self.token = get_admin_token() # Uses function from utils to log in as admin and return token
        self.page.add_init_script(f""" window.localStorage.setItem('token', '{self.token}')""")
        self.page.goto("http://localhost:5173/")

    def create_product_for_test_via_api(self, product_name):
        api = AdminAPI(base_url="http://localhost:8000", token=self.token)
        response = api.create_product(product_name)
        assert response.status_code == 200, "Failed to create product via API"
        self.page.goto("http://localhost:5173/")
        return product_name