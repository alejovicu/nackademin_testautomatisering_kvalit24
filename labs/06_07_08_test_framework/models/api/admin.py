import requests

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_current_product_count(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        if response.status_code == 200:
            return len(response.json())
        return 0

    def create_product(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        body = {"name": product_name}
        response = requests.post(
            f"{self.base_url}/product",
            json=body,
            headers=headers
        )
        return response

    def delete_product_by_name(self, product_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        if response.status_code == 200:
            products = response.json()
            for product in products:
                if product['name'] == product_name:
                    delete_response = requests.delete(
                        f"{self.base_url}/product/{product['id']}",
                        headers=headers
                    )
                    return delete_response
        return None