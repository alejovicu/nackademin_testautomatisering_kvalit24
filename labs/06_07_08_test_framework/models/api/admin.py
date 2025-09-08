class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url

    def set_token(self, token):
        self.token = token

    def get_current_product_count(self):
        # complete logic
        # return number of total products displayed
        pass

    def create_product(self, product_name):  # complete logic
        token = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        pass

    def delete_product_by_name(self, product_name):
        # complete logic
        pass
