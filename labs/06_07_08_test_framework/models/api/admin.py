import requests

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token


    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}" if self.token else "",
            "Content-Type": "application/json",
        }
    
    def create_product(self, product_name):
        # complete logic
        body = {"name":product_name}
        response = requests.post(f"{self.base_url}/product", json=body, headers = self.headers)
        return response
    
    def get_product_id(self, product_name: str) -> int | None:
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        products = response.json()
        for product in products:
            if product["name"] == product_name:
                return product["id"]
        return None


    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers = self.headers)
        return response

    #i chose to delete by id instead of by name
    def delete_product_by_id(self, product_id):
        response = requests.delete(f"{self.base_url}/product/{product_id}", headers = self.headers)
        return response
    
    def delete_product_by_name(self, product_name: str):
        product_id = self.get_product_id(product_name)
        response = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        return response
    
    