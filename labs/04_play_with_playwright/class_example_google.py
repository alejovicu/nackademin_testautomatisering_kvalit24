import time
from playwright.sync_api import Page

def test_open_google(page: Page):
    page.goto("https://www.google.com/") 
    time.sleep(5)