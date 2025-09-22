# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        return response

    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response


    def add_product_to_user(self, product_name):
        response = requests.post(
        f"{self.base_url}/user/products",
        json={"product_name": product_name}
    )
        response.raise_for_status()
        return response.json()

    def remove_product_from_user(self, product_name):
        response = requests.delete(
        f"{self.base_url}/user/products/{product_name}"
    )
        response.raise_for_status()
        return response.json()