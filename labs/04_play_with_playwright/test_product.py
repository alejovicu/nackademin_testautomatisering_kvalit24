import re
from playwright.sync_api import Page, expect


# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")
#     expect(page).to_have_title(re.compile("Playwright"))
#     expect(page.get_by_text("Get started")).to_be_visible()


# def test_basic_duckduckgo_search(page: Page):

#     # Arrange 
#     search_term = "Hello"

#     # Act

#     page.goto("https://duckduckgo.com/")
#     # Given the DuckDuckGo home page is displayed
#     expect(page).to_have_title(re.compile("DuckDuckGo"))
#     # When the user searches for a phrase
#     page.locator("#searchbox_input").fill(search_term)
#     page.locator('button[aria-label="Search"]').click()
#     # Then the search result query is the phrase
#     expect(page.locator('#search_form_input')).to_have_value(re.compile(search_term))
#     # And the search result links pertain to the phrase
#     expect(page.get_by_role("link", name=re.compile(search_term, re.IGNORECASE)).first).to_be_visible()
#     # And the search result title contains the phrase
#     expect(page).to_have_title(re.compile(search_term))

def admin_login(page: Page):
    url='http://localhost:5173'
    username = "admin"
    password = "admin"

    page.goto(url)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

def test_admin_add_product(page: Page):

    # Arrange
    admin_login(page)
    
    product = "Banan"
    
    # Act
    
    products = page.locator('.product-item')
    expect(products.first).to_be_visible()
    number_of_products_before = products.count()

    page.get_by_placeholder("Product Name").fill(product)
    page.get_by_role("button", name="Create Product").click()

    products = page.locator('.product-item')
    expect(products).to_have_count(number_of_products_before + 1)

    expect(page.get_by_text("Welcome, admin!")).to_be_visible()


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_admin_remove_product(page: Page):

     # Arrange
    admin_login(page)
    product = "Banan"

    
    products = page.locator('.product-item')
    expect(products.first).to_be_visible()
    number_of_products_before = products.count()

    products = page.locator(".product-grid")
    product = products.locator(".product-item").nth(-1)  # e.g., 6th item visually
    product.get_by_role("button", name="Delete").click()
    
    products = page.locator('.product-item')
    expect(products).to_have_count(number_of_products_before - 1)
