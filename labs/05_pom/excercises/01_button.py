from playwright.sync_api import Page


def test_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/simple")

    # The user should be able to click the button.
    button_element = page.locator("#submit-id-submit")

    # The button should be labeled Click.
    button_element.click()

    # After pressing the button, the user should be shown confirmation that the button was pressed.
    result_element = page.locator("#result-text")
    assert result_element.inner_text() == "Submitted"

    page.get_by_text("Submitted")

