import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url

        self.session = requests.Session()
        self.token = None

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        self.status_code = response.status_code 
        response.raise_for_status()
        data = response.json()
        self.token = data.get("token") or data.get("access_token") or data.get("jwt")
        return response

    def create_product(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        body = {"name": product_name}
        return self.session.post(f"{self.base_url}/product", headers=headers, json=body)
    
    def find_product(self, product_name):
        return self.product_list.filter(has_text=product_name)

    def list_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        products = response.json()

        return products


    def delete_product_by_name(self, product_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        delete_product_response = requests.delete(f"{self.base_url}/product/{product_id}", headers=headers)

        return delete_product_response
