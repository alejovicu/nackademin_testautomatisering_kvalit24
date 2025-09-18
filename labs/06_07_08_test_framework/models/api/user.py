import requests

# View where an user (non admin) can Choose
# products from the Product Catalog and/or remove it


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def set_token(self, token: str):
        self.token = token

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response.json()

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        self.token = response.json()["access_token"]
        return response.json()

    def get_user_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/user", headers=headers)
        return response.json()

    def add_product_to_user(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        products = requests.get(f"{self.base_url}/products", headers=headers).json()
        for product in products:
            if product["name"] == product_name:
                return requests.post(
                    f"{self.base_url}/user/products/{product['id']}", headers=headers
                )

        return None

    def remove_product_from_user(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        products = requests.get(f"{self.base_url}/products", headers=headers).json()
        for product in products:
            if product["name"] == product_name:
                return requests.delete(
                    f"{self.base_url}/user/products/{product['id']}", headers=headers
                )

        return None
