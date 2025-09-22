import requests

def get_current_product_count(self):
    response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
    response.raise_for_status()
    return len(response.json())

def create_product(self, product_name):
    response = requests.post(
        f"{self.base_url}/products",
        headers={"Authorization": f"Bearer {self.token}"},
        json={"name": product_name}
    )
    response.raise_for_status()
    return response.json()

def delete_product_by_name(self, product_name):
    response = requests.delete(
        f"{self.base_url}/products/{product_name}",
        headers={"Authorization": f"Bearer {self.token}"}
    )
    response.raise_for_status()