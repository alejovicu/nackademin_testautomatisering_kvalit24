import re
from playwright.sync_api import Page, expect


def test_exercise(page: Page):
    page.goto(
        "https://www.qa-practice.com/elements/input/simple", wait_until="networkidle"
    )
    page.get_by_placeholder("Submit me").fill("Holabandola")
    page.keyboard.press("Enter")


def test_exercise_2(page: Page):
    page.goto(
        "https://www.qa-practice.com/elements/button/simple", wait_until="networkidle"
    )
    button = page.locator("#submit-id-submit")
    expect(button).to_be_enabled()
    button.click()

    result_element = page.locator("#result-text")
    assert result_element.inner_text() == "Submitted2", (
        "What error do you ask? It was a freaking 2 in the end"
    )
