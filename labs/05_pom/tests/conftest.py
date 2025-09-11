# conftest.py
import pytest
import time
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Launch a single browser for the whole test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(browser):
    """Open a single page for all tests in the session."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def product_name():
    # Generera en unik produkt som kan användas av flera tester
    import time
    return f"apple-{int(time.time())}"

