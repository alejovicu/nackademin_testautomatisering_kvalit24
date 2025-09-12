import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_current_product_count(self, access_token):
        token = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{self.base_url}/products", headers=token)
        products = response.json()
        total_products = len(products)
        return total_products

    def create_product(self, access_token, product_name):
        token = {"Authorization": f"Bearer {access_token}"}
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/products", headers=token, json=body)
        return response

    def delete_product_by_id(self, access_token, product_id):
        token = {"Authorization": f"Bearer {access_token}"}
        response = requests.delete(
            f"{self.base_url}/product/{product_id}", headers=token
        )
        return response

    def get_current_products(self, access_token):
        token = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{self.base_url}/products", headers=token)
        products = response.json()
        return products
