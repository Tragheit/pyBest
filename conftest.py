import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--preview", action="store_true",
                     default=False, help="Disables headless mode")


@pytest.fixture(scope='function')
def preview(request):
    preview = request.config.option.preview
    return preview


@pytest.fixture(scope="function", autouse=True)
def driver(preview, request):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--search-engine-choice-country")


    if not preview:
        options.add_argument('--headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
