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
        # complete code
        return None

    def remove_product_from_user(self, product_name):
        # complete code
        return None