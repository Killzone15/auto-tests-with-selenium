import time
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
