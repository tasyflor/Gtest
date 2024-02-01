from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50, 10)

    @staticmethod
    def get_selenium_by(find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'id': By.ID,
                    'name': By.NAME,
                    'class_name': By.CLASS_NAME,
                    'link_text': By.LINK_TEXT,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)),
                               locator_name)