from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
from models.api.user import UserAPI
import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix("user", 8)
    password = "pass1234"

    home_page = HomePage(page)
    signup_page = SignupPage(page)
    user_page = UserPage(username, page)

    # Navigate to home
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # Go to signup page
    home_page.go_to_signup()
    page.wait_for_load_state("networkidle")

    # Signup
    signup_page.signup(username, password)
    page.wait_for_load_state("networkidle")

    # Klicka sign up
    signup_page.signup_btn_login.click()
    page.wait_for_load_state("networkidle")

    # Log in
    home_page.login(username, password)
    page.wait_for_load_state("networkidle")

    # Wait until the welcome message appears
    user_page.title_user.wait_for(state="visible", timeout=5000)

    # Assertions
    assert username in user_page.title_user.inner_text()
    assert user_page.title_user.is_visible(), "User title is not visible"
    assert user_page.title_user.inner_text() == f"Welcome, {username}!"


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_signup_auth_user(page: Page):
    username = "user_1"
    password = "pass1234"

    home_page = HomePage(page)
    user_page = UserPage(username, page)
    user_api = UserAPI("http://localhost:8000")

    # Get token from API
    response = user_api.login(username, password)
    assert response.status_code == 200
    token = user_api.token

    # Set token i localStorage before loading
    page.add_init_script(f"""
        window.localStorage.setItem("token", "{token}");
    """)

    # 3) Go directly to homepage
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # 4) Load users produkts
    user_page.get_user_products()
    page.wait_for_load_state("networkidle")

    # 5) Verify products or empty state
    products = user_page.get_user_products()
    if products:
        print(f"Found products: {products}")
        assert len(products) > 0
    else:
        no_products_locator = page.get_by_text("No products assigned.")
        assert no_products_locator.is_visible()
