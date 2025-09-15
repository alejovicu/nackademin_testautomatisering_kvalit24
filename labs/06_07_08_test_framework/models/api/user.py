import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def login(self, username, password):
        resp = requests.post(
            f"{self.base_url}/login",
            json={"username": username, "password": password}
        )
        resp.raise_for_status()
        self.token = resp.json().get("access_token")
        if self.token:
            self.headers = {"Authorization": f"Bearer {self.token}"}
        return self.token
    

    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response


    # this one should not have been implemented I guess. since it doesnt work the way it should be intended as.
    def add_product_to_user(self, product, token):
        body = { "name": product}
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(f"{self.base_url}/products", json=body, headers=headers)
        return response


    # this one should not have been implemented I guess. since it doesnt work the way it should be intended as.
    def remove_product_from_user(self, product_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(f"{self.base_url}/product/{product_id}", headers=headers)
        return response