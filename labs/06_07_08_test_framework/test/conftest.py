from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os


def setup():
    user_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    username = os.getenv("admin_username", "Admin_user")
    password = os.getenv("admin_password", "Admin53")
    normal_user = "user83"
    normal_password = "pass83"
    course01 = os.getenv("product01", "CI/CD pipelines med Jenkins")
    course02 = os.getenv("product02", "Frontend programering 1")
    course03 = os.getenv("product03", "Backend programering 1")
    course04 = os.getenv("product04", "Avancerad Java-programmering")
    user_api.signup(username, password)
    user_api.signup(normal_user, normal_password)
    admin_token = user_api.login_token(username, password)
    admin_api.set_token(admin_token)
    admin_api.create_product(course01)
    admin_api.create_product(course02)
    admin_api.create_product(course03)
    admin_api.create_product(course04)
    token = user_api.login_token(normal_user, normal_password)
    user_api.add_product_to_user(token, course02)
    user_api.add_product_to_user(token, course03)


def reset():
    user_api = UserAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    admin_api = AdminAPI(os.getenv("BACKEND_URL", "http://localhost:8000"))
    admin_username = os.getenv("admin_username", "Admin_user")
    admin_password = os.getenv("admin_password", "Admin53")
    course01 = os.getenv("product01", "CI/CD pipelines med Jenkins")
    course02 = os.getenv("product02", "Frontend programering 1")
    course03 = os.getenv("product03", "Backend programering 1")
    course04 = os.getenv("product04", "Avancerad Java-programmering")
    admin_token = user_api.login_token(admin_username, admin_password)
    admin_api.set_token(admin_token)
    username = "user83"
    password = "pass83"
    user_token = user_api.login_token(username, password)
    user_api.remove_product_from_user(user_token, course02)
    user_api.remove_product_from_user(user_token, course03)
    admin_api.delete_product_by_name(course01)
    admin_api.delete_product_by_name(course02)
    admin_api.delete_product_by_name(course03)
    admin_api.delete_product_by_name(course04)
    admin_api.delete_product_by_name("Java-programmering för nybörjare")
