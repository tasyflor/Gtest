import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# Scope of fixtures for tests here
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use 'headless' if don`t need browser UI ("chrome if need UI")
    options.add_argument('--start-maximized')
    options.add_argument('window-size=1200x600')
    options.add_experimental_option("detach", True)
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://gcore.com/hosting'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    #driver.close()
    #driver.quit()

