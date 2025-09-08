# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        # complete code
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        return response

    def login_token(self, username, password):
        # complete code
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        # set token to object
        token = response.json().get("access_token")
        # return token
        return token

    def signup(self, username, password):
        # complete code
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response
        # return username and password

    def user_profile(self, user_token):
        token = {
            "Authorization": f"Bearer {user_token}",
            "Content-Type": "application/json",
        }
        response = requests.get(f"{self.base_url}/user", headers=token)
        # {
        # "username": "Admin_user",
        # "id": 1,
        # "products": []
        # }
        return response

    def add_product_to_user(self, product_name):
        # complete code
        pass

    def remove_product_from_user(self, product_name):
        # complete code
        pass
