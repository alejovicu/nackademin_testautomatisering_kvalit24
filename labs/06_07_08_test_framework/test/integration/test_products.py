import pytest
from models.api.admin import AdminAPI
from models.api.user import UserAPI


### RUN 'pytest test_data_admin.py' first to register admin credentials


# Store admin login token
@pytest.fixture(scope="session")
def get_admin_token():
    user_api = UserAPI("http://localhost:8000")
    credentials = user_api.login("user_admin", "test_1234")
    token = credentials.json().get("access_token")
    return token


# Prepare adding product for removal
@pytest.fixture(scope="session")
def add_product_for_removal(get_admin_token):
    admin_api = AdminAPI("http://localhost:8000")
    product_name = "dummy_product"
    new_product = admin_api.create_product(get_admin_token, product_name)
    return new_product


####################################################
# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
#####################################################
def test_add_product_to_catalog(get_admin_token):
    ### ARRANGE - Given I am an admin user​
    product_name = "test_product"
    admin_api = AdminAPI("http://localhost:8000")

    ### ACT - When I add a product to the catalog​
    # get pre-addition product count
    pre_addition_product_count = admin_api.get_current_product_count(get_admin_token)
    # add product
    add_product = admin_api.create_product(get_admin_token, product_name)
    # get product list
    product_list = admin_api.get_current_products(get_admin_token)
    # get post-addition product count
    post_addition_product_count = admin_api.get_current_product_count(get_admin_token)

    ### ASSERT - Then The product is available to be used in the app
    # Assert status code for deletion
    assert add_product.status_code == 200
    # Does product appear in stock?
    assert product_list[-1].get("name") == product_name
    # Has stock count increased by 1?
    assert post_addition_product_count == pre_addition_product_count + 1


##############################################################
# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
###############################################################
def test_remove_product_from_catalog(get_admin_token, add_product_for_removal):
    ### ARRANGE - Given I am an admin user​
    admin_api = AdminAPI("http://localhost:8000")
    #  Fetch added product for removal
    new_product = add_product_for_removal
    new_product_id = new_product.json().get("id")
    product_name = new_product.json().get("name")
    # get pre-removal product count
    pre_removal_product_count = admin_api.get_current_product_count(get_admin_token)

    ### ACT - When I remove a product from the catalog​
    # Delete recently added product
    delete_product = admin_api.delete_product_by_id(get_admin_token, new_product_id)
    # get product list post-deletion
    product_list = admin_api.get_current_products(get_admin_token)
    # get post-removal product count
    post_removal_product_count = admin_api.get_current_product_count(get_admin_token)

    ### ASSERT - Then The product should not be listed in the app to be used
    # Assert status code for deletion
    assert delete_product.status_code == 200
    # Has the latest product been removed from stock?
    assert product_list[-1].get("name") != product_name
    # Has stock count decreased by 1?
    assert post_removal_product_count == pre_removal_product_count - 1
