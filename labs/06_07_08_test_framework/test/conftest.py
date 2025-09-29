def pytest_sessionstart(session):
    from models.api.user import UserAPI
    from models.api.admin import AdminAPI
    import os

    VITE_BACKEND_URL = os.getenv("VITE_BACKEND_URL", "http://localhost:8000")

    api_base = VITE_BACKEND_URL
    user_api = UserAPI(api_base)

    # Create users
    user_api.signup("admin", "1234")
    user_api.signup("testuser00", "1234")
    user_api.signup("testuser11", "1234")

    # Login as admin to create products
    user_api.login("admin", "1234")
    admin_api = AdminAPI(api_base, token=user_api.token)
    admin_api.create_product("testproduct00")
    admin_api.create_product("testproduct11")

    # Assign products to testuser00
    user_api.login("testuser00", "1234")
    user_api.add_product_to_user("testproduct00")
    user_api.add_product_to_user("testproduct11")

    # testuser11 has no products
    print("Test data setup via API completed!")
