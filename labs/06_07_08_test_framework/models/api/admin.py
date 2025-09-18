<<<<<<< HEAD
import requests

=======
>>>>>>> 3edf30ae5023c79809e3dfcba1c96cc54596bd9c

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

<<<<<<< HEAD
    def get_current_product_count(self):
        # complete logic
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{self.base_url}/products", headers=headers)
        return response
=======


    def get_current_product_count(self):
        # complete logic
>>>>>>> 3edf30ae5023c79809e3dfcba1c96cc54596bd9c
        # return number of total products displayed

    def create_product(self, product_name):
        # complete logic
<<<<<<< HEAD
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {"name": product_name}
        response = requests.post(
            f"{self.base_url}/products", json=body, headers=headers)

        product_id = response.json().get("id")
        return response, product_id

    def delete_product_by_name(self, product_name):

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.get(f"{self.base_url}/products", headers=headers)
        response.raise_for_status()
        products = response.json()

        product_to_delete = next(
            (p for p in products if p.get("name") == product_name), None)
        if not product_to_delete:
            return None

        product_id = product_to_delete.get("id")
        delete_response = requests.delete(
            f"{self.base_url}/products/{product_id}", headers=headers)
        return delete_response
=======

    def delete_product_by_name(self, product_name):
        # complete logic
>>>>>>> 3edf30ae5023c79809e3dfcba1c96cc54596bd9c
