import requests


class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_product_list(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        return response.json()

    def get_current_product_count(self):
        products = self.get_product_list()
        return len(products)

    def create_product(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/product", json=body, headers=headers)
        self.status_code = response.status_code
        return response.json()

    def search_product_id(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        products = response.json()

        for product in products:
            if product.get("name") == product_name:
                return product.get("id")

        raise Exception("Product not found")

    def delete_product_by_name(self, product_name):
        product_id = self.search_product_id(product_name)

        headers = {"Authorization": f"Bearer {self.token}"}
        body = {"name": product_name}
        response = requests.delete(
            f"{self.base_url}/product/{product_id}", json=body, headers=headers
        )
        self.status_code = response.status_code
        return response.json()
