from pages.base_page import BasePage

class DuckDuckGoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_box = "input[name='q']"
        self.result_links = "a.result__a, a[data-testid='result-title-a']"

    def open(self):
        self.visit("https://duckduckgo.com/")

    def search(self, query: str):
        self.page.fill(self.search_box, query)
        self.page.keyboard.press("Enter")
        self.page.wait_for_selector(self.result_links)

    def top_result_text(self) -> str:
        return self.page.text_content(self.result_links)
