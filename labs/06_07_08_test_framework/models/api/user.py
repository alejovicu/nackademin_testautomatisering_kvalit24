# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def _headers(self):
        if not self.token:
            raise ValueError("Token not set. Please login first.")
        return {"Authorization": f"Bearer {self.token}"}


    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        return response

    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response


    def add_product_to_user(self, product_name):
        # add product to user
        requests.post(
            f"{self.base_url}/user/products/{product_name}",
            headers=self.get_headers())
    
        return None
    
    def get_user_products(self):
        # return list of products added to the user
        return requests.get(
            f"{self.base_url}/user/products",
            headers=self.get_headers())
        

    def remove_product_from_user(self, product_name):
        # remove product from user
        requests.delete(
            f"{self.base_url}/user/product/{product_name}",
            headers=self.get_headers())
        return None