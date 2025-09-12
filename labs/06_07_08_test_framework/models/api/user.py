import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        url = f"{self.base_url}/login"
        response = requests.post(url, json={"username": username, "password": password})
        if response.status_code == 200:
            self.token = response.json().get("access_token")
        return response

    def signup(self, username, password):
        url = f"{self.base_url}/signup"
        body = {"username": username, "password": password}
        response = requests.post(url, json=body)
        return response

    def add_product_to_user(self, product_id):
        url = f"{self.base_url}/user/products/{product_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers)
        return response

    def remove_product_from_user(self, product_id):
        url = f"{self.base_url}/user/product/{product_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.delete(url, headers=headers)
        return response
