import requests
from models.api.base import BaseAPI

class AdminAPI(BaseAPI):

    def get_current_product_count(self) -> int:
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        number_of_products = len(response.json())
        return number_of_products

    def create_product(self, product_name: str):
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/products", json=body, headers=self.headers)
        return response 

    def delete_product_by_name(self, product_name: str):
        product_id = self.get_product_id(product_name)
        response = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        return response