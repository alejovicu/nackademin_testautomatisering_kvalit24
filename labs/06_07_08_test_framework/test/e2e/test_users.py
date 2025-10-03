import uuid
from playwright.sync_api import Page, expect
from models.ui.signup import SignupPage
from models.ui.home import HomePage



def test_signup(page: Page):
    username = f"user{uuid.uuid4().hex}"
    password = "user1234"
    
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()
    
    signup_page = SignupPage(page)
    
    with page.expect_response(lambda r: r.url.endswith("/signup") and r.status == 200):
        signup_page.signup(username, password)
    
    
    page.wait_for_load_state("networkidle")
    
    signup_page.go_to_home()
    home_page.login(username, password)
    expect(page.get_by_text(f"Welcome, {username}")).to_be_visible()


def test_login_as_user(page: Page):
    home_page = HomePage(page)
    
    home_page.navigate()
    
    username = "user1"
    password = "user1234"
    home_page.login(username, password)
    
    expect(page.get_by_text(f"Welcome, {username}")).to_be_visible()
    expect(page.get_by_role("button", name="Logout")).to_be_visible()
    expect(page.get_by_text("Your Products:")).to_be_visible()
        


def test_login_as_admin(page: Page):
    home_page = HomePage(page)
    
    home_page.navigate()
    home_page.login("admin", "admin1234")
    
  
    expect(page.get_by_text("Welcome, admin!")).to_be_visible()
  
    expect(page.get_by_text("Add new product:")).to_be_visible()
    expect(page.get_by_placeholder("Product Name")).to_be_visible()
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()
    
    expect(page.get_by_role("button", name="Logout")).to_be_visible()