# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def user_token(self, token):
        self.token = token

    def login(self, username, password):
        # set token to object

        body = {"username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.user_token(response.json().get("access_token"))

        # return token
        return response

    def signup(self, username, password):
        # complete code
        body = {"username": username, "password": password }
        signup_response = requests.post(f"{self.base_url}/signup", json=body)

        # return username and password
        return signup_response


    def add_product_to_user(self, product_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        product_response = requests.post(f"{self.base_url}/user/product/{product_id}", headers=headers)

        return product_response

    def remove_product_from_user(self, product_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        delete_response = requests.delete(f"{self.base_url}/user/product/{product_id}", headers=headers)

        return delete_response
