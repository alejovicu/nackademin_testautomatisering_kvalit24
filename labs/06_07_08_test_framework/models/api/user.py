# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        # complete code
        # set token to object
        # return token

    def signup(self):
        # complete code
        # return username and password

    def add_product_to_user(self, product_name):
        # complete code

    def remove_product_from_user(self, product_name):
        # complete code