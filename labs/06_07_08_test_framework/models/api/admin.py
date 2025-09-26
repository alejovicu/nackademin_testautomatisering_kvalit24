import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.session = requests.Session()

    def login(self, username, password):
        body = {"username": username, "password": password}
        r = self.session.post(f"{self.base_url}/login", json=body)
        if r.status_code != 200:
            # На чистой БД может не быть пользователя admin — создадим и повторим логин
            self.session.post(f"{self.base_url}/signup", json=body)
            r = self.session.post(f"{self.base_url}/login", json=body)

        assert r.status_code == 200, f"Admin login failed: {r.status_code} {r.text}"
        data = r.json()
        token = data.get("access_token") or data.get("token")
        assert token, f"No token in login response: {data}"
        self.session.headers["Authorization"] = f"Bearer {token}"

    def list_products(self):
        response = self.session.get(f"{self.base_url}/products")
        data = response.json()
        return [p["name"] for p in data]

    def create_product(self, product_name):
        body = {"name": product_name}
        return self.session.post(f"{self.base_url}/products", json=body)

    def delete_product_by_name(self, product_name):
        products = self.session.get(f"{self.base_url}/products").json()
        for product in products:
            if product["name"] == product_name:
                return self.session.delete(f"{self.base_url}/product/{product['id']}")
        return None

    def get_current_product_count(self):
        return len(self.list_products())
