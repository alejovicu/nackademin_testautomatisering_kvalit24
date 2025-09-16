from models.api.admin import AdminAPI
from models.ui.admin import AdminPage

class AdminFacade:
    def __init__(self, page, base_url="http://localhost:8000", frontend_url="http://localhost:5173/"):
        self.page = page
        self.admin_page = AdminPage(page)
        self.base_url = base_url
        self.frontend_url = frontend_url
        self.api = AdminAPI(base_url=base_url)

    
    def login_via_token(self):
        self.api.get_admin_token() # call api-model
        self.page.add_init_script(f""" window.localStorage.setItem('token', '{self.api.token}')""") # put token directly in local storage
        self.page.goto(self.frontend_url) # load frontend


    def create_product_for_test_via_api(self, product_name):
        response = self.api.create_product(product_name)
        assert response.status_code == 200, "Failed to create product via API"
        self.page.goto(self.frontend_url) # update page to see new product
        return product_name