import requests
class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def set_admin_token(self, token):
        self.token = token

    def admin_login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)

        if response.status_code == 200:
            self.set_admin_token(response.json().get("access_token"))
        else:
            print(f"Login failed: {response.status_code} - {response.text}")

        return response

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get_all_products(self):
        url = f"{self.base_url}/products"
        response = requests.get(url, headers=self.get_headers())        
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get products: {response.status_code}")
            return []

    def get_current_product_count(self):
        products = self.get_all_products()
        return len(products)

    def create_product_by_api(self, product_name):
        url = f"{self.base_url}/product"
        payload = {"name": product_name}
        response = requests.post(url, json=payload, headers=self.get_headers())
        
        if response.status_code == 201:
            print(f"Product '{product_name}' created successfully.")
        else:
            print(f"Failed to create product '{product_name}': {response.status_code} - {response.text}")
        
        return response

    def delete_product_by_id(self, product_id):
        url = f"{self.base_url}/product/{product_id}"
        response = requests.delete(url, headers=self.get_headers())

        if response.status_code == 200:
            print(f"Product with ID {product_id} deleted successfully.")
        else:
            print(f"Failed to delete product ID {product_id}: {response.status_code} - {response.text}")

        return response   