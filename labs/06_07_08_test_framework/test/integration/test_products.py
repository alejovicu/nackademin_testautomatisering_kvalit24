import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI

BASE_URL = "http://host.docker.internal:8000"

def test_add_product_to_catalog():
    admin_username = libs.utils.generate_string_with_prefix("admin", 6)
    admin_password = "admin123"
    
    admin_api = UserAPI(BASE_URL)
    admin_api.signup(admin_username, admin_password)
    admin_api.login(admin_username, admin_password)
    
    admin_actions = AdminAPI(BASE_URL, admin_api.token)
    
    product_name = libs.utils.generate_string_with_prefix("Product", 6)
    initial_count = admin_actions.get_current_product_count()
    
    response = admin_actions.create_product(product_name)
    assert response.status_code == 200
    
    final_count = admin_actions.get_current_product_count()
    assert final_count == initial_count + 1

def test_remove_product_from_catalog():
    admin_username = libs.utils.generate_string_with_prefix("admin", 6)
    admin_password = "admin123"
    
    admin_api = UserAPI(BASE_URL)
    admin_api.signup(admin_username, admin_password)
    admin_api.login(admin_username, admin_password)
    
    admin_actions = AdminAPI(BASE_URL, admin_api.token)
    
    product_name = libs.utils.generate_string_with_prefix("Product", 6)
    admin_actions.create_product(product_name)
    initial_count = admin_actions.get_current_product_count()
    
    response = admin_actions.delete_product_by_name(product_name)
    assert response.status_code == 200
    
    final_count = admin_actions.get_current_product_count()
    assert final_count == initial_count - 1