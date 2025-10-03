
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if hasattr(self, "token") and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        response.raise_for_status()
        data = response.json()
        self.token = data.get("access_token")
        return response

    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response


    def add_product_to_user(self, product_id):
        url = f"{self.base_url}/user/product/{product_id}"
        response = requests.post(url, headers=self._headers())
        response.raise_for_status()
        return response.status_code == 200
        

    def remove_product_from_user(self, product_id):
        url = f"{self.base_url}/user/product/{product_id}"
        response = requests.delete(url, headers=self._headers())
        response.raise_for_status()
        return response.status_code == 200