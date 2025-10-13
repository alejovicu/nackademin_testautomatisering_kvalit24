import os
from models.api.user import UserAPI
from models.api.admin import AdminAPI


def setup_admin():

    # setup admin user
    admin_username = "test_admin"
    admin_password = "test1234"
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/")
    user_api = UserAPI(BACKEND_URL)
    signup_response = user_api.signup(admin_username, admin_password)

    if signup_response.status_code == 200:
        print("Admin user created successfully.")
    else:
        print("Admin user already exists or there was an error.")

    # login admin user
    login_response = user_api.login(admin_username, admin_password)
    assert login_response.status_code == 200, "Could not log in admin"
    token = user_api.token

    # create product
    admin_api = AdminAPI(BACKEND_URL, token)
    admin_api.create_product("TestProduct37")

    # if create_product_response.status_code == 200:
    #     print("Product created successfully.")
    # else:
    #     print("Product already exists or there was an error.")


def setup_new_user():
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/")
    user_api = UserAPI(BACKEND_URL)

    # create new user
    username = "test_user"
    password = "test_password"
    signup_response = user_api.signup(username, password)


    if signup_response.status_code == 200:
        print("New user created successfully.")
    else:
        print("User already exists or there was an error.")

    # logga in newuser
    login_response = user_api.login(username, password)
    assert login_response.status_code == 200, "Could not log in new user"

    # assign product to new user

    add_product_response = user_api.add_product_to_user("TestProduct37")

    if add_product_response.status_code == 200:
        print("Product added to user successfully.")
    else:
        print("There was an error adding the product to the user.")


if __name__ == "__main__":
    setup_admin()
    setup_new_user()