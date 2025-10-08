
import requests

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token


    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        response.raise_for_status()
        self.token = response.json().get("access_token")
        return response
    
    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
    
    def get_products(self):
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response.json()

    def get_current_product_count(self):
        
        # return number of total products displayed
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        products = response.json()
        return len(products)

    def create_product(self, product_name):
        
        #cretae product 
        response = requests.post(f"{self.base_url}/products", json={"name": product_name}, headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response.json()

    def delete_product_by_name(self, product_name):
        # complete logic
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        products = response.json()
        for product in products:
            if product["name"] == product_name:
                product_id = product["id"]
                del_response = requests.delete(f"{self.base_url}/products/{product_id}", headers={"Authorization": f"Bearer {self.token}"})
                del_response.raise_for_status()
                return True
        return False

