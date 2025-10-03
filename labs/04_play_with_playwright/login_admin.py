from playwright.sync_api import Page, expect

def test_admin_login(page: Page):
    page.goto("https://dinapp/admin")
    page.fill("#username", "admin")
    page.fill("#password", "admin123")
    page.click("button[type=submit]")
    expect(page.locator("text=Dashboard")).to_be_visible()
