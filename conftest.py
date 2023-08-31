from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Set the language for the tests (default is English)")


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    service = Service(executable_path=binary_path)
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
