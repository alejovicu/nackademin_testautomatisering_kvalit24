from playwright.sync_api import Page, expect
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignUpPage
from models.admin import AdminPage
from models.user import UserPage
import time

# Admin credentials
ADMIN_USER = "user"
ADMIN_PASS = "Pass123"


def test_add_user(page: Page):
    """Test registering and logging in a normal user."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignUpPage(page)
    user_page = UserPage(page)

    # Navigate to homepage
    home_page.navigate()

    # Go to signup page and register user
    login_page.navigate_to_signup()
    signup_page.sign_up("user", "Pass123")

    # Go back to login and login
    signup_page.nav_to_login()
    login_page.login("user", "Pass123")

    # TODO: check that products are not visible for normal user
    # expect(user_page.product_item).not_to_be_visible()

    # Logout user
    user_page.logout_user()


def test_add_product_to_catalog(page: Page, product_name):
    """Test adding a product as admin."""
    # Generate a unique product name to avoid duplicates
    product = f"apple-{int(time.time())}"
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    # Logout if admin is already logged in
    try:
        admin_page.logout_admin()
    except:
        pass

    # Navigate to login page
    page.goto("http://localhost:5173/login")

    # Wait for login inputs
    expect(login_page.input_username).to_be_visible()
    expect(login_page.input_password).to_be_visible()

    # Login as admin
    login_page.login(ADMIN_USER, ADMIN_PASS)

    # Wait for admin page to load
    expect(admin_page.input_product).to_be_visible()

    # Create product
    admin_page.create_product(product_name)
    expect(admin_page.product_item.filter(has_text=product_name).first).to_be_visible()

    # Verify the newly created product is visible (use .first to avoid strict mode violation)
    expect(admin_page.product_item.filter(has_text=product).first).to_be_visible()

    # Logout admin
    admin_page.logout_admin()


def test_remove_product_from_catalog(page: Page, product_name):
    """Test removing a product as admin."""
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    # Logout if admin is already logged in
    try:
        admin_page.logout_admin()
    except:
        pass

    # Navigate to login page
    page.goto("http://localhost:5173/login")

    # Wait for login inputs
    expect(login_page.input_username).to_be_visible()
    expect(login_page.input_password).to_be_visible()

    # Login as admin
    login_page.login(ADMIN_USER, ADMIN_PASS)

    # Wait for product list to load
    expect(admin_page.product_item.first).to_be_visible()

    # Delete product
    admin_page.delete_product(product_name)

    # Verify product no longer visible
    expect(admin_page.product_item.filter(has_text=product_name).first).not_to_be_visible()

    # Logout admin
    admin_page.logout_admin()
