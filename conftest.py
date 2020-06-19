import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
