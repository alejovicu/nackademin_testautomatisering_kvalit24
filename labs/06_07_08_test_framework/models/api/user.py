import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.token = response.json()["access_token"]
        return response

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response

    def add_product_to_user(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(f"{self.base_url}/products", headers=headers)
        if r.status_code != 200:
            return r
        products = r.json() or []
        for product in products:
            if product.get("name") == product_name:
                return requests.post(
                    f"{self.base_url}/user/product/{product['id']}", headers=headers
                )
        return None

    def remove_product_from_user(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        products = requests.get(f"{self.base_url}/products", headers=headers).json()
        for product in products:
            if product["name"] == product_name:
                return requests.delete(
                    f"{self.base_url}/user/product/{product['id']}", headers=headers
                )
        return None
