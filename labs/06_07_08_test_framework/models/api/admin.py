import requests

class AdminAPI:
    def __init__(self, base_url, token=None, session=None):
        self.base_url = str(base_url).rstrip("/")
        self.session = session or requests.Session()
        self.token = token

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    # -------- READ --------
    def get_product_list(self) -> list:
        resp = self.session.get(self._url("/products"), headers=self._headers())
        resp.raise_for_status()
        return resp.json()

    def get_current_product_count(self) -> int:
        return len(self.get_product_list())

    # -------- CREATE (return Response) --------
    def create_product(self, product_name: str) -> requests.Response:
        body = {"name": product_name}
        resp = self.session.post(self._url("/product"), json=body, headers=self._headers())
        return resp  # test kollar .status_code och ev. .json()

    # -------- DELETE (return Response) --------
    def delete_product_by_name(self, product_name: str) -> requests.Response:
        lst = self.session.get(self._url("/products"), headers=self._headers())
        lst.raise_for_status()
        products = lst.json()
        target = next((p for p in products if p.get("name") == product_name), None)

        if not target or "id" not in target:
            r = requests.Response()
            r.status_code = 404
            r._content = b'{"detail":"not found"}'
            return r

        pid = target["id"]
        resp = self.session.delete(self._url(f"/product/{pid}"), headers=self._headers())
        return resp

    # -------- AUTH helper --------
    def get_admin_token(self, username="admin", password="admin123") -> str:
        login = self.session.post(self._url("/login"), json={"username": username, "password": password})
        if login.status_code == 200:
            self.token = login.json().get("access_token")
            return self.token

        self.session.post(self._url("/signup"), json={"username": username, "password": password})
        login = self.session.post(self._url("/login"), json={"username": username, "password": password})
        login.raise_for_status()
        self.token = login.json().get("access_token")
        return self.token