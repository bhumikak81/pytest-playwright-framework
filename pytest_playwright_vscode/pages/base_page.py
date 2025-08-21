class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url)

    def title(self) -> str:
        return self.page.title()
