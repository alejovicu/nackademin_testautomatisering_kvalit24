import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.token = response.json()['access_token']
        return response

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response

    def get_user_info(self):
        if not self.token:
            raise Exception("Not authenticated. Call login() first.")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/user", headers=headers)
        return response

    def add_product_to_user(self, product_id):
        if not self.token:
            raise Exception("Not authenticated. Call login() first.")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(
            f"{self.base_url}/user/product/{product_id}",
            headers=headers
        )
        return response

    def remove_product_from_user(self, product_id):
        if not self.token:
            raise Exception("Not authenticated. Call login() first.")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.delete(
            f"{self.base_url}/user/product/{product_id}",
            headers=headers
        )
        return response