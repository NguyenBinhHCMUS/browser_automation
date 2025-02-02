from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote_parser import QuoteParser

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, QuotesPageLocators.QUOTE)]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN)
        print(element)
        return Select(element)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)