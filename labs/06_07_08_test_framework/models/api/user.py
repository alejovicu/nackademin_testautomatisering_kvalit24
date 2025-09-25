import requests
class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        body = { "username": username, "password": password }
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.ok:
            self.token = response.json().get("access_token")
        return response

    def signup(self, username, password):
        body = { "username": username, "password": password }
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response

    def get_user_details(self, token):
        headers = {
            "Authorization": f"Bearer {token}",
            "accept": "application/json"
        }
        return requests.get(f"{self.base_url}/user", headers=headers)

    def add_product_to_user(self, product_name):
        # complete code
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {"product": product_name}
        response = requests.post(
            f"{self.base_url}/user/products", json=body, headers=headers)
        return response

    def remove_product_from_user(self, product_name):
        # complete code 
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {"product": product_name}
        response = requests.delete(
            f"{self.base_url}/user/products", json=body, headers=headers)
        return response