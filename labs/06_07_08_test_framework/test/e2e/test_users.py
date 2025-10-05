from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import libs.utils
import os

def test_signup(page: Page):
    """Test user signup flow"""
    frontend_url = os.environ.get('FRONTEND_URL', 'http://app-frontend:5173')
    username = libs.utils.generate_string_with_prefix("e2euser")
    password = "Test123!@#"
    
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    
    home_page.navigate(frontend_url)
    home_page.go_to_signup()
    signup_page.signup(username, password)
    page.wait_for_timeout(2000)
    signup_page.go_to_home()
    home_page.login(username, password)
    
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible(timeout=10000)

def test_user_sees_products(page: Page):
    """Test that logged in user can see their products"""
    frontend_url = os.environ.get('FRONTEND_URL', 'http://app-frontend:5173')
    username = libs.utils.generate_string_with_prefix("e2euser")
    password = "Test123!@#"
    
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    
    home_page.navigate(frontend_url)
    home_page.go_to_signup()
    signup_page.signup(username, password)
    page.wait_for_timeout(2000)
    signup_page.go_to_home()
    home_page.login(username, password)
    
    expect(page.get_by_text("Your Products:")).to_be_visible(timeout=10000)