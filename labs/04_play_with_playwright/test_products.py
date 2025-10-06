import re  
from playwright.sync_api import Page

def test_open_google(page: page):
    page.goto("http://google.com/")