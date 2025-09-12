import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        return response

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response

    def add_product_to_user(self, access_token, product_id):
        token = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(
            f"{self.base_url}/user/products/{product_id}", headers=token
        )
        return response

    def remove_product_from_user(self, access_token, product_id):
        token = {"Authorization": f"Bearer {access_token}"}
        response = requests.delete(
            f"{self.base_url}/user/product/{product_id}", headers=token
        )
        return response

    def get_products_from_user(self, access_token):
        token = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{self.base_url}/user", headers=token)
        return response
