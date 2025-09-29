import requests


class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token




    def get_current_product_count(self):
        url = f"{self.base_url}/products"
        headers = {
        "Authorization": f"Bearer {self.token}",
         "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            products = response.json()
            return len(products)
        return 0

    def create_product(self, product_name):
        
        url = f"{self.base_url}/products"
        headers = {
        "Authorization": f"Bearer {self.token}",
         "Content-Type": "application/json"
        }

        body = {"name": product_name}

        response = requests.post(url, headers=headers, json=body)
        return response

    def delete_product_by_name(self, product_name):
        
        url = f"{self.base_url}/products"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None

        products = response.json()
        for product in products:
            if product.get("name") == product_name:
                product_id = product.get("id")
                delete_product = f"{self.base_url}/product/{product_id}"

                response = requests.delete(delete_product, headers=headers)
                return response

        return None  # Om produkten inte hittades

