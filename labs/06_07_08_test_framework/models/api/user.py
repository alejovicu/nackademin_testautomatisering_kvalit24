# # View where an user (non admin) can Choose
# # produts from the Product Catalog and/or
# # remove it
# import requests


# class UserAPI:
#     def __init__(self, base_url):
#         self.base_url = base_url

#     def login(self, username, password):
#         body = {"username": username, "password": password}
#         response = requests.post(f"{self.base_url}/login", json=body)
#         return response

#     def signup(self, username, password):
#         body = {"username": username, "password": password}
#         response = requests.post(f"{self.base_url}/signup", json=body)
#         return response

#     def add_product_to_user(self, product_name):
#         # complete code
#         return None

#     def remove_product_from_user(self, product_name):
#         # complete code
#         return None
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.token = None
        self.headers = {}

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.ok:
            data = response.json()
            self.token = data.get("access_token")
            if self.token:
                self.headers = {
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/json",
                }
        return response

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response

    def add_product_to_user(self, product_name):
        """Assign a product to the current user by product name."""
        # Fetch products
        resp = requests.get(f"{self.base_url}/products", headers=self.headers)
        resp.raise_for_status()
        products = resp.json()

        target = next((p for p in products if p.get("name") == product_name), None)
        if not target:
            raise ValueError(f"Product '{product_name}' not found")

        product_id = target["id"]
        url = f"{self.base_url}/user/products/{product_id}"
        resp = requests.post(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def remove_product_from_user(self, product_name):
        """Remove a product from the current user by product name."""
        # Fetch products
        resp = requests.get(f"{self.base_url}/products", headers=self.headers)
        resp.raise_for_status()
        products = resp.json()

        target = next((p for p in products if p.get("name") == product_name), None)
        if not target:
            raise ValueError(f"Product '{product_name}' not found")

        product_id = target["id"]
        url = f"{self.base_url}/user/products/{product_id}"
        resp = requests.delete(url, headers=self.headers)
        resp.raise_for_status()
        return True
