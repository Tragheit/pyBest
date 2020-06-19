import pytest


from pages.duck_duck_go_home_page import DuckDuckGoHomePage
from pages.duck_duck_go_search_page import DuckDuckGoSearchPage
from pages.duck_duck_go_result_page import DuckDuckGoResultPage

from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/test_scenario.feature')

@given('the DuckDuckGo home page is displayed')
def ddg_home(driver):
    home_page = DuckDuckGoHomePage(driver)
    home_page.goToPage()


@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(driver, phrase):
    search_page = DuckDuckGoSearchPage(driver)
    search_page.search(phrase)


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(driver, phrase):
    result_page = DuckDuckGoResultPage(driver)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(phrase) > 0
    assert result_page.search_input_value() == phrase
