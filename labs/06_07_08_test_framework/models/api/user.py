# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        # complete code
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        return response

    def login_token(self, username, password):
        # complete code
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        # set token to object
        token = response.json().get("access_token")
        # return token
        return token

    def signup(self, username, password):
        # complete code
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response
        # return username and password

    def user_profile(self, user_token):
        token = {
            "Authorization": f"Bearer {user_token}",
            "Content-Type": "application/json",
        }
        response = requests.get(f"{self.base_url}/user", headers=token)
        # {
        # "username": "user",
        # "id": 1,
        # "products": []
        # }
        return response

    def add_product_to_user(self, user_token, product_name):
        product_id = None
        token = {
            "Authorization": f"Bearer {user_token}",
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
        add_product = requests.post(
            f"{self.base_url}/user/products/{product_id}", headers=token
        )
        return add_product

    def remove_product_from_user(self, user_token, product_name):
        product_id = None
        token = {
            "Authorization": f"Bearer {user_token}",
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
                f"{self.base_url}/user/product/{product_id}", headers=token
            )
            print(f"product {product_name} removed.")
            return remove_product
        else:
            print(f"product {product_name} was not found.")
            return
