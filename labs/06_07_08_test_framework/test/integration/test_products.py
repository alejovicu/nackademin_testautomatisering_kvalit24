import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI

def test_add_product_to_catalog(base_url, admin_credentials):
    """Test admin can add product to catalog"""
    admin_api_client = UserAPI(base_url)
    login_response = admin_api_client.login(
        admin_credentials['username'],
        admin_credentials['password']
    )
    assert login_response.status_code == 200
    
    admin_api = AdminAPI(base_url, admin_api_client.token)
    product_name = libs.utils.generate_string_with_prefix("IntProduct")
    initial_count = admin_api.get_current_product_count()
    
    create_response = admin_api.create_product(product_name)
    assert create_response.status_code == 200
    
    new_count = admin_api.get_current_product_count()
    assert new_count == initial_count + 1

def test_remove_product_from_catalog(base_url, admin_credentials):
    """Test admin can remove product from catalog"""
    admin_api_client = UserAPI(base_url)
    login_response = admin_api_client.login(
        admin_credentials['username'],
        admin_credentials['password']
    )
    assert login_response.status_code == 200
    
    admin_api = AdminAPI(base_url, admin_api_client.token)
    product_name = libs.utils.generate_string_with_prefix("IntProduct")
    admin_api.create_product(product_name)
    initial_count = admin_api.get_current_product_count()
    
    delete_response = admin_api.delete_product_by_name(product_name)
    assert delete_response is not None
    assert delete_response.status_code == 200
    
    new_count = admin_api.get_current_product_count()
    assert new_count == initial_count - 1