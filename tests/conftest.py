import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# Scope of fixtures for tests here
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://gcore.com/hosting'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()
    driver.quit()

