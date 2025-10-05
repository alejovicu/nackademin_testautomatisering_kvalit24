# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
       

    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.token = response.json().get("token")
        return response

    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response
    
    def _get_headers(self):
        if not self.token:
            raise Exception("User not logged in")
        return { "Authorization": f"Bearer {self.token}" }


    def add_product_to_user(self, product_name: str):
       body = { "product_name": product_name }
       response = requests.post(f"{self.base_url}/add_product", json=body,headers=self._get_headers())
       return response
        

    def remove_product_from_user(self, product_name:str):
       response = requests.delete(f"{self.base_url}/delete_product", params={ "product_name": product_name }, headers=self._get_headers())
       return response
    
    def get_user_products(self):
        response = requests.get(f"{self.base_url}/my_products", headers=self._get_headers())
        return response

        