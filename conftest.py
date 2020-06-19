import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
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
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')

    if not preview:
        options.add_argument('--headless')

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), service_log_path='NUL', options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
