import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose language: en or fr or any other")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument('headless')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        browser = webdriver.Chrome(
            options=options,
            executable_path=os.path.join(current_dir, 'chromedriver')
        )
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        os.environ['MOZ_HEADLESS'] = '1'
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
