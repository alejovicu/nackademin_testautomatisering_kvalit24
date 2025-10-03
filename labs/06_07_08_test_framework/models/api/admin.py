import requests
class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_current_product_count(self):
        # Logic to fetch the current product count
        response = requests.get(f"{self.base_url}/product", headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return len(response.json())  # Assuming the API returns a list of products

    def create_product(self, product_name):
        # Logic to create a product
        response = requests.post(
            f"{self.base_url}/product",
            json={"name": product_name},
            headers={"Authorization": f"Bearer {self.token}"}
        )
        response.raise_for_status()
        return response.json()

    def delete_product_by_name(self, product_name):
        # Logic to delete a product by name
        response = requests.delete(
            f"{self.base_url}/product/{product_name}",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        response.raise_for_status()