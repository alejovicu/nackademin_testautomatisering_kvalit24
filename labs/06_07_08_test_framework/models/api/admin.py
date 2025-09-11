# class AdminAPI:
#     def __init__(self, base_url, token):
#         self.base_url = base_url
#         self.token = token


#     def get_current_product_count(self):
#         # complete logic
#         # return number of total products displayed

#     def create_product(self, product_name):
#         # complete logic

#     def delete_product_by_name(self, product_name):
#         # complete logic
import requests


class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def get_current_product_count(self):
        """Return the total number of products in the system."""
        url = f"{self.base_url}/products"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        products = resp.json()
        return len(products)

    def create_product(self, product_name):
        """Create a new product and return the created product JSON."""
        url = f"{self.base_url}/products"
        payload = {"name": product_name}
        resp = requests.post(url, headers=self.headers, json=payload)
        resp.raise_for_status()
        return resp.json()

    def delete_product_by_name(self, product_name):
        """Delete a product by its name. Return True if deleted, False if not found."""
        url = f"{self.base_url}/products"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        products = resp.json()

        target = next((p for p in products if p.get("name") == product_name), None)
        if not target:
            return False

        product_id = target["id"]
        del_url = f"{self.base_url}/products/{product_id}"
        del_resp = requests.delete(del_url, headers=self.headers)
        del_resp.raise_for_status()
        return True
