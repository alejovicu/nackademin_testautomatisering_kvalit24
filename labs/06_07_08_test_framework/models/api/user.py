# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        self.status_code = response.status_code

        # set token to object
        self.token = response.json().get("access_token")

        # return token
        return self.token

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        self.status_code = response.status_code
        return response.json()

    def search_product_id(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        products = response.json()

        for product in products:
            if product.get("name") == product_name:
                return product.get("id")

        raise Exception(f"Product {product_name} not found")

    def add_product_to_user(self, product_name):
        # Search product id
        product_id = self.search_product_id(product_name)

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(
            f"{self.base_url}/user/product/{product_id}", headers=headers
        )
        return response.json()

    def display_user_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/user", headers=headers)
        return response.json()

    def remove_product_from_user(self, product_name):
        # Search product id
        product_id = self.search_product_id(product_name)

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.delete(
            f"{self.base_url}/user/product/{product_id}", headers=headers
        )
        return response.json()
