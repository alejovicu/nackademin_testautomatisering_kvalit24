
#class AdminAPI:
    #def __init__(self, base_url, token):
        #self.base_url = base_url
        #self.token = token



    #def get_current_product_count(self):
        # complete logic
        # return number of total products displayed

    #def create_product(self, product_name):
        # complete logic

    #def delete_product_by_name(self, product_name):
        # complete logic

# models/api/admin.py

import requests

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_current_product_count(self):
        url = f"{self.base_url.rstrip('/')}/product"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        products = response.json()
        return len(products)

    def create_product(self, product_name):
        url = f"{self.base_url}/product"
        body = {"name": product_name}
        response = requests.post(url, json=body, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete_product_by_id(self, product_id):
        url = f"{self.base_url}/product/{product_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return response.status_code == 200

    def delete_product_by_name(self, product_name):
        # Get all products
        url = f"{self.base_url}/products"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        products = response.json()

        matching = next((p for p in products if p["name"] == product_name), None)
        if not matching:
            return False
        return self.delete_product_by_id(matching["id"])
