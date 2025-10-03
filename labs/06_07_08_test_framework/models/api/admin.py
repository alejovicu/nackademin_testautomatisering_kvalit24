import requests
import time


class AdminAPI:
    def __init__(
        self,
        base_url,
    ):
        self.base_url = base_url
        # self.token = None

    def set_token(self, token):
        self.token = token

    def get_product_by_name(self, product_name):
        token = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        product_found = None
        find_product = product_name
        response = requests.get(f"{self.base_url}/products", headers=token)
        assert response.status_code == 200
        product_list = response.json()
        for product in product_list:
            if product["name"] == find_product:
                product_found = product["name"]
                print(f"product {product_name} exist on the app.")
                break
        time.wait(1)
        return product_found

    def get_current_product_count(self):  # complete logic
        token = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response = requests.get(f"{self.base_url}/products", headers=token)
        product_list = response.json()
        number_of_products = len(product_list)
        # return number of total products displayed
        return number_of_products

    def create_product(self, product_name):  # complete logic
        token = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/product", json=body, headers=token)
        return response

    def delete_product_by_name(self, product_name):  # complete logic
        product_id = None
        token = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        find_product = product_name
        response = requests.get(f"{self.base_url}/products", headers=token)
        assert response.status_code == 200
        product_list = response.json()
        for product in product_list:
            if product["name"] == find_product:
                product_id = product["id"]
                break
        if product_id is not None:
            remove_product = requests.delete(
                f"{self.base_url}/product/{product_id}", headers=token
            )
            print(f"product {product_name} removed.")
            return remove_product
        else:
            print(f"product {product_name} was not found.")
            return
