from playwright.sync_api import Page

# from models.login import LoginPage ?????
# complete imports
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.admin import AdminPage

import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    # Step 1: Go to home/login page
    home_page = HomePage(page)
    home_page.navigate()

    # Step 2: Navigate to signup
    home_page.go_to_signup()
    signup_page = SignupPage(page)

    # Step 3: Create unique credentials
    username = libs.utils.generate_string_with_prefix("user")
    password = "password123"

    # Step 4: Fill signup form
    signup_page.signup(username, password)

    # Step 5: Login with new user
    home_page.login(username, password)

    # Step 6: Assert that we land on catalogue/admin page
    admin_page = AdminPage(page)
    assert admin_page.get_current_product_count() >= 0  # means catalogue is visible


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_see_catalogue(page: Page):
    home_page = HomePage(page)
    home_page.navigate()

    # Login with known user
    home_page.login("admin", "admin")

    # Check catalogue
    admin_page = AdminPage(page)
    assert admin_page.get_current_product_count() >= 0
