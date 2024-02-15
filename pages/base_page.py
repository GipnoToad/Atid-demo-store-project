from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_clickable(self, locator: tuple, wait=5):
        try:
            WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable(locator))
            return True
        except:
            raise AssertionError(f'Element: {locator} is not clickable.')

    def click_element(self, locator: tuple):
        try:
            self.element_is_clickable(locator)
            self.browser.find_element(*locator).click()
        except:
            raise AssertionError(f'Failed to click element: {locator}.')

    def element_is_visible(self, locator: tuple, wait=5):
        try:
            WebDriverWait(self.browser, wait).until(EC.visibility_of_element_located(locator))
        except:
            raise AssertionError(f'Element: {locator} is not visible.')
