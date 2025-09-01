import re
from playwright.sync_api import Page, expect

def test_basic_duckduckgo_search(page:Page):
    #Given the DuckDuckGo home page is displayed
    page.goto("https://duckduckgo.com/")

    #When the user searches for a phrase
    search_phrase = "test"
    page.locator('#searchbox_input').fill(search_phrase)
    page.locator("button[aria-label='Search']").click()

    #Then the search result query is the phrase
    search_input = page.locator("#search_form_input")
    expect(search_input).to_have_value(search_phrase)

    #And the search result links pertain to the phrase
    results = page.locator("a[data-testid='result-title-a']")
    texts = results.all_text_contents()
    assert any(word.lower() in t.lower() for t in texts for word in search_phrase.split()), \
        f"No search results contained any part of the phrase: {search_phrase}"

    #And the search result title contains the phrase
    expect(page).to_have_title(re.compile(search_phrase, re.IGNORECASE))