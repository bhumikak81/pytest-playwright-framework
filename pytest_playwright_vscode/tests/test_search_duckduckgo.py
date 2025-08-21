from pages.duckduckgo_page import DuckDuckGoPage

def test_duckduckgo_search(page):
    ddg = DuckDuckGoPage(page)
    ddg.open()
    ddg.search("Playwright Python")
    assert "Playwright" in (ddg.top_result_text() or "")
