import requests
# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
    
    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get("access_token") or data.get("token")
        return response
    
    def signup(self, username, password):
        return requests.post(f"{self.base_url}/signup", json={"username": username, "password": password})
    
    def _headers(self):
        if not self.token:
            raise ValueError("Token missing!")
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
    
    def get_profile(self):
        return requests.get(f"{self.base_url}/user", headers=self._headers())

    def add_product_to_user(self, product_id):
        return requests.post(f"{self.base_url}/user/product/{product_id}", headers=self._headers())
    
    def remove_product_from_user(self, product_id):
        return requests.delete(f"{self.base_url}/user/product/{product_id}", headers=self._headers())

    


