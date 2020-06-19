import pytest

from pages.base_page import BasePage

class DuckDuckGoHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def goToPage(self):
        self.driver.get("https://duckduckgo.com/")
