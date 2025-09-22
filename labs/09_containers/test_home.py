import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Run in headless mode
        yield browser
        browser.close()

def test_home_load(browser):
    # Read the APP_FRONT_URL environment variable
    app_front_url = os.getenv("APP_FRONT_URL", "http://localhost:5173")  # Default to localhost if not set
    page = browser.new_page()
    page.goto(app_front_url)  # Use the environment variable here
    assert "Course App" in page.title()