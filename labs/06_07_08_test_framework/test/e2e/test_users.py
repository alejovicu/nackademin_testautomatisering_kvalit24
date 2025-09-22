from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage

import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):

    #Generates unique username for test
    username = libs.utils.generate_string_with_prefix()
    password = "Test1234"

    
    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()



    sign_up = SignupPage(page)
    #wait for  signup request to finish before login
    with page.expect_response(lambda r: r.url.endswith("/signup") and r.status ==200):
        sign_up.signup(username,password)
    sign_up.go_to_home()


    home_page.login(username,password)
    
    
    expect(page.get_by_text("Your Products:")).to_be_visible()





# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login_user(page: Page):

    username = "malle"
    password = "1234"

    
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username,password)


    expect(page.get_by_text("Your Products:")).to_be_visible()





