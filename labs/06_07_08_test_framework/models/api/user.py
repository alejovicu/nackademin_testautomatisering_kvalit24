# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests
class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def set_token(self, token):
        self.token = token

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        
        if response.status_code == 200:
            self.set_token(response.json().get("acces_token"))
    
        return response

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        # complete code
        return response

    def add_product_to_user(self, product_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        response_add_product = requests.post(f"{self.base_url}/user/products/{product_id}", headers=headers)

        return response_add_product
        

    def remove_product_from_user(self, product_id):
        # complete code
        headers = {"Authorization": f"Bearer {self.token}"}
        response_remove_product = requests.delete(f"{self.base_url}/user/product/{product_id}", headers=headers)

        return response_remove_product