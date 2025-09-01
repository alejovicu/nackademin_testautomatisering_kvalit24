from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

def test_open_google(page: Page):
    page.goto("https://www.google.com/")
    