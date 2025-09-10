# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

import requests
from models.api.base import BaseAPI

class UserAPI(BaseAPI):

    def signup(self, username: str, password: str):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response
    
    def get_user_profile(self):
        response = requests.get(f"{self.base_url}/user", headers=self.headers)
        return response
    
    def user_products(self) -> list[dict]:
        response = self.get_user_profile()
        return response.json()["products"]
    
    def num_of_user_products(self) -> int:
        return len(self.user_products())

    def assign_product_to_user(self, product_name: str):
        product_id = self.get_product_id(product_name)
        response = requests.post(f"{self.base_url}/user/products/{product_id}", headers=self.headers)
        return response

    def unassign_product_from_user(self, product_name: str):
        product_id = self.get_product_id(product_name)
        response = requests.delete(f"{self.base_url}/user/product/{product_id}", headers=self.headers)
        return response