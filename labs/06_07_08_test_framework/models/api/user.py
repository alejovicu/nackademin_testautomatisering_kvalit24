
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.ok:
            self.token = response.json().get("access_token")
        return response

    def signup(self, username, password):
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
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        # Hämta alla produkter
        response = requests.get(f"{self.base_url}/products", headers=headers)
        response.raise_for_status()
        products = response.json()

        # Hitta produkten med rätt namn
        product_to_assign = next(
            (p for p in products if p.get("name") == product_name), None)
        if not product_to_assign:
            raise ValueError(f"Product '{product_name}' not found")

        product_id = product_to_assign.get("id")

        # Tilldela produkten till användaren
        assign_response = requests.post(
            f"{self.base_url}/user/product/{product_id}", headers=headers
        )
        return assign_response

    def remove_product_from_user(self, product_name):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {"product": product_name}
        response = requests.delete(
            f"{self.base_url}/user/products", json=body, headers=headers)
        return response