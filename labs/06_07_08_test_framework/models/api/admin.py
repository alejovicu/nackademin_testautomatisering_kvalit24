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
        body = {"name":product_name}
        response = requests.post(f"{self.base_url}/products", json=body, headers = self.headers)
        return response
    
    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers = self.headers)
        return response
         
    #i chose to delete by id instead of by name
    def delete_product_by_id(self, product_id):
        response = requests.delete(f"{self.base_url}/product/{product_id}", headers = self.headers)
        return response