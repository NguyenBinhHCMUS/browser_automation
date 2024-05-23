from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quotes_page import QuotesPage

service = Service(executable_path='/usr/local/bin/chromedriver')
chrome = webdriver.Chrome()
# chrome.get('http://quotes.toscrape.com')
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotesPage(chrome)

# for quote in page.quotes:
#     print(quote)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)
